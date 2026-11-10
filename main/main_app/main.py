from random import randrange
import random
import sys
import os
import json
from szoba import Szoba
from hero import Hero, GraphicalHero
from monster import Monster, GraphicalMonster
from PySide6.QtCore import Qt, QSize, QObject, Signal, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QAbstractItemView, QListView, QGraphicsScene, QGraphicsPixmapItem, QGraphicsRectItem, QGraphicsItem
from PySide6.QtGui import QIcon, QPixmap, QBrush, QColor, QPen

from ui_menu import Ui_MainWindow
from db import Adatbazis


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
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # --- FŐMENÜ BEÁLLÍTÁSA INDULÁSKOR ---
        self.ui.stackedWidget.setCurrentIndex(0)
        #bal oszlop gombok meg a text doboz elrejtése 
        self.ui.frame_3.hide()       
        self.ui.textBrowser.hide()
        
        #fomenu gomb fuggvenyei
        self.ui.btn_folytatas.clicked.connect(self.jatek_folytatasa)
        self.ui.btn_kilepes.clicked.connect(self.close)
        self.ui.btn_kilepes_2.clicked.connect(self.vissza_a_fomenube)
        
        #text dobozba terminál szöveg kiiras
        self.console_redirector = ConsoleRedirector()
        self.console_redirector.output_written.connect(self.frissit_text_browser)
        sys.stdout = self.console_redirector
        
        # Gombok összekötése stacked widgetnek az indexei alapján: 0 - főmenü, 1 - térkép, 2 - sötét erdő, 3 - karakter + hátizsák, 
        #                                                          4 - harc,
        
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
        self.palya_betoltese(map_adat["palya_fajl"])

        kezdo_szoba = "Kezdo"
        hos_x, hos_y = 400, 300
        if mentes and mentes["aktualis_szoba"] in self.szobak:
            kezdo_szoba = mentes["aktualis_szoba"]
            hos_x, hos_y = mentes["hos_x"], mentes["hos_y"]

        self.aktualis_szoba = self.szobak.get(kezdo_szoba)
        if self.aktualis_szoba:
            self.ui.graphicsView.setScene(self.aktualis_szoba)
            self.ui.graphicsView.fitInView(self.aktualis_szoba.sceneRect(), Qt.IgnoreAspectRatio)
            self.hos = GraphicalHero("assets/hero.png", hos_x, hos_y, hos_statok)
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


        self.lenyomott_gombok = set() 
        
        #fps(60 FPS = 1000ms / 60 =~ 16ms)
        self.mozgas_timer = QTimer(self)
        self.mozgas_timer.timeout.connect(self.folyamatos_mozgas)
        self.mozgas_timer.start(16)
        self.szobavaltas_alatt = True  #amíg le nem lép az ajtóról, nincs szobaváltás
		
