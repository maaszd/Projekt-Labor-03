from random import randrange
import random
import sys
import os
from PySide6.QtCore import Qt, QSize, QObject, Signal, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QAbstractItemView
from PySide6.QtGui import QIcon, QPixmap
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
        self.ui.btn_dungeon_soteterdo.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))

        # térkép

        self.terkep_cellak = {}
        
        self.ui.gridLayout.setSpacing(0)
        self.ui.gridLayout.setContentsMargins(0, 0, 0, 0)
        for row in range(self.ui.gridLayout.rowCount()):
            for col in range(self.ui.gridLayout.columnCount()):
                item = self.ui.gridLayout.itemAtPosition(row, col)
                if item is not None:
                    cella_widget = item.widget()
                    
                    # eltároljuk a x-y értékeket 
                    self.terkep_cellak[(col, row)] = cella_widget
                    
                    # Teszt: köd, minden fekete
                    cella_widget.setStyleSheet("background-color: black;")

        
        self.hos_x = 4
        self.hos_y = 3
        
        #TESZT szörny encounter / piros a mező
        self.szorny_x = 6
        self.szorny_y = 4
        self.terkep_cellak[(self.szorny_x, self.szorny_y)].setStyleSheet("background-color: red;")
        
        #Ha minden stimmel, akkor a hős cellája zöld körülötte pedig köd(fekete egyenlőre)
        self.terkep_cellak[(self.hos_x, self.hos_y)].setStyleSheet("background-color: green;")


        self.ui.listWidget.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.ui.listWidget.setIconSize(QSize(64, 64))
        projekt_mappa = os.path.dirname(os.path.abspath(__file__))

	#teszt tárgyakkal
         
        self.ui.listWidget.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.ui.listWidget.setIconSize(QSize(64, 64))
        projekt_mappa = os.path.dirname(os.path.abspath(__file__))

        teszt_targyak = [
            {"nev": "Kard", "info": "Sebzés: +5\nRitkaság: Gyakori", "kep": "sword.png"},
            {"nev": "Mellvért", "info": "Védelem: +10\nRitkaság: Gyakori", "kep": "chestplate.png"},
            {"nev": "Sisak", "info": "Védelem: +15\nBlokkolás: 10%", "kep": "helmet.png"},
            {"nev": "Pajzs", "info": "Védelem: +15\nBlokkolás: 10%", "kep": "shield.png"},
            {"nev": "Nadrág", "info": "Védelem: +8\nMozgás: -1", "kep": "leggings.png"},
            {"nev": "Kesztyű", "info": "Ügyesség: +3\nVédelem: +2", "kep": "gloves.png"},
            {"nev": "Csizma", "info": "Sebesség: +2\nVédelem: +1", "kep": "boots.png"},
        ]

        for targy in teszt_targyak:
            item = QListWidgetItem() 
            item.setToolTip(f"<b>{targy['nev']}</b><br>{targy['info']}")
            item.setData(Qt.UserRole, targy["nev"])
            
            teljes_utvonal = os.path.join(assets_mappa, targy["kep"])
            pixmap = QPixmap(teljes_utvonal)
            if pixmap.isNull():
                print(f"HIBA: Még mindig null ez a kép: {teljes_utvonal}")
            
            #képek átméretezése fix 64x64-re
            atmeretezett_kep = pixmap.scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation)
  
            item.setIcon(QIcon(atmeretezett_kep))
            #icon betöltése assets/ mappából
            
            self.ui.listWidget.addItem(item)
        
		self.ui.listWidget.itemDoubleClicked.connect(self.targyra_kattintott)
		
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
        #csak a dungeonbe mozoghatunk
        if self.ui.stackedWidget.currentIndex() != 2: 
            return
    
        #zöld szín visszaváltoztatása miatt kell
        uj_x, uj_y = self.hos_x, self.hos_y
        if event.key() == Qt.Key_W:
             uj_y -= 1
        elif event.key() == Qt.Key_S:
            uj_y += 1
        elif event.key() == Qt.Key_A:
            uj_x -= 1
        elif event.key() == Qt.Key_D:
             uj_x += 1
        
        #TESZT: szörny encounter
        if uj_x == self.szorny_x and uj_y == self.szorny_y:
            print("Egy szörnyet találtál, a csata elkezdődik!")
            
            #hős képe betöltése
            hos_kep_utvonal =  os.path.join(assets_mappa,"hero.png")
            hos_pixmap = QPixmap(hos_kep_utvonal)
            self.ui.lbl_hos_img.setPixmap(hos_pixmap)
            self.ui.lbl_hos_img.setScaledContents(True)
            
            #szörny képe betöltése
            szorny_kep_utvonal = os.path.join(assets_mappa,"monster.png")
            szorny_pixmap = QPixmap(szorny_kep_utvonal)
            self.ui.lbl_szorn_img.setPixmap(szorny_pixmap)
            self.ui.lbl_szorn_img.setScaledContents(True)

            #3. harci gui, váltunk rá
            self.ui.stackedWidget.setCurrentIndex(4) 
            #TODO: statok betöltése itt?
            return
        
        max_x = self.ui.gridLayout.columnCount()
        max_y = self.ui.gridLayout.rowCount()
    
        #hős cella színezése, zöld <-> fekete
        if 0 <= uj_x < max_x and 0 <= uj_y < max_y:
            self.terkep_cellak[(self.hos_x, self.hos_y)].setStyleSheet("background-color: black;")
            self.hos_x, self.hos_y = uj_x, uj_y
            self.terkep_cellak[(self.hos_x, self.hos_y)].setStyleSheet("background-color: green;")
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

#---------------------------JÁTÉKABLAK VÉGE-------------------------		
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ablak = JatekAblak()
    ablak.show()
    sys.exit(app.exec())
