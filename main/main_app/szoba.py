import os
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGraphicsScene, QGraphicsPixmapItem, QGraphicsRectItem
from PySide6.QtGui import QPixmap, QBrush, QPen, QColor
from monster import Monster, GraphicalMonster
class Szoba(QGraphicsScene):
    def __init__(self, nev, hatter_kep_utvonal, db=None):
        super().__init__(0, 0, 800, 600)
        self.nev = nev
        self.db = db #adatbazis (szornyek betoltesehez)
        
        projekt_mappa = os.path.dirname(os.path.abspath(__file__))
        teljes_kep_utvonal = os.path.normpath(os.path.join(projekt_mappa, hatter_kep_utvonal))
        pixmap = QPixmap(teljes_kep_utvonal).scaled(800, 600, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        #hatterkep betoltese
        if pixmap.isNull():
            print(f"HIBA: A Qt nem találja a képet ezen az útvonalon: {teljes_kep_utvonal}")
            self.setBackgroundBrush(QBrush(Qt.darkGray)) #sotetszurke lesz
        else:
            skalazott_hatter = pixmap.scaled(800, 600, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
            self.hatter = QGraphicsPixmapItem(skalazott_hatter)
            self.hatter.setZValue(0)
            self.addItem(self.hatter)

        self.ajtok = []
        self.vizualis_ajtok = []
        self.szornyek = []
        self.akadalyok = []

    def szorny_hozzadasa(self, x, y, nev="Goblin", hp=30, damage=8, defense=2):
        is_boss = "BOSS" in nev.upper()
        szorny_statok = Monster(name=nev, current_hp=hp, max_hp=hp, damage=damage, defense=defense, is_boss=is_boss)
        
        #szorny kep valasztasa a nev alapjan
        szorny_kepek = {
            "Goblin": "assets/goblin.png",
            "Zombi": "assets/zombi.png",
            "Csontváz Harcos": "assets/csontvaz.png",
            "Pók": "assets/pok.png",
            "Árnyék": "assets/arnyek.png",
            "BOSS: Demonic Overlord": "assets/boss.png"
        }
        
        kep = szorny_kepek.get(nev, "assets/boss.png" if is_boss else "assets/monster.png")
        
        szorny = GraphicalMonster(kep, x, y, szorny_statok)
        szorny.setData(3, "szorny")
        szorny.setZValue(10)
        
        self.szornyek.append(szorny)
        self.addItem(szorny)

    def ajto_hozzadasa(self, x, y, szelesseg, magassag, cel_szoba_nev, cel_x, cel_y):
        #trigger lathatatlan
        trigger = QGraphicsRectItem(x, y, szelesseg, magassag)
        trigger.setBrush(Qt.NoBrush)
        atlatszo_pen = QPen(Qt.transparent)
        atlatszo_pen.setWidth(0)
        trigger.setPen(atlatszo_pen)
        
        trigger.setData(1, cel_szoba_nev)
        trigger.setData(2, (cel_x, cel_y))
        
        self.ajtok.append(trigger)
        self.addItem(trigger)

        #vizualis ajto
        projekt_mappa = os.path.dirname(os.path.abspath(__file__))
        kep_utvonal = os.path.join(projekt_mappa, "assets", "ajto.png")
        ajto_eredeti = QPixmap(kep_utvonal)
        
        if not ajto_eredeti.isNull():
            #fix meretezes
            ajto_kep = ajto_eredeti.scaled(80, 100, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
            vizualis_ajto = QGraphicsPixmapItem(ajto_kep)
            vizualis_ajto.setZValue(15)
            
            #az ajto forgatasa
            vizualis_ajto.setTransformOriginPoint(40, 50)
            
            
            if y == 0:  
                #felso
                vizualis_ajto.setPos(x + (szelesseg / 2) - 40, 0)
                vizualis_ajto.setRotation(0) 
                
            elif y > 400:  
                #also
                vizualis_ajto.setPos(x + (szelesseg / 2) - 40, y + magassag - 100)
                vizualis_ajto.setRotation(180) 
                
            elif x == 0:  
                #bal
                vizualis_ajto.setPos(10, y + (magassag / 2) - 50)
                vizualis_ajto.setRotation(-90)
                
            elif x > 600:  
                #jobb
                vizualis_ajto.setPos(800 - 90, y + (magassag / 2) - 50)
                vizualis_ajto.setRotation(90) 

            self.addItem(vizualis_ajto)
            
            
            if not hasattr(self, 'vizualis_ajtok'):
                self.vizualis_ajtok = []
            self.vizualis_ajtok.append(vizualis_ajto)
        else:
            print(f"HIBA: Nem találom az ajtó képet: {kep_utvonal}")