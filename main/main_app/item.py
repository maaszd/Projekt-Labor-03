from enum import Enum


class ItemRarity(Enum):

  COMMON = 1  # Gyakori
  UNCOMMON = 2  # Nem gyakori
  RARE = 3  # Ritka
  EPIC = 4  # Epikus
  LEGENDARY = 5  # Legendás

  def get_name_hungarian(self):
    names = {
        1: "Common (Gyakori)",
        2: "Uncommon (Nem gyakori)",
        3: "Rare (Ritka)",
        4: "Epic (Epikus)",
        5: "Legendary (Legendás)",
    }
    return names.get(self.value, "Ismeretlen")


class ItemType(Enum):

  ARMOR = 1  # Páncél
  WEAPON = 2  # Fegyver
  ITEM = 3  # Egyéb tárgy (pl. tekercs, ital stb.)

  def get_name_hungarian(self):
    names = {1: "Páncél", 2: "Fegyver", 3: "Tárgy/Tekercs"}
    return names.get(self.value, "Ismeretlen")


class Item:

  def __init__(
      self,
      item_id: int,  # item_id: Egyedi azonosító az adatbázisból
      name: str,  # name: A tárgy neve (pl. "Sárkányölő kard")[cite: 1]
      item_type: ItemType,  # item_type: A tárgy típusa[cite: 1]
      rarity: ItemRarity,  # rarity: A ritkasági szintje[cite: 1]
      bonus_attack: int,  # bonus_attack: Bónusz támadási érték[cite: 1]
      bonus_defense: int,  # bonus_defense: Bónusz védekezési érték[cite: 1]
      gold_value: int,  # gold_value: Mennyit ér aranyban[cite: 1]
      image_path: str,  # image_path: A tárgyhoz tartozó kép fájlútvonala[cite: 1]
  ):
    # ITT VÁLTOZÁS: aláhúzás került a nevek elé (privát változók)
    self._item_id = item_id
    self._name = name
    self._item_type = item_type
    self._rarity = rarity
    self._bonus_attack = bonus_attack
    self._bonus_defense = bonus_defense
    self._gold_value = gold_value
    self._image_path = image_path

  @property
  def item_id(self) -> int:
    return self._item_id

  @property
  def name(self) -> str:
    return self._name

  @property
  def item_type(self) -> ItemType:
    return self._item_type

  @property
  def rarity(self) -> ItemRarity:
    return self._rarity

  @property
  def image_path(self) -> str:
    return self._image_path

  @property
  def bonus_attack(self) -> int:
    return self._bonus_attack

  @bonus_attack.setter
  def bonus_attack(self, value: int):
    self._bonus_attack = value

  @property
  def bonus_defense(self) -> int:
    return self._bonus_defense

  @bonus_defense.setter
  def bonus_defense(self, value: int):
    self._bonus_defense = value

  @property
  def gold_value(self) -> int:
    return self._gold_value

  @gold_value.setter
  def gold_value(self, value: int):
    self._gold_value = value
