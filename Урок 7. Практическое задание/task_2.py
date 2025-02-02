"""
Задание 2.

Реализовать проект расчета суммарного расхода ткани на производство одежды.

Единственный класс этого проекта — одежда (класс Clothes).

К типам одежды в этом проекте относятся пальто и костюм.

У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: v и h, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (v/6.5 + 0.5),
для костюма (2*h + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать
абстрактный класс для единственного класса проекта,
проверить на практике работу декоратора @property

Пример:
Расход ткани на пальто = 1.27
Расход ткани на костюм = 20.30
Общий расход ткани = 21.57

Два класса: абстрактный и Clothes
"""
class Clothes: #класс одежда + параметры размер и рост
    def __init__(self, v, h): #

        self.v = v
        self.h = h



    def palto(self):  # для пальто
        return self.v / 6.5 + 0.5


    def kostu(self):  # для костюма
        return 2 * self.h + 0.3

palto_inp = Clothes(48, 170)
kostu_inp = Clothes(48, 170)

pot = palto_inp.palto()
kot = kostu_inp.kostu()
all_clothes = pot + kot

print(f"На пальто расход: {pot}")
print(f"На костюм расход: {kot}")
print(f"Всего расход: {all_clothes}")

"""
Часть 2
from abc import ABC, abstractmethod



class Clothess(ABC):# абстрактный класс для одежды
    def __init__(self, v, h):
        self.v = v
        self.h = h

    @abstractmethod# Абстрактный метод расчета расхода ткани
    def summ_c_s(self):
        pass


class Clothes(Clothess):# Создаем класс , который наследуется от Clothess
    def coat_calc(self):# метод расчета расхода для пальто
        return self.v / 6.5 + 0.5

    def suit_calc(self):# метод расчета расхода для костюма
        return 2 * self.h + 0.3

    def summ_c_s(self):# абстрактный метод из абстрактного класса Clothing
        return self.coat_calc() + self.suit_calc()


# объекты класса Clothes параметрами
coat = Clothes(50, 160)
suit = Clothes(48, 185)


coat_calc = coat.coat_calc()# Рассчитываем расход пальто
suit_calc = suit.suit_calc()# Рассчитываем расход костюм
total_summ = suit.summ_c_s()# Рассчитываем расход общий


print("Расход ткани на пальто:", coat_calc)
print("Расход ткани на костюм:", suit_calc)
print("Общий расход ткани:", total_summ)
"""