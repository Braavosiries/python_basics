"""
Задание 5.

Реализовать класс Stationery (канцелярская принадлежность).

Определить в нем публичный атрибут title (название) и публичный метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”

Создать три дочерних класса: Pen (ручка), Pencil (карандаш), Handle (маркер).

В каждом из классов реализовать переопределение метода draw.

Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""
class Stationery:# Создаем класс

    def __init__(self, title):
        # атрибуты объекта
        self.title = title #публичный атрибут

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery): # дочерний класс
    def draw(self):
        print("Рисуем ручкой")
class Pencil(Stationery):  # дочерний класс
    def draw(self):
        print("Рисуем карандашем")
class Handle(Stationery):  # дочерний класс
    def draw(self):
        print("Рисуем маркером")


# объект класса и вызов метода
pen_1 = Pen("")
pen_1.draw()
Pencil_1 = Pencil("")
Pencil_1.draw()
Handle_1 = Handle("")
Handle_1.draw()