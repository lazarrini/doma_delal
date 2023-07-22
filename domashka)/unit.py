import random
from exception import *
class Unit:

    units_in_battle = []
    armor = 12
    max_hp = 8
    max_stamina = 6
    units_in_grave = []


    def __init__(self, name):
        self.name = name
        self.hp = self.max_hp
        self.stamina = self.max_stamina
        self.units_in_battle.append(self)



    def __add__(self, other):
        if isinstance(other, int):
            self.hp += other


    def __sub__(self, other):
        if isinstance(other, int):
            self.hp -= other

    def attack(self, target, weapon=None):
        if target not in Unit.units_in_battle:
            raise UnitNameError("Персонаж с таким именем не найден")


        if self.stamina == 0:
            self.rest()
        dam_1k4 = random.randint(1, 4)
        if self.hp <= 0:
            print(f"\n{self.name} повержен и не может больше сражаться")


        elif self.stamina <= 0:
            print(f"\nУ {self.name} больше нет сил. Нужен отдых.")

        else:
            self.stamina -= 1

            print(f"\n{self.name} атакует {target.name} \nуспех решит бросок кубика...")

            dice_res = random.randint(1, 20)
            if weapon:
                self.atck_dam = random.randint(1, weapon.w_damage)
            else:
                self.atck_dam = dam_1k4

            if dice_res == 1:

                print(
                    f"Результат: {dice_res}. Критический промах... {self.name} подскальзывается, падает на землю и получает {dam_1k4} урона!")
                self.take_damage(self.atck_dam)

            elif dice_res >= self.armor and dice_res != 20:
                print(
                    f"Результат: {dice_res}! Броня пробита!! Можно посчитать урон! {self.name} наносит {self.atck_dam} урона!")
                target.take_damage(self.atck_dam)

            elif dice_res == 20:
                print(
                    f"На кубике {dice_res}!!! {self.name} совершает критическую атаку и наносит {2 * self.atck_dam} урона!")
                target.take_damage(2 * self.atck_dam)

            else:
                print(f"Результат на кубике: {dice_res}! Броня соперника не пробита...")

    def take_damage(self, damage):
        self - damage
        print(f"\n{self.name} получает {damage} урона!")
        if self.hp <= 0:
            self.hp = 0
            print(f"{self.name} погиб...")

        else:
            print(f"У него остаётся всего {self.hp} жизней!")

    def rest(self):
        if self.hp <= 0:
            print(f"{self.name} уже не оправится...")
        else:
            stam_buff = random.randint(2, 4)
            hp_buff = random.randint(1, 6)
            self.stamina += stam_buff
            self + hp_buff
            if self.hp > self.max_hp:
                self.hp = self.max_hp

            if self.stamina > self.max_stamina:
                self.stamina = self.max_stamina



            print(f"\n{self.name} отступил, чтобы восстановить силы:\n"
                  f"{stam_buff} запаса сил восстановлено! {hp_buff} hp восстановлено!\n"
                  f"Текущие здоровье: {self.hp}/{self.max_hp}; Запас сил: {self.stamina}/{self.max_stamina}")

    def __del__(self):
        pass



    def __str__(self):
        if self == self.units_in_battle:
            for unit in self.units_in_battle:
                return f"{unit.name}"
        else:
            return f"Максимальное значение здоровья: {self.max_hp};\nМаксимальное значение запаса сил {self.max_stamina};\nКласс брони: {self.armor}"


class Human:

    def battle_cry(self):
        self.phrases = ["Я готов к любой опасности!", "За альянс)", "Я стану величайшим героем!"]
        rand_phrse = random.randint(0, len(self.phrases) - 1)
        print(self.phrases[rand_phrse])

    @staticmethod
    def charateristic():
        print(f"Люди создают могучие империи, основанные на завоеваниях и торговле.\nЧто бы ни двигало ими, люди всегда были инноваторами и пионерами во всех мирах.")


class Orc:
    def battle_cry(self):
        self.phrases = ["Все кости переломаю!!!", "За орду)", "Я сотру в порошок своих врагов!"]
        rand_phrse = random.randint(0, len(self.phrases) - 1)
        print(self.phrases[rand_phrse])

    @staticmethod
    def charateristic():
        print(f"Орки — дикие грабители и налетчики; у них сутулая осанка,\nнизкий лоб и свиноподобные лица с выступающими нижними клыками, напоминающими бивни.")


class Elf:
    def battle_cry(self):
        self.phrases = ["Я заслужу уважение своего наставника!", "Я навострил свои уши!", "Ты не скроешься!!!"]
        rand_phrse = random.randint(0, len(self.phrases) - 1)
        print(self.phrases[rand_phrse])

    @staticmethod
    def characteristic():
        print(f"Эльфам нравится оттачивать своё воинское мастерство, \nили добиваться великой волшебной мощи, и приключения способствуют этому.")


class Knight(Unit, Human):
    race = "human"
    def __init__(self, name):
        super().__init__(name)
        self.armor += 2

    def __str__(self):

        return f"{super().__str__()}\n{self.name} будучи рыцарем, мастерски владеет оружием, самым прочный доспехом, и приёмами ведения боя."



class Barbarian(Unit, Orc):
    rase = "orc"
    def __init__(self, name):
        super().__init__(name)
        self.max_hp += 2

    def __str__(self):
        return f"{super().__str__()}\nЯрость варвара {self.name}, как свирепость загнанного в угол хищника, а его огромное тело, здоровее любого зверя."



class Ranger(Unit, Elf):
    race = "elf"
    def __init__(self, name):
        self.max_stamina += 2
        super().__init__(name)

    def __str__(self):
        return f"{super().__str__()}\nCреди плотно стоящих деревьев, оличающийся высокой выносливостью следопыт {self.name} несёт свой бесконечный дозор."

