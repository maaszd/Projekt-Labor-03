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
#---------------------------JÁTÉKABLAK VÉGE-------------------------		
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ablak = JatekAblak()
    ablak.show()
    sys.exit(app.exec())