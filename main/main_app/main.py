from random import randrange
import random
import sys
import os
import json
from szoba import Szoba
from hero import Hero, GraphicalHero
from monster import Monster, GraphicalMonster
from user import User
from user_db import UserDatabaseManager
from animacio import SebzesAnimacio, KardAnimacio
from PySide6.QtCore import Qt, QSize, QObject, Signal, QTimer, QRect, QUrl
from PySide6.QtWidgets import QApplication, QLabel, QFrame, QMainWindow, QListWidget, QListWidgetItem, QAbstractItemView, QListView, QGraphicsScene, QGraphicsPixmapItem,  QGraphicsBlurEffect, QGraphicsRectItem, QGraphicsItem
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtMultimedia import QSoundEffect, QMediaPlayer, QAudioOutput
from PySide6.QtCore import Qt, QSize, QObject, Signal, QTimer, QRect
from PySide6.QtWidgets import QApplication, QHBoxLayout, QLabel, QFrame, QMainWindow, QListWidget, QListWidgetItem, QAbstractItemView, QListView, QGraphicsScene, QGraphicsPixmapItem,  QGraphicsBlurEffect, QGraphicsRectItem, QGraphicsItem, QVBoxLayout, QWidget
from PySide6.QtGui import QIcon, QPixmap, QBrush, QColor, QPen, QImage, QPainter, QRadialGradient
from ui_menu import Ui_MainWindow
from db import Adatbazis
from potion import EffectType

os.chdir(os.path.dirname(os.path.abspath(__file__)))
#textBrowserbe kiiratas miatt kell
class ConsoleRedirector(QObject):
    output_written = Signal(str)
    def write(self, text):
        sys.__stdout__.write(text)
        sys.__stdout__.flush()
        if text.strip():
            self.output_written.emit(text.strip())
    def flush(self):
        pass 

