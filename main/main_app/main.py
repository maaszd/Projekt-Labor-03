from random import randrange
import random
import sys
import os
import json
from PySide6.QtCore import Qt, QSize, QObject, Signal, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QAbstractItemView, QListView, QGraphicsScene, QGraphicsPixmapItem, QGraphicsRectItem, QGraphicsItem
from PySide6.QtGui import QIcon, QPixmap, QBrush, QColor, QPen
from ui_menu import Ui_MainWindow 


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
class Hos(QGraphicsPixmapItem):
    def __init__(self, kep_utvonal, x, y):
        super().__init__()
        
        projekt_mappa = os.path.dirname(os.path.abspath(__file__))
        teljes_utvonal = os.path.normpath(os.path.join(projekt_mappa, kep_utvonal))
        pixmap = QPixmap(teljes_utvonal)
        
        if pixmap.isNull():
            print("HIBA: Nem található a hős képe!")
        else:
            #fix 50x50 meretu
            self.setPixmap(pixmap.scaled(50, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            
        self.setPos(x, y)
        self.sebesseg = 15 #mennyit tud lepni egy gombnyomasra
          
class Szoba(QGraphicsScene):
    def __init__(self, nev, hatter_kep_utvonal):
        super().__init__(0, 0, 800, 600)
        self.nev = nev
        
        projekt_mappa = os.path.dirname(os.path.abspath(__file__))
        teljes_kep_utvonal = os.path.normpath(os.path.join(projekt_mappa, hatter_kep_utvonal))
        pixmap = QPixmap(teljes_kep_utvonal)
        #hatterkep betoltese
        if pixmap.isNull():
            print(f"HIBA: A Qt nem találja a képet ezen az útvonalon: {teljes_kep_utvonal}")
            self.setBackgroundBrush(QBrush(Qt.darkGray)) #sotetszurke lesz
        else:
            self.hatter = QGraphicsPixmapItem(pixmap)
            self.addItem(self.hatter)

        self.ajtok = []
        self.szornyek = []
        self.akadalyok = []

    def ajto_hozzadasa(self, x, y, szelesseg, magassag, cel_szoba_nev, cel_x, cel_y):
        ajto = QGraphicsRectItem(x, y, szelesseg, magassag)
        ajto.setBrush(QBrush(Qt.blue)) #egyelore zöld
        
        #setdataval elteszunk plusz infokat az ajtoba
        ajto.setData(1, cel_szoba_nev) # 1 - hova visz?
        ajto.setData(2, (cel_x, cel_y)) # 2- milyen x,y-ra dobja a host
        
        self.ajtok.append(ajto)
        self.addItem(ajto)

    def szorny_hozzadasa(self, x, y):
        szorny = QGraphicsRectItem(0, 0, 50, 50)
        szorny.setBrush(QBrush(Qt.red))
        szorny.setPos(x, y)
        self.szornyek.append(szorny)
        self.addItem(szorny)

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

        #TÉRKÉP
        self.szobak = {}
        self.palya_betoltese("palya_1.json")
        self.aktualis_szoba = self.szobak["Kezdo"]
        self.ui.graphicsView.setScene(self.aktualis_szoba)
        self.ui.graphicsView.fitInView(self.aktualis_szoba.sceneRect(), Qt.IgnoreAspectRatio)
        self.hos = Hos("assets/hero.png", 400, 300) 
        self.aktualis_szoba.addItem(self.hos)
        
        
        #inventory beallitasai   
        self.ui.listWidget.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.ui.listWidget.setIconSize(QSize(64, 64))
        self.ui.listWidget.setViewMode(QListWidget.IconMode)
        self.ui.listWidget.setResizeMode(QListWidget.Adjust)
        self.ui.listWidget.setMovement(QListView.Static)
        self.ui.listWidget.setSpacing(10) 
        self.ui.listWidget.setGridSize(QSize(80, 80))
        
        projekt_mappa = os.path.dirname(os.path.abspath(__file__))

	    #teszt tárgyakkal
         
        self.ui.listWidget.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.ui.listWidget.setIconSize(QSize(64, 64))
        self.projekt_mappa = os.path.dirname(os.path.abspath(__file__))
        self.assets_mappa = os.path.join(self.projekt_mappa, "assets")
        
        teszt_targyak = [
            {"nev": "Kard", "info": "Sebzés: +5\nRitkaság: Gyakori", "kep": "sword.png"},
            {"nev": "Mellvért", "info": "Védelem: +10\nRitkaság: Gyakori", "kep": "chestplate.png"},
            {"nev": "Sisak", "info": "Védelem: +15\n", "kep": "helmet.png"},
            {"nev": "Pajzs", "info": "Védelem: +15\n","kep": "shield.png"},
            {"nev": "Kesztyű", "info": "Ügyesség: +3\nVédelem: +2", "kep": "gloves.png"},
            {"nev": "Csizma", "info": "Sebesség: +2\nVédelem: +1", "kep": "boots.png"},
        ]

        for targy in teszt_targyak:
            item = QListWidgetItem() 
            item.setToolTip(f"<b>{targy['nev']}</b><br>{targy['info']}")
            item.setData(Qt.UserRole, targy["nev"])
            
            teljes_utvonal = os.path.join(self.assets_mappa, targy["kep"])
            pixmap = QPixmap(teljes_utvonal)
            if pixmap.isNull():
              print(f"HIBA: Még mindig null ez a kép: {teljes_utvonal}")
            
            #képek átméretezése fix 64x64-re
            atmeretezett_kep = pixmap.scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation)
  
            item.setIcon(QIcon(atmeretezett_kep))
            
            #icon betöltése assets/ mappából
            self.ui.listWidget.addItem(item)
        
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
        self.szobavaltas_alatt = False
		
#----------------------__init__(self): VÉGE ---------------------------------
    
    def frissit_text_browser(self, szoveg):
        self.ui.textBrowser.append(szoveg)
			
    def jatek_folytatasa(self):
        self.ui.frame_3.show()
        self.ui.textBrowser.show()
        self.ui.stackedWidget.setCurrentIndex(1)
        print("Üdv újra a játékban!")

    def vissza_a_fomenube(self):    
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
       
        #megortenik a lepes
        self.hos.setPos(x, y)

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
            self.lenyomott_gombok.clear()
    
    def ajto_engedelyezese(self):
        self.szobavaltas_alatt = False

    def targyra_kattintott(self, item):
        targy_neve = item.data(Qt.UserRole)
        print(f"Duplán kattintottál erre a tárgyra: {targy_neve}")
        #TODO: equip logika normálisan

        #teszt equip frontend szinten
        if "kard" in targy_neve.lower():
        
            self.ui.btn_kard.setIcon(item.icon())
            self.ui.btn_kard.setIconSize(QSize(64, 64))
            self.ui.btn_kard.setText("")
        
            row = self.ui.listWidget.row(item)
            self.ui.listWidget.takeItem(row)
            print(f"Felszerelve: {targy_neve}")

    def harc_inditasa(self):
        if self.ui.btn_harcinditas.text() == "Tovább a térképre":
            self.ui.stackedWidget.setCurrentIndex(1)
            self.ui.btn_harcinditas.setText("Harc indítása")
            
            #szörny letörlése a térképről
            self.terkep_cellak[(self.szorny_x, self.szorny_y)].setStyleSheet("background-color: black;")
            #semmissé tesszük a szörny koordinátáit, TODO: elegánsabb megoldás?
            self.szorny_x, self.szorny_y = -1, -1
            return
        print("A harc elkezdődött!")
        self.ui.btn_harcinditas.setEnabled(False) 
            
        #1000ms = 1sec ütések között
        self.hos_kore = True
        self.harc_timer.start(1000)

    def auto_harc_kor(self):
        if self.hos_kore:
            #TESZT: hős támadás
            sebzes = 15
            valos_sebzes = int(random.uniform(0.8,1) * sebzes)
            print(f"A hős lecsapott: {valos_sebzes} sebzés!")
            
            #szörny hp bar frissitése
            jelenlegi_szorny_hp = self.ui.pb_szorny_hp.value()
            uj_hp = max(0, jelenlegi_szorny_hp - valos_sebzes)
            self.ui.pb_szorny_hp.setValue(uj_hp)
            
            if uj_hp <= 0:
                print("A szörny halott!")
                self.harc_timer.stop()
                self.ui.btn_harcinditas.setText("Tovább a térképre")
                self.ui.btn_harcinditas.setEnabled(True)
                return
            
            self.hos_kore = False
        else:
            #TESZT: szörny támad
            szorny_sebzes = 8
            valos_sebzes = int(random.uniform(0.8,1) * szorny_sebzes)
            print(f"A szörny visszatámadt: {valos_sebzes} sebzés!")
            
            jelenlegi_hos_hp = self.ui.pb_hos_hp.value()
            uj_hos_hp = max(0, jelenlegi_hos_hp - valos_sebzes)
            self.ui.pb_hos_hp.setValue(uj_hos_hp)

            # Vereség ellenőrzése
            if uj_hos_hp <= 0:
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
            uj_szoba = Szoba(szoba_nev, adatok["hatter"])
            
            #ajtok generalasa
            for ajto in adatok.get("ajtok", []):
                uj_szoba.ajto_hozzadasa(
                    ajto["x"], ajto["y"], ajto["szelesseg"], ajto["magassag"], 
                    ajto["cel_szoba"], ajto["cel_x"], ajto["cel_y"]
                )
                
            #szornyek generalasa
            for szorny in adatok.get("szornyek", []):
                uj_szoba.szorny_hozzadasa(szorny["x"], szorny["y"])
                
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
