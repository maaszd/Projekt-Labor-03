import random
import sqlite3
from collections import namedtuple
from pathlib import Path

from hero import Hero
from monster import Monster
from item import Item, ItemType, ItemRarity

PROJEKT_MAPPA = Path(__file__).resolve().parent
DB_UTVONAL = PROJEKT_MAPPA / "jatek.db"

# A seed.sql verziója (PRAGMA user_version). Ha új alapadatot teszel a seed.sql-be, emeld eggyel:
# a seed.sql minden sora INSERT OR IGNORE, ezért a meglévő adatbázison is biztonságosan újra lefut.
SEED_VERZIO = 2

# Új játékos ezeket a tárgyakat kapja (Item.id-k a seed.sql-ből)
KEZDO_ITEMEK = [1, 2, 3, 4, 5, 6]

InventorySor = namedtuple("InventorySor", "item slot mennyiseg fel_van_szerelve")


class Adatbazis:
    def __init__(self, utvonal=DB_UTVONAL):
        self.conn = sqlite3.connect(str(utvonal))
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("PRAGMA foreign_keys = ON")  # SQLite-ban kapcsolatonként kell!
        self._letrehozas()

    def _letrehozas(self):
        """Táblák létrehozása; az alapadatok betöltése/bővítése a seed.sql-ből (verziószám alapján)."""
        self.conn.executescript((PROJEKT_MAPPA / "schema.sql").read_text(encoding="utf-8"))
        verzio = self.conn.execute("PRAGMA user_version").fetchone()[0]
        if verzio < SEED_VERZIO:
            self.conn.executescript((PROJEKT_MAPPA / "seed.sql").read_text(encoding="utf-8"))
            self.conn.execute(f"PRAGMA user_version = {SEED_VERZIO}")
            self.conn.commit()

    def close(self):
        self.conn.close()

    # Játékos
    def jatekos_betoltes_vagy_letrehozas(self, nev="Kalandor", slot=1):
        """-> (jatekos_id, Hero). Ha a slotban nincs mentés, új játékost hoz létre."""
        sor = self.conn.execute(
            "SELECT * FROM Jatekos WHERE mentes_slot = ? ORDER BY id LIMIT 1", (slot,)
        ).fetchone()
        if sor is None:
            return self._uj_jatekos(nev, slot)
        return sor["id"], self._hero(sor)

    def _uj_jatekos(self, nev, slot):
        hos = Hero(name=nev, current_hp=100, max_hp=100, damage=15, defense=5)
        with self.conn:
            cur = self.conn.execute(
                """INSERT INTO Jatekos (nev, szint, tapasztalati_pont, aktualis_eletero, max_eletero,
                                        tamadoero, vedekezes, kezdemenyezes, arany, mentes_slot)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (hos.name, hos.level, hos.xp, hos.current_hp, hos.max_hp,
                 hos.damage, hos.defense, hos.initiative, hos.gold, slot),
            )
            jatekos_id = cur.lastrowid
            self.conn.executemany(
                "INSERT INTO Inventory (jatekos_id, item_id) VALUES (?, ?)",
                [(jatekos_id, item_id) for item_id in KEZDO_ITEMEK],
            )
        return jatekos_id, hos

    @staticmethod
    def _hero(sor):
        return Hero(
            name=sor["nev"],
            current_hp=sor["aktualis_eletero"],
            max_hp=sor["max_eletero"],
            damage=sor["tamadoero"],
            defense=sor["vedekezes"],
            gold=sor["arany"],
            level=sor["szint"],
            xp=sor["tapasztalati_pont"],
            initiative=sor["kezdemenyezes"],
        )

    def jatekos_mentes(self, jatekos_id, hos):
        with self.conn:
            self.conn.execute(
                """UPDATE Jatekos SET nev = ?, szint = ?, tapasztalati_pont = ?, aktualis_eletero = ?,
                          max_eletero = ?, tamadoero = ?, vedekezes = ?, kezdemenyezes = ?, arany = ?,
                          utolso_mentes = CURRENT_TIMESTAMP
                   WHERE id = ?""",
                (hos.name, hos.level, hos.xp, hos.current_hp, hos.max_hp,
                 hos.damage, hos.defense, hos.initiative, hos.gold, jatekos_id),
            )

    #  Szörny
    def szorny_betoltes(self, szorny_id):
        """Új, teljes életerejű Monster példány a szörny-sablonból."""
        sor = self.conn.execute("SELECT * FROM Szorny WHERE id = ?", (szorny_id,)).fetchone()
        if sor is None:
            raise KeyError(f"Nincs ilyen szörny az adatbázisban: id={szorny_id}")
        return Monster(
            name=sor["nev"],
            current_hp=sor["alap_hp"],
            max_hp=sor["alap_hp"],
            damage=sor["tamadas"],
            defense=sor["vedekezes"],
            initiative=sor["kezdemenyezes"],
            id_szam=sor["id"],
            is_boss=bool(sor["is_boss"]),
            title_reward=sor["titulus_jutalom"],
        )

    #  Map
    def map_lekeres(self, nev):
        sor = self.conn.execute("SELECT * FROM Map WHERE nev = ?", (nev,)).fetchone()
        if sor is None:
            raise KeyError(f"Nincs ilyen pálya az adatbázisban: {nev}")
        return dict(sor)

    # Inventory
    @staticmethod
    def _item(sor):
        return Item(
            item_id=sor["id"],
            name=sor["nev"],
            item_type=ItemType[sor["tipus"]],
            rarity=ItemRarity[sor["ritkasag"]],
            bonus_attack=sor["bonus_tamadas"],
            bonus_defense=sor["bonus_vedekezes"],
            gold_value=sor["arany_ertek"],
            image_path=sor["kep_utvonal"],
        )

    def inventory(self, jatekos_id):
        sorok = self.conn.execute(
            """SELECT i.*, inv.mennyiseg, inv.fel_van_szerelve
               FROM Inventory inv JOIN Item i ON i.id = inv.item_id
               WHERE inv.jatekos_id = ? ORDER BY i.id""",
            (jatekos_id,),
        ).fetchall()
        return [
            InventorySor(self._item(s), s["slot"], s["mennyiseg"], bool(s["fel_van_szerelve"]))
            for s in sorok
        ]

    def item_hozzaadas(self, jatekos_id, item_id, mennyiseg=1):
        """Ha már van ilyen tárgya a játékosnak, a mennyiséget növeli."""
        with self.conn:
            self.conn.execute(
                """INSERT INTO Inventory (jatekos_id, item_id, mennyiseg) VALUES (?, ?, ?)
                   ON CONFLICT(jatekos_id, item_id)
                   DO UPDATE SET mennyiseg = mennyiseg + excluded.mennyiseg""",
                (jatekos_id, item_id, mennyiseg),
            )

    def felszerel(self, jatekos_id, item_id):
        """Felszereli a tárgyat; a slotban lévő korábbit leveszi. False, ha nem szerelhető fel."""
        sor = self.conn.execute(
            """SELECT i.slot FROM Inventory inv JOIN Item i ON i.id = inv.item_id
               WHERE inv.jatekos_id = ? AND inv.item_id = ?""",
            (jatekos_id, item_id),
        ).fetchone()
        if sor is None or not sor["slot"]:
            return False
        with self.conn:
            self.conn.execute(
                """UPDATE Inventory SET fel_van_szerelve = 0
                   WHERE jatekos_id = ? AND fel_van_szerelve = 1
                     AND item_id IN (SELECT id FROM Item WHERE slot = ?)""",
                (jatekos_id, sor["slot"]),
            )
            self.conn.execute(
                "UPDATE Inventory SET fel_van_szerelve = 1 WHERE jatekos_id = ? AND item_id = ?",
                (jatekos_id, item_id),
            )
        return True

    def levesz(self, jatekos_id, slot):
        """Leveszi a slotban lévő tárgyat. True, ha volt mit levenni."""
        with self.conn:
            cur = self.conn.execute(
                """UPDATE Inventory SET fel_van_szerelve = 0
                   WHERE jatekos_id = ? AND fel_van_szerelve = 1
                     AND item_id IN (SELECT id FROM Item WHERE slot = ?)""",
                (jatekos_id, slot),
            )
        return cur.rowcount > 0

    # Játékmező (mentett állás)
    def jatekmezo_mentes(self, jatekos_id, map_id, szoba, x, y, hp):
        with self.conn:
            van = self.conn.execute(
                "SELECT id FROM Jatekmezo WHERE jatekos_id = ? ORDER BY id DESC LIMIT 1",
                (jatekos_id,),
            ).fetchone()
            if van:
                self.conn.execute(
                    """UPDATE Jatekmezo SET map_id = ?, aktualis_map_id = ?, aktualis_szoba = ?,
                              hos_x = ?, hos_y = ?, aktualis_hp = ? WHERE id = ?""",
                    (map_id, map_id, szoba, x, y, hp, van["id"]),
                )
            else:
                self.conn.execute(
                    """INSERT INTO Jatekmezo (jatekos_id, map_id, aktualis_map_id, aktualis_szoba,
                                              hos_x, hos_y, aktualis_hp)
                       VALUES (?, ?, ?, ?, ?, ?, ?)""",
                    (jatekos_id, map_id, map_id, szoba, x, y, hp),
                )

    def jatekmezo_betoltes(self, jatekos_id):
        """-> dict a mentett állással, vagy None, ha még nincs mentés."""
        sor = self.conn.execute(
            "SELECT * FROM Jatekmezo WHERE jatekos_id = ? ORDER BY id DESC LIMIT 1", (jatekos_id,)
        ).fetchone()
        return dict(sor) if sor else None

    # Zsákmány (drop)
    def szorny_zsakmany(self, jatekos_id, szorny_nev, rng=random):
        """A legyőzött szörny zsákmánya. Minden drop-sorra külön dob az esély alapján, a megszerzett
        tárgyak bekerülnek a játékos inventoryjába (ha már van ilyen, a mennyiség nő).
        -> [(Item, mennyiseg), ...] (üres lista, ha nem esett semmi, vagy a szörnynek nincs dropja)"""
        dropok = self.conn.execute(
            """SELECT i.*, d.esely, d.min_mennyiseg, d.max_mennyiseg
               FROM Szorny_Drop d
               JOIN Szorny s ON s.id = d.szorny_id
               JOIN Item i   ON i.id = d.item_id
               WHERE s.nev = ? ORDER BY d.id""",
            (szorny_nev,),
        ).fetchall()
        zsakmany = []
        with self.conn:  # egy tranzakció: vagy minden tárgy bekerül, vagy egyik sem
            for d in dropok:
                if rng.random() >= d["esely"]:
                    continue
                mennyiseg = rng.randint(d["min_mennyiseg"], d["max_mennyiseg"])
                self.conn.execute(
                    """INSERT INTO Inventory (jatekos_id, item_id, mennyiseg) VALUES (?, ?, ?)
                       ON CONFLICT(jatekos_id, item_id)
                       DO UPDATE SET mennyiseg = mennyiseg + excluded.mennyiseg""",
                    (jatekos_id, d["id"], mennyiseg),
                )
                zsakmany.append((self._item(d), mennyiseg))
        return zsakmany