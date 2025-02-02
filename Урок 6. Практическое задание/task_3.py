"""
Задание 3.

Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).

П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку __str__
__str__(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""
class Worker:# Создаем класс

    def __init__(self, name, surname, position, income):
        # атрибуты объекта
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income #защищенный атрибут
class Position(Worker):# Создаем класс на базе Worker
    def get_full_name(self): #метод для получения полного имени
        return f"{self.surname}, {self.name}"
    def get_total_income(self):#метод для получения дохода
        return self._income["wage"] + self._income["bonus"]
worker = Position("Том", "Марволо", "Юрист", {"wage":45000, "bonus": 5000})
print(worker.get_full_name())
print(worker.get_total_income())
