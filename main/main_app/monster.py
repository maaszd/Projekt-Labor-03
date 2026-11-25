import os
import random
import math
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
        
        if pixmap.isNull() and "boss" in kep_utvonal.lower():
            tartalek_utvonal = os.path.normpath(os.path.join(projekt_mappa, "assets/monster.png"))
            pixmap = QPixmap(tartalek_utvonal)
        
        if pixmap.isNull():
            print(f"HIBA: Nem található a szörny képe: {teljes_utvonal}")
        else:
            #sima szorny: 80x80, Boss: 130x130 a terkepen
            meret = 130 if self.adatok.is_boss else 80
            self.setPixmap(pixmap.scaled(meret, meret, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            #kozepre helyezes a terkepen
            eltolas = (meret - 50) // 2
            x = max(0, x - eltolas)
            y = max(0, y - eltolas)
            
        self.setPos(x, y)
        #azonositas
        self.setData(3, "szorny")

        #veletlenszeru jarorozes egy fix koron belul
        self.spawn_x = x
        self.spawn_y = y
        self.zona_sugar = 75
        self.sebesseg = 1.2
        self.varakozas = random.randint(0, 30)  # Ne egyszerre induljanak el
        self.cel_x = x
        self.cel_y = y

    def _uj_celpont(self):
        # veletlenszeru pont a zona sugaran belul
        szog = random.uniform(0, 2 * math.pi)
        tav = self.zona_sugar * math.sqrt(random.uniform(0, 1))
        uj_x = self.spawn_x + math.cos(szog) * tav
        uj_y = self.spawn_y + math.sin(szog) * tav

        #szoba hatarain belul tartas
        self.cel_x = max(20, min(700, uj_x))
        self.cel_y = max(20, min(500, uj_y))

    def jarorozes(self):
        if self.adatok.is_boss:
            return

        if self.varakozas > 0:
            self.varakozas -= 1
            return

        dx = self.cel_x - self.x()
        dy = self.cel_y - self.y()
        tav = math.hypot(dx, dy)

        if tav <= self.sebesseg:
            self.setPos(self.cel_x, self.cel_y)
            self._uj_celpont()
            self.varakozas = random.randint(30, 90)  # ~0.5 - 1.5 mp szunet
        else:
            self.setPos(
                self.x() + (dx / tav) * self.sebesseg,
                self.y() + (dy / tav) * self.sebesseg
            )