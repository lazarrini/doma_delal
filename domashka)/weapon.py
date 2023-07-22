from exception import *
class Weapon:
    def __init__(self, name, w_damage):
        self.name = name
        self.w_damage = w_damage
        if self.w_damage > 12:
            raise SoMuchDamage("Указан слишком большой урон")

    def __str__(self):
        return f"{self.name} (Урон: {self.w_damage})"

    def __eq__(self, other):
        if isinstance(other, Weapon):
            return self.name == other.name and self.w_damage == other.w_damage
        return False


class Excalibur:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        Excalibur.__instance = None

    def __init__(self, name="excalibur", w_damage=12):
        self.name = name
        self.w_damage = w_damage

    def __str__(self):
        return f"{self.name} - величайший легендарный меч"