#---------------------------------------------------
#csak a kép miatt kell

          
class JatekAblak(QMainWindow):
    #potik hatásai: csak a harc idejére élnek, nem kerülnek mentésre
    poti_bonusz_dmg = 0
    regen_ertek = 0
    regen_hatralevo_korok = 0

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        # harci animációk
        self.sebzes_anim = SebzesAnimacio(self.ui)
        self.kard_anim = KardAnimacio(self.ui)

        
        #hangok 
        self.hangero = 0.7
        self.zene_hangero = 0.7
        self.beallitasok_fajl = os.path.join(os.path.dirname(os.path.abspath(__file__)), "beallitasok.json")
        hang_mappa = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "sounds")

        self.hangok = {}
        hang_fajlok = {"sword": "sword.wav", "potion": "potion.wav"}
        for nev, fajl in hang_fajlok.items():
            hang = QSoundEffect(self)
            hang.setSource(QUrl.fromLocalFile(os.path.join(hang_mappa, fajl)))
            hang.setVolume(self.hangero)
            self.hangok[nev] = hang

        #háttérzenék
        self.zene_kimenet = QAudioOutput(self)
        self.zene_kimenet.setVolume(self.zene_hangero)
        self.zene_lejatszo = QMediaPlayer(self)
        self.zene_lejatszo.setAudioOutput(self.zene_kimenet)
        self.zene_lejatszo.setLoops(QMediaPlayer.Infinite)
        self.aktualis_zene = None
        self.zenek = {
            "menu": QUrl.fromLocalFile(os.path.join(hang_mappa, "menu.mp3")),
            "kocsma": QUrl.fromLocalFile(os.path.join(hang_mappa, "kocsma.mp3")),
            "campfire": QUrl.fromLocalFile(os.path.join(hang_mappa, "campfire.mp3")),
            "kovacs": QUrl.fromLocalFile(os.path.join(hang_mappa, "Blacksmith.mp3")),
        }


        self.setWindowTitle("Projekt Labor 03 - RPG Játék")  
        self.ui.statusbar.hide()  
        self.ui.menubar.hide()    
        self.ui.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.ui.btn_dungeon_soteterdo.setText("Kripta")
        self.ui.btn_dungeon_kripta.setText("Sötét erdő")
        # --- FELHASZNÁLÓ ADATBÁZIS KEZELÉS ---
        self.userdb = UserDatabaseManager()
        self.aktualis_felhasznalo = None
        
        # --- FŐMENÜ BEÁLLÍTÁSA INDULÁSKOR ---
        
        #login / reg frame
        self.ui.stackedWidget.setCurrentIndex(7)
        #bal oszlop gombok meg a text doboz elrejtése 
        self.ui.frame_3.hide()       
        self.ui.textBrowser.hide()
        #hangerö beállitás betöltése és menü zene inditás
        self.beallitasok_betoltese()
        self.zene_inditasa("menu")

        #placeholder text a mezokben
        for mezo, szoveg in [
            (self.ui.le_login_nev, "Felhasználónév"),
            (self.ui.le_login_jelszo, "Jelszó"),
            (self.ui.le_reg_nev, "Új felhasználónév"),
            (self.ui.le_reg_jelszo, "Jelszó"),
            (self.ui.le_reg_jelszo2, "Jelszó újra"),
        ]:
            mezo.clear()
            mezo.setPlaceholderText(szoveg)

        #regisztráció vagy login gomb bekötése
        self.ui.btn_login.clicked.connect(self.login_gomb_nyomas)
        self.ui.btn_reg.clicked.connect(self.reg_gomb_nyomas)
        
        #fomenu gomb fuggvenyei
        self.ui.btn_folytatas.clicked.connect(self.jatek_folytatasa)
        self.ui.btn_beallitasok.clicked.connect(self.beallitasok_megnyitasa)
        self.ui.btn_kilepes.clicked.connect(self.close)
        self.ui.btn_kilepes_2.clicked.connect(self.vissza_a_fomenube)

        #beallitasok menu gombjai es sliderei
        self.ui.slider_hangeffektek.valueChanged.connect(self.hangeffekt_hangero_valtozott)
        self.ui.slider_hatterzene.valueChanged.connect(self.hatterzene_hangero_valtozott)
        self.ui.btn_beallitasok_mentes.clicked.connect(self.beallitasok_mentese)
        self.ui.btn_beallitasok_vissza.clicked.connect(self.vissza_a_fomenube)

        self.ui.btn_beallitasok.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(6))
        
        self.ui.btn_mentes_es_betoltes.clicked.connect(self.mentes_oldal_megnyitasa)
        #mentes es betoltes gombjai
        self.ui.btn_mentes_vegleges.clicked.connect(self.page6_mentes_gomb)
        self.ui.btn_betoltes.clicked.connect(self.page6_betoltes_gomb)
        self.ui.btn_mentes_vissza.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        
        #text dobozba terminál szöveg kiiras
        self.console_redirector = ConsoleRedirector()
        self.console_redirector.output_written.connect(self.frissit_text_browser)
        sys.stdout = self.console_redirector
        
        # Gombok összekötése stacked widgetnek az indexei alapján: 0 - főmenü, 1 - térkép, 2 - sötét erdő, 3 - karakter + hátizsák, 
        #                                                          4 - harc, 5 - mentés és betöltés, 6 - beállítások, 7 - login/regisztráció
        
        self.ui.btn_karakter.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.btn_expedicio.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.btn_dungeon_soteterdo.clicked.connect(self.belepes_soteterdobe)

        #ADATBAZIS: hős + mentett állás betöltése (ha nincs mentés, új hős jön létre)
        self.db = Adatbazis()
        self.jatekos_id, hos_statok = self.db.jatekos_betoltes_vagy_letrehozas("Kalandor")
        mentes = self.db.jatekmezo_betoltes(self.jatekos_id)

        #TÉRKÉP
        map_adat = self.db.map_lekeres("Sötét erdő")
        self.map_id = map_adat["id"]
        self.szobak = {}
        self.palya_betoltese("palya_1.json")
        kezdo_szoba = "Szoba_1"
        hos_x, hos_y = 400, 300
        if mentes and mentes.get("aktualis_szoba") in self.szobak:
            kezdo_szoba = mentes["aktualis_szoba"]
            if mentes.get("hos_x") is not None and mentes.get("hos_y") is not None:
                hos_x, hos_y = float(mentes["hos_x"]), float(mentes["hos_y"])

        self.aktualis_szoba = self.szobak.get(kezdo_szoba)
        if self.aktualis_szoba:
            self.ui.graphicsView.setScene(self.aktualis_szoba)
            self.ui.graphicsView.fitInView(self.aktualis_szoba.sceneRect(), Qt.IgnoreAspectRatio)
            self.hos = GraphicalHero("assets/hero.png", hos_x, hos_y, hos_statok)
            self.hos.setZValue(20)
            self.aktualis_szoba.addItem(self.hos)
        
        #inventory beallitasai   
        self.ui.listWidget.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.ui.listWidget.setIconSize(QSize(64, 64))
        self.ui.listWidget.setViewMode(QListWidget.IconMode)
        self.ui.listWidget.setResizeMode(QListWidget.Adjust)
        self.ui.listWidget.setMovement(QListView.Static)
        self.ui.listWidget.setSpacing(5)
        self.ui.listWidget.setStyleSheet("QListWidget::item { border: 1px solid gray; }")
        self.ui.listWidget.setGridSize(QSize(80, 80))
        
        projekt_mappa = os.path.dirname(os.path.abspath(__file__))

	    #teszt tárgyakkal
         
        self.ui.listWidget.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.ui.listWidget.setIconSize(QSize(64, 64))
        self.projekt_mappa = os.path.dirname(os.path.abspath(__file__))
        self.assets_mappa = os.path.join(self.projekt_mappa, "assets")
        
        #felszerelés slotok: a slot neve = btn_<slot> gomb (Item.slot az adatbázisban)
        self.slotok = ["kard", "mellvert", "sisak", "pajzs", "kesztyu", "cipo", "nadrag", "gyuru"]
        self.slot_alap_szoveg = {}
        for slot in self.slotok:
            gomb = getattr(self.ui, f"btn_{slot}")
            self.slot_alap_szoveg[slot] = gomb.text()
            #a felszerelt tárgyra kattintva levesszük
            gomb.clicked.connect(lambda checked=False, s=slot: self.levesz(s))

        self.inventory_frissites()
        
        self.ui.listWidget.itemDoubleClicked.connect(self.targyra_kattintott)

    #harc teszt
        
        #harc idozito
        self.harc_timer = QTimer(self)
        self.harc_timer.timeout.connect(self.auto_harc_kor)
        self.ui.btn_harcinditas.clicked.connect(self.harc_inditasa)
        #POTIK gomb a "Harc indítása" mellett (a hatások a menüből választható potikból jönnek)
        #self.btn_poti = QPushButton("Potik", self.ui.page4_harc)
        self.btn_poti.setEnabled(False)
        self.btn_poti.clicked.connect(self.poti_menu_megnyitasa)
        gomb_sor = QHBoxLayout()
        self.ui.gridLayout_4.removeWidget(self.ui.btn_harcinditas)
        gomb_sor.addWidget(self.ui.btn_harcinditas)
        gomb_sor.addWidget(self.btn_poti)
        self.ui.gridLayout_4.addLayout(gomb_sor, 1, 1, 1, 1)


        self.lenyomott_gombok = set() 
        
        #fps(60 FPS = 1000ms / 60 =~ 16ms)
        self.mozgas_timer = QTimer(self)
        self.mozgas_timer.timeout.connect(self.folyamatos_mozgas)
        self.mozgas_timer.start(16)
        self.szobavaltas_alatt = True  #amíg le nem lép az ajtóról, nincs szobaváltás

        label_stilus = """
            QLabel {
                background-color: #1e1b24;
                border: 2px solid #8c7853;
                border-radius: 6px;
                color: #f5eedc;
                padding: 5px 10px;
                font-size: 14px;
                font-weight: bold;
            }
        """
        for oldal in (self.ui.page3_karakter, self.ui.page4_harc):
            for lbl in oldal.findChildren(QLabel):
                if lbl.objectName() not in ("lbl_hos_img", "lbl_szorn_img", "sebzes_lbl"):
                    lbl.setFrameShape(QFrame.Shape.Box)
                    lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    lbl.setStyleSheet(label_stilus)
		
