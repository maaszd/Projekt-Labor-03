import os
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGraphicsScene, QGraphicsPixmapItem, QGraphicsRectItem
from PySide6.QtGui import QPixmap, QBrush, QPen
from monster import Monster, GraphicalMonster
class Szoba(QGraphicsScene):
    def __init__(self, nev, hatter_kep_utvonal, db=None):
        super().__init__(0, 0, 800, 600)
        self.nev = nev
        self.db = db #adatbazis (szornyek betoltesehez)
        
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
        ajto.setBrush(Qt.NoBrush)
        ajto.setPen(Qt.NoPen)
        
        #setdataval elteszunk plusz infokat az ajtoba
        ajto.setData(1, cel_szoba_nev) # 1 - hova visz?
        ajto.setData(2, (cel_x, cel_y)) # 2- milyen x,y-ra dobja a host
        
        self.ajtok.append(ajto)
        self.addItem(ajto)

    def szorny_hozzadasa(self, x, y, szorny_id=1):
        #letrehozzuk a szornyet
        if self.db is not None:
            szorny_statok = self.db.szorny_betoltes(szorny_id)
        else:
            szorny_statok = Monster(name="Goblin", current_hp=30, max_hp=30, damage=8, defense=2)
        
        szorny = GraphicalMonster("assets/monster.png", x, y, szorny_statok)
        
        self.szornyek.append(szorny)
        self.addItem(szorny)