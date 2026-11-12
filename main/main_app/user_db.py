import os
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from user import User


class UserDatabaseManager:
    def __init__(self):
        db_nev = "users.db"
        projekt_mappa = os.path.dirname(os.path.abspath(__file__))
        self._db_utvonal = os.path.join(projekt_mappa, db_nev)

        self.conn = sqlite3.connect(self._db_utvonal)
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS felhasznalok (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nev TEXT UNIQUE NOT NULL,
                jelszo TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def felhasznalo_letezik(self, nev: str):
        cursor = self.conn.cursor()
        cursor.execute("SELECT 1 FROM felhasznalok WHERE nev = ?", (nev,))
        return cursor.fetchone() is not None

    def regisztracio(self, nev: str, jelszo: str):

        if not nev or not jelszo:
            return False, "A felhasználónév és a jelszó megadása kötelező!", None

        if self.felhasznalo_letezik(nev):
            return False, "Ez a felhasználónév már foglalt!", None

        jelszo_hash = generate_password_hash(jelszo)

        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO felhasznalok (nev, jelszo) VALUES (?, ?)",
                (nev, jelszo_hash)
            )
            self.conn.commit()
            uj_id = cursor.lastrowid

            uj_felhasznalo = User(user_id=uj_id, name=nev)
            return True, f"Sikeres regisztráció! (ID: {uj_id})", uj_felhasznalo

        except sqlite3.IntegrityError:
            return False, "Ez a felhasználónév már létezik az adatbázisban!", None
        except sqlite3.Error as e:
            return False, f"Adatbázis hiba történt: {e}", None

    def bejelentkezes(self, nev: str, jelszo: str):

        if not nev or not jelszo:
            return False, "Add meg a felhasználónevet és a jelszót!", None

        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT id, nev, jelszo FROM felhasznalok WHERE nev = ?",
            (nev,)
        )
        sor = cursor.fetchone()

        if sor is None:
            return False, "Nincs ilyen felhasználó az adatbázisban!", None

        user_id, adatbazis_nev, adatbazis_jelszo = sor

        if not check_password_hash(adatbazis_jelszo, jelszo):
            return False, "Hibás jelszó!", None

        bejelentkezett_user = User(user_id=user_id, name=adatbazis_nev)
        return True, f"Sikeres bejelentkezés! Üdv, {adatbazis_nev}!", bejelentkezett_user