#----------------------__init__(self): VÉGE ---------------------------------
    
    def frissit_text_browser(self, szoveg):
        self.ui.textBrowser.append(szoveg)
			
    def jatek_folytatasa(self):
        self.ui.frame_3.show()
        self.ui.textBrowser.show()
        self.ui.stackedWidget.setCurrentIndex(1)
        print("Üdv újra a játékban!")

    def vissza_a_fomenube(self):    
        self.mentes()
        self.ui.frame_3.hide()       
        self.ui.textBrowser.hide()   
        self.ui.stackedWidget.setCurrentIndex(0) 
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

        #ha a hos ralepett egy szornyre akkor harc kezdodik
        erintett_szornyek = [item for item in self.hos.collidingItems() if item.data(3) == "szorny"]

        if erintett_szornyek:
            
            self.aktualis_harcolt_szorny = erintett_szornyek[0]
            self.lenyomott_gombok.clear()
            
            #hos kepet es nevet frissitjuk a harci menuben
            self.ui.lbl_hos_img.setPixmap(self.hos.pixmap().scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.ui.lbl_hos_nev.setText(self.hos.adatok.name)
            
            #szorny kepet es nevet frissitjuk a harci menuben
            self.ui.lbl_szorn_img.setPixmap(self.aktualis_harcolt_szorny.pixmap().scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.ui.lbl_szorny_nev.setText(self.aktualis_harcolt_szorny.adatok.name)
            
            #hos es szorny statok frissitese a harci menuben
            self.ui.lbl_hos_ero_ertek.setText(str(self.hos.adatok.damage))
            self.ui.lbl_hos_vedekezes_ertek.setText(str(self.hos.adatok.defense))
            self.ui.lbl_szorny_ero_ertek.setText(str(self.aktualis_harcolt_szorny.adatok.damage))
            self.ui.lbl_szorn_vedekezes_ertek.setText(str(self.aktualis_harcolt_szorny.adatok.defense))
            self.ui.lbl_hos_kezdemenyezes_ertek.setText(str(self.hos.adatok.initiative))
            self.ui.lbl_szorny_kezdemenyezes_ertek.setText(str(self.aktualis_harcolt_szorny.adatok.initiative))
            
            
            #szorny hp bar frissitese
            self.ui.pb_szorny_hp.setMaximum(self.aktualis_harcolt_szorny.adatok.max_hp)
            self.ui.pb_szorny_hp.setValue(self.aktualis_harcolt_szorny.adatok.current_hp)
            #hős hp bar frissitese
            self.ui.pb_hos_hp.setMaximum(self.hos.adatok.max_hp)
            self.ui.pb_hos_hp.setValue(self.hos.adatok.current_hp)
            
            #harci kepernyore valtas
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
        item_id = lista_elem.data(Qt.UserRole)
        nev = lista_elem.data(Qt.UserRole + 1)
        if self.db.felszerel(self.jatekos_id, item_id):
            print(f"Felszerelve: {nev}")
        else:
            print(f"Ez a tárgy nem szerelhető fel: {nev}")
        #a listát csak a jelzés lefutása után építjük újra (az elem, amire kattintottunk, törlődik)
        QTimer.singleShot(0, self.inventory_frissites)

    def harc_inditasa(self):
        if self.ui.btn_harcinditas.text() == "Tovább a térképre":
            self.ui.stackedWidget.setCurrentIndex(2)
            QApplication.processEvents() 
            if hasattr(self, 'aktualis_szoba') and self.aktualis_szoba:
                self.ui.graphicsView.fitInView(self.aktualis_szoba.sceneRect(), Qt.IgnoreAspectRatio)
            self.hos.setFocus()
            self.ui.btn_harcinditas.setText("Harc indítása")
            
            return
        print("A harc elkezdődött!")
        self.ui.btn_harcinditas.setEnabled(False) 
            
        #1000ms = 1sec ütések között
        self.hos_kore = True
        self.harc_timer.start(1000)

    def auto_harc_kor(self):
        if self.hos_kore:
            #hős tamadasa valos adatokkal
            sebzes = self.hos.adatok.damage
            valos_sebzes = int(random.uniform(0.8, 1.0) * sebzes)
            print(f"{self.hos.adatok.name} lecsapott: {valos_sebzes} sebzés!")
            
            #szorny sebzodes
            self.aktualis_harcolt_szorny.adatok.takedamage(valos_sebzes)
            self.ui.pb_szorny_hp.setValue(self.aktualis_harcolt_szorny.adatok.current_hp)
            
            #gyozelem ellenorzes
            if not self.aktualis_harcolt_szorny.adatok.alive():
                print(f"A {self.aktualis_harcolt_szorny.adatok.name} halott!")
                self.hos.adatok.gain_xp(5)
                self.mentes()
                self.harc_timer.stop()
                self.ui.btn_harcinditas.setText("Tovább a térképre")
                self.ui.btn_harcinditas.setEnabled(True)
                
                #hallott szorny eltavolitasa a szobabol
                if self.aktualis_harcolt_szorny in self.aktualis_szoba.szornyek:
                    self.aktualis_szoba.szornyek.remove(self.aktualis_harcolt_szorny)
                self.aktualis_szoba.removeItem(self.aktualis_harcolt_szorny)
                return
            
            self.hos_kore = False
        else:
            #szorny tamadasa valos adatokkal
            szorny_sebzes = self.aktualis_harcolt_szorny.adatok.damage
            #szorny sebzes
            valos_sebzes = max(0, int(random.uniform(0.8, 1.0) * szorny_sebzes) - self.hos.adatok.defense)
            print(f"A szörny visszatámadt: {valos_sebzes} sebzés!")
            
            #hos sebzodes
            self.hos.adatok.takedamage(valos_sebzes)
            self.ui.pb_hos_hp.setValue(self.hos.adatok.current_hp)

            #halál ellenőrzés
            if not self.hos.adatok.alive():
                print("Meghaltál, a Szörny megölt.")
                self.harc_timer.stop()
                self.ui.btn_harcinditas.setText("Vége a játéknak")
                self.ui.btn_harcinditas.setEnabled(True)
                return
            
            self.hos_kore = True

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
                uj_szoba.szorny_hozzadasa(szorny["x"], szorny["y"], szorny.get("szorny_id", 1))
                
            #bekerul memoriaba
            self.szobak[szoba_nev] = uj_szoba

    def belepes_soteterdobe(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        
        #layout frissitese
        QApplication.processEvents()
        
        #radobjuk a kepet
        if hasattr(self, 'aktualis_szoba'):
           self.ui.graphicsView.fitInView(self.aktualis_szoba.sceneRect(), Qt.IgnoreAspectRatio)
           print("Beléptél a Sötét erdőbe")
        self.hos.setFocus()
    
    # ADATBÁZIS

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
                continue

            lista_elem = QListWidgetItem()
            lista_elem.setIcon(ikon)
            lista_elem.setToolTip(self.targy_leiras(sor))
            lista_elem.setData(Qt.UserRole, item.item_id)
            lista_elem.setData(Qt.UserRole + 1, item.name)
            self.ui.listWidget.addItem(lista_elem)

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

#---------------------------JÁTÉKABLAK VÉGE-------------------------		
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ablak = JatekAblak()
    ablak.show()
    sys.exit(app.exec())
