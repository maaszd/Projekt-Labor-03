import os
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGraphicsPixmapItem
from PySide6.QtGui import QPixmap

class Hero:

    def __init__(self, name: str, current_hp: int = 10, max_hp: int = 10, damage: int = 1, defense: int = 1, gold: int = 0, level: int = 1, xp: int = 0, initiative: float = 0.4):
        self._name = name
        self._current_hp = current_hp
        self._max_hp = max_hp
        self._damage = damage
        self._defense = defense
        self._gold = gold
        self._level = level
        self._xp = xp
        self._initiative = initiative

    #getter setterek

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def current_hp(self):
        return self._current_hp

    #nem lehet negatív és nagyobb mint max hp
    @current_hp.setter
    def current_hp(self, value: int):
        self._current_hp = max(0, min(self._max_hp, value))

    @property
    def max_hp(self):
        return self._max_hp

    #nem lehet kisebb mint 1 és nagyobb mint max hp
    @max_hp.setter
    def max_hp(self, value: int):
        self._max_hp = max(1, value)
        if self._current_hp > self._max_hp:
            self._current_hp = self._max_hp

    @property
    def damage(self):
        return self._damage

    #nem lehet negatív
    @damage.setter
    def damage(self, value: int):
        self._damage = max(0, value)

    @property
    def defense(self):
        return self._defense

    #nem lehet negatív
    @defense.setter
    def defense(self, value: int):
        self._defense = max(0, value)

    @property
    def gold(self):
        return self._gold

    #nem lehet negatív
    @gold.setter
    def gold(self, value: int):
        self._gold = max(0, value)

    @property
    def level(self):
        return self._level

    #nem lehet kisebb mint 1
    @level.setter
    def level(self, value: int):
        self._level = max(1, value)

    @property
    def xp(self):
        return self._xp

    #nem lehet negatív
    @xp.setter
    def xp(self, value: int):
        self._xp = max(0, value)

    @property
    def initiative(self):
        return self._initiative

    @initiative.setter
    def initiative(self, value: float):
        self._initiative = value

    #----többi cucc


    def takedamage(self, amount):
        if amount >= 0:
            self._current_hp = max(0,self._current_hp - amount)

    def alive(self):
        return self._current_hp > 0

    def heal(self, amount: int):
        if not self.alive() or amount <= 0:
            return 0
        prev_hp = self._current_hp
        self._current_hp = min(self._max_hp, self._current_hp + amount)
        return self._current_hp - prev_hp #tényleges gyógyítás

    def heal_to_max(self):
        if self.alive():
            self._current_hp = self._max_hp

    def gain_xp(self, amount: int = 1):
        if amount <= 0:
            return
        self._xp += amount
        if self._xp >= 10:
            self.levelup()

    def levelup(self):
        self._level += 1
        self._damage += 1
        self._defense += 1
        self._max_hp += 10
        self.heal_to_max()
        self._initiative = self._initiative * 1.1
        self._xp = 0

#csak a kép miatt kell
class Hos(QGraphicsPixmapItem):
    def __init__(self, kep_utvonal, x, y, hero_adatok):
        super().__init__()
        
        self.adatok = hero_adatok
        
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
