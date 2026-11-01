import os
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGraphicsPixmapItem
from PySide6.QtGui import QPixmap

class Monster:

    def __init__(self, name: str, current_hp: int = 10, max_hp: int = 10, damage: int = 1, defense: int = 1, initiative: float = 0.4, id_szam: int = 0, is_boss: bool = False, title_reward: str = None):
        self._name = name
        self._current_hp = current_hp
        self._max_hp = max_hp
        self._damage = damage
        self._defense = defense
        self._initiative = initiative
        self._id = id_szam
        self._is_boss = is_boss
        self._title_reward = title_reward


    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def current_hp(self):
        return self._current_hp

    #nem lehet negatív és nem lépheti túl a max hp-t
    @current_hp.setter
    def current_hp(self, value: int):
        self._current_hp = max(0, min(self._max_hp, value))

    @property
    def max_hp(self):
        return self._max_hp

    #nem lehet kisebb mint 1
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
    def initiative(self):
        return self._initiative

    @initiative.setter
    def initiative(self, value: float):
        self._initiative = value

    @property
    def is_boss(self):
        return self._is_boss

    @is_boss.setter
    def is_boss(self, value: bool):
        self._is_boss = value

    @property
    def title_reward(self):
        return self._title_reward

    @title_reward.setter
    def title_reward(self, value: str):
        self._title_reward = value

    # metodusok

    def alive(self):
        return self._current_hp > 0

    def takedamage(self, amount: int):
        if amount >= 0:
            self._current_hp = max(0, self._current_hp - amount)

class GraphicalMonster(QGraphicsPixmapItem):
    def __init__(self, kep_utvonal, x, y, monster_adatok):
        super().__init__()
        
        self.adatok = monster_adatok
        
        projekt_mappa = os.path.dirname(os.path.abspath(__file__))
        teljes_utvonal = os.path.normpath(os.path.join(projekt_mappa, kep_utvonal))
        pixmap = QPixmap(teljes_utvonal)
        
        if pixmap.isNull():
            print(f"HIBA: Nem található a szörny képe: {teljes_utvonal}")
        else:
            self.setPixmap(pixmap.scaled(50, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            
        self.setPos(x, y)
        #azonositas
        self.setData(3, "szorny")