from enum import Enum
class EffectType(Enum):
  HEALTH = 1  # 1 = életerő
  DEFENSE = 2  # 2 = védekezés
  ATTACK = 3  # 3 = támadási erő
  INITIATIVE = 4  # 4 = kezdeményezés

  def get_name_hungarian(self):
    names = {
        1: "életerő",
        2: "védekezés",
        3: "támadási erő",
        4: "kezdeményezés",
    }
    return names.get(self.value, "ismeretlen")

class Potion:

  def __init__(
      self,
      param_id: int,
      name: str,
      image_path: str,
      effect_type: EffectType,
      value: int,
  ):
    self._param_id = param_id  # Egyedi azonosító az adatbázisból
    self._name = name  # A poti neve
    self._image_path = image_path  # A kép útvonala
    self._effect_type = effect_type  # A hatás típusa (Enum)
    self._value = value  # A növelés mértéke

  @property
  def param_id(self) -> int:
    return self._param_id

  @property
  def name(self) -> str:
    return self._name

  @property
  def image_path(self) -> str:
    return self._image_path

  @property
  def effect_type(self) -> EffectType:
    return self._effect_type

  @property
  def value(self) -> int:
    return self._value

  @value.setter
  def value(self, new_value: int):
    self._value = new_value

  def __repr__(self):
    type_name = self.effect_type.get_name_hungarian()
    return (
        f"<Potion [{self.name}] -> Típus: {type_name}"
        f" ({self.effect_type.value}), Érték: +{self.value}, Kép:"
        f" {self.image_path}>"
    )
