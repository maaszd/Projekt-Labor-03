import os
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGraphicsScene, QGraphicsPixmapItem, QGraphicsRectItem
from PySide6.QtGui import QPixmap, QBrush

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