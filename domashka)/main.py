import random
from unit import *
from weapon import *


stas = Knight("Stas")
vlad = Ranger("Vlad")
roma = Barbarian("Roma")

axe = Weapon("axe", 6)
big_sword = Weapon("big_sword", 8)

excalibur = Excalibur()

print(stas)
print(big_sword)
print(excalibur)
Elf.characteristic()

stas.battle_cry()
stas.attack(vlad)

roma.battle_cry()
roma.attack(stas, axe)
stas.attack(roma)
stas.rest()