#----------------------__init__(self): VÉGE ---------------------------------
    
    def frissit_text_browser(self, szoveg):
        self.ui.textBrowser.append(szoveg)

    def felhasznalo_regisztracio(self, nev: str, jelszo: str):
        siker, uzenet, uj_user = self.userdb.regisztracio(nev, jelszo)
        print(uzenet)
        if siker:
            self.aktualis_felhasznalo = uj_user

    def felhasznalo_bejelentkezes(self, nev: str, jelszo: str):
        siker, uzenet, user = self.userdb.bejelentkezes(nev, jelszo)
        print(uzenet)
        if siker and user:
            self.aktualis_felhasznalo = user
            if hasattr(self, 'hos'):
                self.hos.adatok.name = user.name

    def felhasznalo_kijelentkezes(self):
        self.aktualis_felhasznalo = None
        print("Sikeresen kijelentkeztél.")
			
    def zene_inditasa(self, zene_nev):
        if zene_nev not in self.zenek:
            return
        if self.aktualis_zene == zene_nev and self.zene_lejatszo.playbackState() == QMediaPlayer.PlayingState:
            return
        self.aktualis_zene = zene_nev
        self.zene_lejatszo.setSource(self.zenek[zene_nev])
        self.zene_lejatszo.play()

    def zene_leallitasa(self):
        self.zene_lejatszo.stop()
        self.aktualis_zene = None

    def jatek_folytatasa(self):
        self.zene_leallitasa()
        self.ui.frame_3.show()
        self.ui.textBrowser.show()
        self.ui.stackedWidget.setCurrentIndex(1)
        print("Üdv újra a játékban!")

    def beallitasok_megnyitasa(self):
        self.beallitasok_ui_frissites()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page6_beallitasok)

    def beallitasok_ui_frissites(self):
        hangeffekt_szazalek = int(round(self.hangero * 100))
        hatterzene_szazalek = int(round(self.zene_hangero * 100))
        self.ui.slider_hangeffektek.setValue(hangeffekt_szazalek)
        self.ui.lbl_hangeffektek_ertek.setText(f"{hangeffekt_szazalek}%")
        self.ui.slider_hatterzene.setValue(hatterzene_szazalek)
        self.ui.lbl_hatterzene_ertek.setText(f"{hatterzene_szazalek}%")

    def hangeffekt_hangero_valtozott(self, ertek):
        self.ui.lbl_hangeffektek_ertek.setText(f"{ertek}%")

    def hatterzene_hangero_valtozott(self, ertek):
        self.ui.lbl_hatterzene_ertek.setText(f"{ertek}%")

    def beallitasok_betoltese(self):
        adatok = {"hangeffektek": 70,"hatterzene": 70}
        if os.path.exists(self.beallitasok_fajl):
            try:
                with open(self.beallitasok_fajl, "r", encoding="utf-8") as f:
                    betoltott = json.load(f)
                if isinstance(betoltott, dict):
                    adatok.update(betoltott)
            except (json.JSONDecodeError, OSError) as e:
                print(f"Nem sikerült betölteni a beállításokat: {e}")

        self.hangero = adatok["hangeffektek"] / 100.0
        self.zene_hangero = adatok["hatterzene"] / 100.0

        for hang in self.hangok.values():
            hang.setVolume(self.hangero)
        self.zene_kimenet.setVolume(self.zene_hangero)

        self.beallitasok_ui_frissites()

    def beallitasok_mentese(self):
        hangeffektek = self.ui.slider_hangeffektek.value()
        hatterzene = self.ui.slider_hatterzene.value()
        
        self.hangero = hangeffektek / 100.0
        self.zene_hangero = hatterzene / 100.0
        for hang in self.hangok.values():
            hang.setVolume(self.hangero)
        self.zene_kimenet.setVolume(self.zene_hangero)

        adatok = {"hangeffektek": hangeffektek, "hatterzene": hatterzene}
        try:
            with open(self.beallitasok_fajl, "w", encoding="utf-8") as f:
                json.dump(adatok, f, indent=4, ensure_ascii=False)
            print("Beállítások sikeresen elmentve!")
        except OSError as e:
            print(f"Hiba a beállítások mentésekor: {e}")

    def vissza_a_fomenube(self):    
        self.mentes()
        self.ui.frame_3.hide()       
        self.ui.textBrowser.hide()   
        self.ui.stackedWidget.setCurrentIndex(0) 
        self.zene_inditasa("menu")
        print("Visszatértél a főmenübe.")
    
    def keyPressEvent(self, event):
        if self.ui.stackedWidget.currentIndex() != 2:
            return
        self.lenyomott_gombok.add(event.key())

    def keyReleaseEvent(self, event):
        if self.ui.stackedWidget.currentIndex() != 2:
            return
        if event.key() in self.lenyomott_gombok:
            self.lenyomott_gombok.remove(event.key())
    
    def folyamatos_mozgas(self):
        if self.ui.stackedWidget.currentIndex() != 2 or not hasattr(self, 'hos'):
            return

        x = self.hos.x()
        y = self.hos.y()
        lepes = 3.5

        #atlos mozgas
        if Qt.Key_W in self.lenyomott_gombok or Qt.Key_Up in self.lenyomott_gombok:
            y -= lepes
        if Qt.Key_S in self.lenyomott_gombok or Qt.Key_Down in self.lenyomott_gombok:
            y += lepes
        if Qt.Key_A in self.lenyomott_gombok or Qt.Key_Left in self.lenyomott_gombok:
            x -= lepes
        if Qt.Key_D in self.lenyomott_gombok or Qt.Key_Right in self.lenyomott_gombok:
            x += lepes


        #border ellenorzes, hogy ne menjen ki a hos a jatek teren kivulre
        x = max(0, min(x, 750))
        y = max(0, min(y, 550))
        #megortenik a lepes
        self.hos.setPos(x, y)
        if hasattr(self, 'aktualis_szoba') and self.aktualis_szoba:
            self.aktualis_szoba.kod_frissites(x, y, self.hos.adatok.level)

        if hasattr(self, 'aktualis_szoba') and self.aktualis_szoba:
            for szorny in self.aktualis_szoba.szornyek:
                szorny.jarorozes()

        #ha a hos ralepett egy szornyre akkor harc kezdodik
        erintett_szornyek = [item for item in self.hos.collidingItems() if item.data(3) == "szorny"]

        if erintett_szornyek:
            
            self.aktualis_harcolt_szorny = erintett_szornyek[0]
            self.poti_hatasok_nullazasa()
            self.lenyomott_gombok.clear()

            
            
            #hos kepet es nevet frissitjuk a harci menuben
            self.ui.lbl_hos_img.setMinimumSize(QSize(180, 180))
            self.ui.lbl_hos_img.setPixmap(self.hos.pixmap().scaled(180, 180, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.ui.lbl_hos_nev.setText(f"{self.hos.adatok.name} - {self.hos.adatok.level}. szint")
            
            #szorny kepet es nevet frissitjuk a harci menuben
            szorny_harci_meret = 220 if self.aktualis_harcolt_szorny.adatok.is_boss else 180
            self.ui.lbl_szorn_img.setMinimumSize(QSize(szorny_harci_meret, szorny_harci_meret))
            self.ui.lbl_szorn_img.setPixmap(self.aktualis_harcolt_szorny.pixmap().scaled(szorny_harci_meret, szorny_harci_meret, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.ui.lbl_szorny_nev.setText(self.aktualis_harcolt_szorny.adatok.name)
            
            
            #hos es szorny statok frissitese a harci menuben
            
            bonus_dmg, bonus_def = self.hos_bonus_statok()
            self.ui.lbl_hos_ero_ertek.setText(str(self.hos.adatok.damage + bonus_dmg))
            self.ui.lbl_hos_vedekezes_ertek.setText(str(self.hos.adatok.defense + bonus_def))
            
            self.ui.lbl_szorny_ero_ertek.setText(str(self.aktualis_harcolt_szorny.adatok.damage))
            self.ui.lbl_szorn_vedekezes_ertek.setText(str(self.aktualis_harcolt_szorny.adatok.defense))
            self.ui.lbl_hos_kezdemenyezes_ertek.setText(f"{self.hos.adatok.initiative:.2f}")
            self.ui.lbl_szorny_kezdemenyezes_ertek.setText(f"{self.aktualis_harcolt_szorny.adatok.initiative:.2f}")
            
            
            #szorny hp bar frissitese
            self.ui.pb_szorny_hp.setMaximum(self.aktualis_harcolt_szorny.adatok.max_hp)
            self.ui.pb_szorny_hp.setValue(self.aktualis_harcolt_szorny.adatok.current_hp)
            #hős hp bar frissitese
            self.ui.pb_hos_hp.setMaximum(self.hos.adatok.max_hp)
            self.ui.pb_hos_hp.setValue(self.hos.adatok.current_hp)
            
            #harci kepernyore valtas
            self.btn_poti.setEnabled(True)
            self.ui.stackedWidget.setCurrentIndex(4)
            print(f"Harc indult a(z) {self.aktualis_harcolt_szorny.adatok.name} ellen!")
            
            
            return

        erintett_ajtok = [item for item in self.hos.collidingItems() if item.data(1)]

        #ha a hos nem all ajton feloldjuk
        if not erintett_ajtok:
            self.szobavaltas_alatt = False

        #ha ralep az ajtora es atmehet
        elif not self.szobavaltas_alatt:
            ajto = erintett_ajtok[0]
            cel_szoba_nev = ajto.data(1)
            cel_x, cel_y = ajto.data(2)
            
            #addig igy van amig le nem megy az ajtorol
            self.szobavaltas_alatt = True 
            
            #szobavaltas vegrehajtasa
            self.aktualis_szoba = self.szobak[cel_szoba_nev]
            self.ui.graphicsView.setScene(self.aktualis_szoba)
            self.aktualis_szoba.addItem(self.hos)
            self.hos.setPos(cel_x, cel_y)
            self.ui.graphicsView.fitInView(self.aktualis_szoba.sceneRect(), Qt.IgnoreAspectRatio)
            
            print(f"Átléptél ide: {cel_szoba_nev}")
            self.mentes()
            self.lenyomott_gombok.clear()
    
    def ajto_engedelyezese(self):
        self.szobavaltas_alatt = False

    def targyra_kattintott(self, lista_elem):
        if lista_elem.data(Qt.UserRole + 2) == "poti":
            print(f"{lista_elem.data(Qt.UserRole + 1)}: a potikat harc közben, a Potik gombbal használhatod.")
            return
        item_id = lista_elem.data(Qt.UserRole)
        nev = lista_elem.data(Qt.UserRole + 1)
        if self.db.felszerel(self.jatekos_id, item_id):
            print(f"Felszerelve: {nev}")
        else:
            print(f"Ez a tárgy nem szerelhető fel: {nev}")
        #a listát csak a jelzés lefutása után építjük újra (az elem, amire kattintottunk, törlődik)
        QTimer.singleShot(0, self.inventory_frissites)

    def harc_inditasa(self):
        gomb_szoveg = self.ui.btn_harcinditas.text()
        
        if gomb_szoveg == "Tovább a térképre":
            self.ui.stackedWidget.setCurrentIndex(2)
            QApplication.processEvents() 
            if hasattr(self, 'aktualis_szoba') and self.aktualis_szoba:
                self.ui.graphicsView.fitInView(self.aktualis_szoba.sceneRect(), Qt.IgnoreAspectRatio)
            self.hos.setFocus()
            self.ui.btn_harcinditas.setText("Harc indítása")
            return

        if gomb_szoveg == "Vége a játéknak":
            
            if gomb_szoveg == "Vége a játéknak":
                self.ui.pb_hos_hp.setValue(self.hos.adatok.current_hp)
                self.ui.btn_harcinditas.setText("Harc indítása")
                self.centralWidget().setStyleSheet("QWidget#centralwidget { border-image: url('assets/alap_bg_blur.png') 0 0 0 0 stretch stretch; }")
                self.ui.stackedWidget.setCurrentIndex(1)
                return
        
        print("A harc elkezdődött!")
        self.ui.btn_harcinditas.setEnabled(False) 
            
        # 1000ms = 1sec ütések között
        self.hos_kore = True
        self.harc_timer.start(1000)

    def auto_harc_kor(self):
        bonus_dmg, bonus_def = self.hos_bonus_statok()
        alap_dmg = self.hos.adatok.damage
        alap_def = self.hos.adatok.defense
        hos_ossz_dmg = alap_dmg + bonus_dmg
        hos_ossz_def = alap_def + bonus_def

        szorny_nev = self.aktualis_harcolt_szorny.adatok.name
        szorny_dmg = self.aktualis_harcolt_szorny.adatok.damage
        szorny_def = self.aktualis_harcolt_szorny.adatok.defense

        if self.hos_kore:
            #gyógyítópoti: életregeneráció, körönként egyszer (a hős körének elején)
            if self.regen_hatralevo_korok > 0:
                gyogyult = self.hos.adatok.heal(self.regen_ertek)
                self.regen_hatralevo_korok -= 1
                self.ui.pb_hos_hp.setValue(self.hos.adatok.current_hp)
                print(f"[REGENERÁCIÓ] +{gyogyult} életerő ({self.regen_hatralevo_korok} kör van hátra)")
            szorzo = random.uniform(0.8, 1.0)
            nyers_sebzes = int(szorzo * hos_ossz_dmg)
            valos_sebzes = max(1, nyers_sebzes - szorny_def)
            self.hos_kore = False

            def _hos_talalat():
                self.sebzes_anim.start(self.ui.lbl_szorn_img, valos_sebzes)
                self.hangok["sword"].play()

                print(
                    f"[HŐS TÁMADÁS] {self.hos.adatok.name}: "
                    f"((Alap erő: {alap_dmg} + Bónusz: {bonus_dmg}) * {szorzo:.2f} = {nyers_sebzes}) "
                    f"- {szorny_nev} védelme ({szorny_def}) => {valos_sebzes} sebzés!"
                )

                # szorny sebzodes
                self.aktualis_harcolt_szorny.adatok.takedamage(valos_sebzes)
                self.ui.pb_szorny_hp.setValue(self.aktualis_harcolt_szorny.adatok.current_hp)

                # gyozelem ellenorzes
                if not self.aktualis_harcolt_szorny.adatok.alive():
                    print(f"A(z) {self.aktualis_harcolt_szorny.adatok.name} halott!")
                    self.hos.adatok.gain_xp(5)
                    self.ui.lbl_hos_nev.setText(f"{self.hos.adatok.name} - {self.hos.adatok.level}. szint")
                    self.karakter_statok_frissitese()
                    self.mentes()
                    self.harc_timer.stop()
                    self.ui.btn_harcinditas.setText("Tovább a térképre")
                    self.ui.btn_harcinditas.setEnabled(True)
            # gyozelem ellenorzes
            if not self.aktualis_harcolt_szorny.adatok.alive():
                print(f"A(z) {self.aktualis_harcolt_szorny.adatok.name} halott!")
                self.poti_hatasok_nullazasa()
                self.btn_poti.setEnabled(False)
                self.hos.adatok.gain_xp(5)
                #zsákmány: a szörny itemeket dobhat, ezek az inventoryba kerülnek
                zsakmany = self.db.szorny_zsakmany(self.jatekos_id, szorny_nev)
                for item, mennyiseg in zsakmany:
                    print(f"Zsákmány: {item.name} x{mennyiseg} ({item.rarity.get_name_hungarian()})")
                if zsakmany:
                    self.inventory_frissites()
                #a szörnyek potikat is dobhatnak (gyógyító 50%, erő 25% – a Szorny_Potion_Drop táblában állítható)
                poti_zsakmany = self.db.szorny_poti_zsakmany(self.jatekos_id, szorny_nev)
                for poti, mennyiseg in poti_zsakmany:
                    print(f"Zsákmány: {poti.name} x{mennyiseg}")
                if poti_zsakmany:
                    self.inventory_frissites()
                self.ui.lbl_hos_nev.setText(f"{self.hos.adatok.name} - {self.hos.adatok.level}. szint")
                self.karakter_statok_frissitese()
                self.mentes()
                self.harc_timer.stop()
                self.ui.btn_harcinditas.setText("Tovább a térképre")
                self.ui.btn_harcinditas.setEnabled(True)

                # halott szorny eltavolitasa a szobabol
                if self.aktualis_harcolt_szorny in self.aktualis_szoba.szornyek:
                    self.aktualis_szoba.szornyek.remove(self.aktualis_harcolt_szorny)
                self.aktualis_szoba.removeItem(self.aktualis_harcolt_szorny)

            self.kard_anim.start(True, _hos_talalat)
        else:
            szorzo = random.uniform(0.8, 1.0)
            nyers_sebzes = int(szorzo * szorny_dmg)
            valos_sebzes = max(0, nyers_sebzes - hos_ossz_def)
            self.hos_kore = True

            def _szorny_talalat():
                self.sebzes_anim.start(self.ui.lbl_hos_img, valos_sebzes)
                self.hangok["sword"].play()

                print(
                    f"[SZÖRNY TÁMADÁS] {szorny_nev}: "
                    f"(Erő: {szorny_dmg} * {szorzo:.2f} = {nyers_sebzes}) "
                    f"- Hős védelme ({alap_def} + {bonus_def} = {hos_ossz_def}) => {valos_sebzes} sebzés!"
                )

                # hos sebzodes
                self.hos.adatok.takedamage(valos_sebzes)
                self.ui.pb_hos_hp.setValue(self.hos.adatok.current_hp)

                # halal ellenorzes
                if not self.hos.adatok.alive():
                    print("Meghaltál, a Szörny megölt.")
                    self.harc_timer.stop()
                    self.ui.btn_harcinditas.setText("Vége a játéknak")
                    self.ui.btn_harcinditas.setEnabled(True)
            # halal ellenorzes
            if not self.hos.adatok.alive():
                print("Meghaltál, a Szörny megölt. A dungeon alaphelyzetbe állt!")
                self.harc_timer.stop()

                #hos healelese es dungeon reset
                self.hos.adatok.heal_to_max()
                self.karakter_statok_frissitese()
                self.dungeon_reset()
                self.mentes()

                self.ui.btn_harcinditas.setText("Vége a játéknak")
                self.ui.btn_harcinditas.setEnabled(True)
                return

            self.kard_anim.start(False, _szorny_talalat)

            self.hos_kore = True

    def dungeon_reset(self):
        if self.hos.scene():
            self.hos.scene().removeItem(self.hos)

        self.szobak = {}
        self.palya_betoltese("palya_1.json")
        self.aktualis_szoba = self.szobak.get("Szoba_1")

        if self.aktualis_szoba:
            self.ui.graphicsView.setScene(self.aktualis_szoba)
            self.aktualis_szoba.addItem(self.hos)
            self.hos.setPos(400, 300)
    
    
    def palya_betoltese(self, json_utvonal):
        #lekerjuk a main.py helyet es osszefuzzuk a json_utvonallal
        projekt_mappa = os.path.dirname(os.path.abspath(__file__))
        teljes_utvonal = os.path.join(projekt_mappa, json_utvonal)
        with open(teljes_utvonal, 'r', encoding='utf-8') as f:
            palya_adatok = json.load(f)
        #vegig iteralunk a szobakon betoltjuk oket
        for szoba_nev, adatok in palya_adatok.items():
            uj_szoba = Szoba(szoba_nev, adatok["hatter"], self.db)
            
            #ajtok generalasa
            for ajto in adatok.get("ajtok", []):
                uj_szoba.ajto_hozzadasa(
                    ajto["x"], ajto["y"], ajto["szelesseg"], ajto["magassag"], 
                    ajto["cel_szoba"], ajto["cel_x"], ajto["cel_y"]
                )
                
            #szornyek generalasa
            for szorny in adatok.get("szornyek", []):
                uj_szoba.szorny_hozzadasa(
                szorny["x"], 
                szorny["y"], 
                szorny.get("nev", "Goblin"), 
                szorny.get("hp", 30), 
                szorny.get("sebzes", 8), 
                szorny.get("vedelem", 2)
        )
                
            #bekerul memoriaba
            self.szobak[szoba_nev] = uj_szoba

    def belepes_soteterdobe(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        
        #layout frissitese
        QApplication.processEvents()
        
        #radobjuk a kepet
        if hasattr(self, 'aktualis_szoba'):
           self.ui.graphicsView.fitInView(self.aktualis_szoba.sceneRect(), Qt.IgnoreAspectRatio)
           print("Beléptél a Kriptába")
        self.hos.setFocus()

        if hasattr(self, 'aktualis_szoba') and self.aktualis_szoba:
            self.aktualis_szoba.kod_frissites(self.hos.x(), self.hos.y(), self.hos.adatok.level)

    def mentes(self):
        #halott hőst nem mentünk, így a "Folytatás" az utolsó élő állapotról indul
        if not hasattr(self, "hos") or not self.hos.adatok.alive():
            return
        self.db.jatekos_mentes(self.jatekos_id, self.hos.adatok)
        self.db.jatekmezo_mentes(self.jatekos_id, self.map_id, self.aktualis_szoba.nev,
                                 self.hos.x(), self.hos.y(), self.hos.adatok.current_hp)

    def targy_leiras(self, sor):
        item = sor.item
        reszek = [f"<b>{item.name}</b>"]
        if item.bonus_attack:
            reszek.append(f"Sebzés: +{item.bonus_attack}")
        if item.bonus_defense:
            reszek.append(f"Védelem: +{item.bonus_defense}")
        reszek.append(f"Ritkaság: {item.rarity.get_name_hungarian()}")
        reszek.append(f"Érték: {item.gold_value} arany")
        if sor.mennyiseg > 1:
            reszek.append(f"Darab: {sor.mennyiseg}")
        return "<br>".join(reszek)

    def inventory_frissites(self):
        #a lista és a felszerelés-gombok újraépítése az adatbázis alapján
        self.ui.listWidget.clear()
        self.kard_anim.felszerelt_kard_kep = None
        for slot in self.slotok:
            gomb = getattr(self.ui, f"btn_{slot}")
            gomb.setIcon(QIcon())
            gomb.setText(self.slot_alap_szoveg[slot])

        for sor in self.db.inventory(self.jatekos_id):
            item = sor.item
            pixmap = QPixmap(os.path.join(self.projekt_mappa, item.image_path))
            if pixmap.isNull():
                print(f"HIBA: Nem található a tárgy képe: {item.image_path}")
            ikon = QIcon(pixmap.scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation))

            if sor.fel_van_szerelve and sor.slot in self.slot_alap_szoveg:
                gomb = getattr(self.ui, f"btn_{sor.slot}")
                gomb.setIcon(ikon)
                gomb.setIconSize(QSize(64, 64))
                gomb.setText("")
                if sor.slot == "kard":
                    self.kard_anim.felszerelt_kard_kep = item.image_path
                continue

            lista_elem = QListWidgetItem()
            lista_elem.setIcon(ikon)
            lista_elem.setToolTip(self.targy_leiras(sor))
            lista_elem.setData(Qt.UserRole, item.item_id)
            lista_elem.setData(Qt.UserRole + 1, item.name)
            self.ui.listWidget.addItem(lista_elem)
            self.karakter_statok_frissitese()
        #potik: a lista végén, darabszámmal (csak amiből van)
        for sor in self.db.potik(self.jatekos_id):
            if sor.mennyiseg <= 0:
                continue
            poti = sor.potion
            pixmap = QPixmap(os.path.join(self.projekt_mappa, poti.image_path))
            if pixmap.isNull():
                print(f"HIBA: Nem található a poti képe: {poti.image_path}")
                pixmap = QPixmap(64, 64)
                pixmap.fill(QColor("#3a3347"))
            pixmap = pixmap.scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            lista_elem = QListWidgetItem()
            lista_elem.setIcon(QIcon(self.ikon_darabszammal(pixmap, sor.mennyiseg)))
            lista_elem.setToolTip(self.poti_leiras(sor))
            lista_elem.setData(Qt.UserRole, poti.param_id)
            lista_elem.setData(Qt.UserRole + 1, poti.name)
            lista_elem.setData(Qt.UserRole + 2, "poti")  #megkülönbözteti a tárgyaktól
            self.ui.listWidget.addItem(lista_elem)

    def ikon_darabszammal(self, pixmap, darab):
        #a kép jobb alsó sarkába "x3" jelvényt rajzol
        kep = pixmap.copy()
        festo = QPainter(kep)
        festo.setRenderHint(QPainter.Antialiasing)
        betu = festo.font()
        betu.setBold(True)
        betu.setPointSize(9)
        festo.setFont(betu)
        szoveg = f"x{darab}"
        szeles = festo.fontMetrics().horizontalAdvance(szoveg) + 8
        magas = festo.fontMetrics().height() + 2
        teglalap = QRect(kep.width() - szeles, kep.height() - magas, szeles, magas)
        festo.setPen(Qt.NoPen)
        festo.setBrush(QColor(0, 0, 0, 190))
        festo.drawRoundedRect(teglalap, 4, 4)
        festo.setPen(QColor("#f5eedc"))
        festo.drawText(teglalap, Qt.AlignCenter, szoveg)
        festo.end()
        return kep

    def poti_leiras(self, sor):
        poti = sor.potion
        if poti.effect_type == EffectType.ATTACK:
            hatas = f"+{poti.value} sebzés a harc végéig"
        else:
            hatas = f"+{poti.value} életerő/kör, {poti.duration} körön át"
        return f"<b>{poti.name}</b><br>{hatas}<br>Darab: {sor.mennyiseg}<br><i>Harc közben, a Potik gombbal használható</i>"

    def levesz(self, slot):
        if self.db.levesz(self.jatekos_id, slot):
            print(f"Levéve: {slot}")
            self.inventory_frissites()

    def closeEvent(self, event):
        self.mentes()
        self.db.close()
        super().closeEvent(event)
    def resizeEvent(self, event):
        #qt elvegzi az atmeretezest a layoutokon
        super().resizeEvent(event)
        
        #ha epp a jatekteren vagyok akkor rateszi a kamerat az ujra
        if self.ui.stackedWidget.currentIndex() == 2 and hasattr(self, 'aktualis_szoba'):
            self.ui.graphicsView.fitInView(self.aktualis_szoba.sceneRect(), Qt.IgnoreAspectRatio)

    def hos_bonus_statok(self):
      bonus_dmg, bonus_def = 0, 0
      for sor in self.db.inventory(self.jatekos_id):
          if sor.fel_van_szerelve:
              bonus_dmg += sor.item.bonus_attack
              bonus_def += sor.item.bonus_defense
      bonus_dmg += self.poti_bonusz_dmg  #erőpoti (a harc végéig)
      return bonus_dmg, bonus_def

    def karakter_statok_frissitese(self):
        if not hasattr(self, "hos"):
            return
        alap_dmg, alap_def, alap_init = self.hos.adatok.damage, self.hos.adatok.defense, self.hos.adatok.initiative
        bonus_dmg, bonus_def = self.hos_bonus_statok()  
        self.ui.label_12.setText(str(alap_dmg))
        self.ui.label_16.setText(str(alap_def))
        self.ui.label_82.setText(f"{alap_init:.2f}")
        self.ui.label_83.setText(f"+{bonus_dmg}")
        self.ui.label_85.setText(f"+{bonus_def}")
        self.ui.label_87.setText("+0.00")
        self.ui.label_89.setText(str(alap_dmg + bonus_dmg))
        self.ui.label_92.setText(str(alap_def + bonus_def))
        self.ui.label_93.setText(f"{alap_init:.2f}")

    def login_gomb_nyomas(self):
        nev = self.ui.le_login_nev.text().strip()
        jelszo = self.ui.le_login_jelszo.text()

        if not nev or not jelszo:
            self.glass_popup("Hiba", "Add meg a felhasználónevet és a jelszót!")
            return

        siker, uzenet, user = self.userdb.bejelentkezes(nev, jelszo)
        if siker and user:
            self.aktualis_felhasznalo = user
            self.allas_betoltese(user.name)
            self.ui.le_login_nev.clear()
            self.ui.le_login_jelszo.clear()
            self.glass_popup("Siker", uzenet)
            self.ui.stackedWidget.setCurrentIndex(0)
        else:
            self.glass_popup("Hiba", uzenet)

    def reg_gomb_nyomas(self):
        nev = self.ui.le_reg_nev.text().strip()
        jelszo = self.ui.le_reg_jelszo.text()
        jelszo2 = self.ui.le_reg_jelszo2.text()

        if not nev or not jelszo:
            self.glass_popup("Hiba", "Minden mező kitöltése kötelező!")
            return
        if jelszo != jelszo2:
            self.glass_popup("Hiba", "A két jelszó nem egyezik!")
            return

        siker, uzenet, uj_user = self.userdb.regisztracio(nev, jelszo)
        if siker:
            self.glass_popup("Siker", uzenet)
            self.ui.le_reg_nev.clear()
            self.ui.le_reg_jelszo.clear()
            self.ui.le_reg_jelszo2.clear()
        else:
            self.glass_popup("Hiba", uzenet)
    def glass_popup(self, cim, szoveg):
        from PySide6.QtWidgets import QDialog, QVBoxLayout, QFrame, QLabel, QPushButton

        dialog = QDialog(self)
        dialog.setObjectName("glass_popup")
        dialog.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        dialog.setAttribute(Qt.WA_TranslucentBackground)
        dialog.setMinimumWidth(340)

        kulso = QVBoxLayout(dialog)
        kulso.setContentsMargins(0, 0, 0, 0)

        keret = QFrame()
        keret.setObjectName("glass_popup_keret")
        belso = QVBoxLayout(keret)
        belso.setSpacing(14)

        lbl_cim = QLabel(cim)
        lbl_cim.setObjectName("popup_cim")
        lbl_cim.setAlignment(Qt.AlignCenter)

        lbl_szoveg = QLabel(szoveg)
        lbl_szoveg.setObjectName("popup_szoveg")
        lbl_szoveg.setAlignment(Qt.AlignCenter)
        lbl_szoveg.setWordWrap(True)

        gomb = QPushButton("Rendben")
        gomb.clicked.connect(dialog.accept)

        belso.addWidget(lbl_cim)
        belso.addWidget(lbl_szoveg)
        belso.addWidget(gomb, alignment=Qt.AlignCenter)
        kulso.addWidget(keret)

        dialog.exec()

    def felhasznalo_kijelentkezes(self):
        self.aktualis_felhasznalo = None
        self.ui.frame_3.hide()
        self.ui.textBrowser.hide()
        self.ui.stackedWidget.setCurrentIndex(7)
        
    
    def mentes_oldal_megnyitasa(self):
        if hasattr(self.ui, 'lbl_mentes_info'):
            szoba_nev = self.aktualis_szoba.nev if hasattr(self, 'aktualis_szoba') and self.aktualis_szoba else "Ismeretlen"
            self.ui.lbl_mentes_info.setText(
                f"Hős: {self.hos.adatok.name} ({self.hos.adatok.level}. szint)\n"
                f"Életerő: {self.hos.adatok.current_hp} / {self.hos.adatok.max_hp}\n"
                f"Jelenlegi szoba: {szoba_nev}"
            )
        self.ui.stackedWidget.setCurrentIndex(5)

    def page6_mentes_gomb(self):
        if not self.aktualis_felhasznalo:
            self.glass_popup("Hiba", "Nincs bejelentkezett felhasználó!")
            return
        self.mentes()
        self.mentes_oldal_megnyitasa()
        self.glass_popup("Mentés", f"{self.aktualis_felhasznalo.name} játékállása sikeresen elmentve!")

    def page6_betoltes_gomb(self):
        if not self.aktualis_felhasznalo:
            self.glass_popup("Hiba", "Nincs bejelentkezett felhasználó!")
            return
        self.allas_betoltese(self.aktualis_felhasznalo.name)
        self.glass_popup("Betöltés", f"{self.aktualis_felhasznalo.name} utolsó mentése betöltve!")

        # Belépés a játékba (oldalsáv és napló megjelenítése, váltás a térképre)
        self.ui.frame_3.show()
        self.ui.textBrowser.show()
        self.ui.stackedWidget.setCurrentIndex(1)
    
    def allas_betoltese(self, felhasznalo_nev):
        self.jatekos_id, hos_statok = self.db.jatekos_betoltes_vagy_letrehozas(felhasznalo_nev)
        mentes = self.db.jatekmezo_betoltes(self.jatekos_id)

        if hasattr(self, 'hos') and self.hos.scene():
            self.hos.scene().removeItem(self.hos)

        self.szobak = {}
        self.palya_betoltese("palya_1.json")

        kezdo_szoba = "Szoba_1"
        hos_x, hos_y = 400, 300
        if mentes and mentes.get("aktualis_szoba") in self.szobak:
            kezdo_szoba = mentes["aktualis_szoba"]
            if mentes.get("hos_x") is not None and mentes.get("hos_y") is not None:
                hos_x, hos_y = float(mentes["hos_x"]), float(mentes["hos_y"])

        self.aktualis_szoba = self.szobak.get(kezdo_szoba)
        if self.aktualis_szoba:
            self.ui.graphicsView.setScene(self.aktualis_szoba)
            self.hos = GraphicalHero("assets/hero.png", hos_x, hos_y, hos_statok)
            self.hos.setZValue(20)
            self.aktualis_szoba.addItem(self.hos)

        self.inventory_frissites()
        self.karakter_statok_frissitese()
        self.ui.pb_hos_hp.setMaximum(self.hos.adatok.max_hp)
        self.ui.pb_hos_hp.setValue(self.hos.adatok.current_hp)
        if hasattr(self, 'aktualis_szoba') and self.aktualis_szoba:
            self.aktualis_szoba.kod_frissites(self.hos.x(), self.hos.y(), self.hos.adatok.level)

#---------------------------JÁTÉKABLAK VÉGE-------------------------		
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    projekt_mappa = os.path.dirname(os.path.abspath(__file__))
    qss_utvonal = os.path.join(projekt_mappa, "style.qss")
    if os.path.exists(qss_utvonal):
        with open(qss_utvonal, "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())
    else:
        print(f"HIBA: Nem találom a style.qss fájlt itt: {qss_utvonal}")

    
    ablak = JatekAblak()
    ablak.show()
    sys.exit(app.exec())
