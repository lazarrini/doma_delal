import random
from unit import *
from weapon import *
from exception import *

if __name__ == "__main__":
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
    #stas.attack(vlad)

    roma.battle_cry()

    #roma.attack(stas, axe)
    stas.attack(roma)
    stas.rest()

    while len(Unit.units_in_battle) > 1:
        attacker = random.choice(Unit.units_in_battle)
        opponent = random.choice(Unit.units_in_battle)

        if attacker != opponent:
            counter = 0
            action = random.randint(1, 6)
            if action == 1 and attacker.hp != attacker.max_hp:
                attacker.rest()
            else:

                attacker.attack(opponent)

                counter += 1
                if counter % 3 == 0:
                    attacker.battle_cry()

            if opponent.hp <= 0:
                Unit.units_in_battle.remove(opponent)
                Unit.units_in_grave.append(opponent)
                del opponent

    print(f"\nВОТ И ПОБЕДИТЕЛЬ ЖЕСТОЧАЙШЕЙ БИТВЫ!:")
    for units in Unit.units_in_battle:
        print(f"{units.name}!!! Оставшееся здоровье:{units.hp}!")
    for units_died in Unit.units_in_grave:
        print(f"\n{units_died.name} погиб.")
