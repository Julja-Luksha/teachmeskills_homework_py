# 1. Создайте класс Soda (для определения типа газированной воды), принимающий
# 1 аргумент при инициализации (отвечающий за добавку к выбираемому
# лимонаду). В этом классе реализуйте метод show_my_drink(), выводящий на
# печать «Газировка и {ДОБАВКА}» в случае наличия добавки, а иначе
# отобразится следующая фраза: «Обычная газировка».
class Soda:
    def __init__(self, additive=None):
        self.additive = additive

    def show_my_drink(self):
        if self.additive:
            print(f"Газировка {self.additive}")
        else:
            print("Обычная газировка")


s1 = Soda(input("Введите название добавки к газировке "))
s1.show_my_drink()


# 2. Требуется проверить, возможно ли из представленных отрезков условной длины
# сформировать треугольник. Для этого необходимо создать класс
# TriangleChecker, принимающий только положительные числа. С помощью
# метода is_triangle() возвращаются следующие значения (в зависимости от ситуации)
class TriangleChecker:
    def __init__(self, side1: int, side2: int, side3: int) -> None:
        self.sides = [side1, side2, side3]

    def is_triangle(self) -> str:
        try:
            checked_sides = [int(s) for s in self.sides]
        except TypeError:
            return "Нужно вводить только числа!"

        for s in checked_sides:
            if s <= 0:
                return "С отрицательными числами ничего не выйдет!"

        a, b, c = sorted(checked_sides)
        if a + b > c:
            return "Ура, можно построить треугольник!"
        else:
            return "Жаль, но из этого треугольник не сделать."


c1 = TriangleChecker(2, 6, 7)
print(c1.is_triangle())


# 3. Необходимо создать класс KgToPounds, в который принимает количество
# килограмм, а с помощью метода to_pounds() они переводятся в фунты.
# Необходимо закрыть доступ к переменной kg.
# Также, реализовать методы: - set_kg() - для задания нового значения килограммов (записывать только
# числовые значения),  - get_kg() - для вывода текущего значения кг.
# Во второй версии необходимо использовать декоратор property для создания
# setter и getter взамен set_kg и get_kg.
# 1
class KgToPounds:
    def __init__(self, kg: float) -> None:
        self.__kg = kg

    def to_pounds(self) -> float:
        return self.__kg * 2.205

    def set_kg(self, value: float) -> None:
        if isinstance(value, (int, float)):
            self.__kg = value
        else:
            raise TypeError("Нужно вводить только числовые значения!")

    def get_kg(self) -> float:
        return self.__kg


c1 = KgToPounds(10)
print(c1.to_pounds())
c1.set_kg(5)
print(c1.get_kg())
print(c1.to_pounds())


# # 2
class KgToPounds:
    def __init__(self, kg: float) -> None:
        self.__kg = kg

    def to_pounds(self) -> float:
        return self.__kg * 2.205

    @property
    def kg(self) -> float:
        return self.__kg

    @kg.setter
    def kg(self, value: float) -> None:
        if isinstance(value, (int, float)):
            self.__kg = value
        else:
            raise TypeError("Нужно вводить только числовые значения!")


c1 = KgToPounds(10)
print(c1.to_pounds())
c1.kg = 7
print(c1.kg)
print(c1.to_pounds())


# 4. Строки в Питоне сравниваются на основании значений символов. Т.е. если мы
# захотим выяснить, что больше: Apple или Яблоко, – то Яблоко окажется
# бОльшим. А все потому, что английская буква A имеет значение 65 (берется из
# таблицы кодировки), а русская буква Я – 1071. Надо создать новый класс
# RealString, который будет принимать строку и сравнивать по количеству
# входящих в них символов. Сравнивать между собой можно как объекты класса,
# так и обычные строки с экземплярами класса RealString.
class RealString:
    def __init__(self, string) -> None:
        self.string = string

    def __len__(self) -> int:
        return len(self.string)

    def _get_len(self, other) -> int:
        if isinstance(other, RealString):
            return len(other)
        elif isinstance(other, str):
            return len(other)
        else:
            return NotImplemented

    def __lt__(self, other) -> bool:
        other_len = self._get_len(other)
        return len(self) < other_len

    def __le__(self, other) -> bool:
        other_len = self._get_len(other)
        return len(self) <= other_len

    def __gt__(self, other) -> bool:
        other_len = self._get_len(other)
        return len(self) > other_len

    def __ge__(self, other) -> bool:
        other_len = self._get_len(other)
        return len(self) >= other_len

    def __eq__(self, other) -> bool:
        other_len = self._get_len(other)
        return len(self) == other_len

    def __ne__(self, other) -> bool:
        other_len = self._get_len(other)
        return len(self) != other_len


a = RealString("Apple")
b = RealString("Апельсин")
print(a > b)


# 5. Напишите класс Rectangle, который имеет атрибуты: width (ширина) и
# height (высота). Класс должен иметь следующие методы:
# • Конструктор, который принимает два параметра: width и height, и
# инициализирует соответствующие атрибуты.
# • Метод str, который возвращает строковое представление объекта класса
# Rectangle в формате “Прямоугольник с шириной width и высотой
# height”.
# • Метод get_area, который возвращает площадь прямоугольника.
# • Метод get_perimeter, который возвращает периметр прямоугольника.
# • Метод is_square, который возвращает True, если прямоугольник является
# квадратом, и False в противном случае. Этот метод должен быть
# декорирован как property.
class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def __str__(self):
        return f"Прямоугольник с шириной {self.width} и высотой {self.height}"

    def get_area(self) -> int:
        return self.width * self.height

    def get_perimeter(self) -> int:
        return self.width * 2 + self.height * 2

    @property
    def is_square(self) -> bool:
        print("Является ли прямоугольник квадратом?")
        return self.width == self.height


a = Rectangle(2, 4)
print(a.is_square)


# 6. Напишите класс Person, который имеет атрибуты name (имя), age (возраст)
# и gender (пол). Класс должен иметь следующие методы:
# • Конструктор, который принимает три параметра: name, age и gender, и
# инициализирует соответствующие атрибуты.
# • Метод str, который возвращает строковое представление объекта класса
# Person в формате “Имя: name, Возраст: age, Пол: gender”.
# • Метод get_name, который возвращает значение атрибута name.
# • Метод set_name, который принимает один параметр: new_name, и
# устанавливает значение атрибута name равным new_name. Этот метод
# должен быть декорирован как property.
# • Метод is_adult, который возвращает True, если возраст объекта больше
# или равен 18, и False в противном случае. Этот метод должен быть
# декорирован как staticmethod.
# • Метод create_from_string, который принимает один параметр: s, и
# создает и возвращает объект класса Person на основе строки s. Строка s
# должна иметь формат “name-age-gender”, где name - имя, age - возраст и
# gender - пол. Этот метод должен быть декорирован как classmethod.
class Person:
    def __init__(self, name, age, gender) -> None:
        self._name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Пол: {self.gender}"

    def get_name(self) -> str:
        return self.name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @staticmethod
    def is_adult(age) -> bool:
        return age >= 18

    @classmethod
    def create_from_string(cls, s):
        name, age, gender = s.split("-")
        return cls(name, int(age), gender)


p1 = Person("Юлия", 25, "Ж")
print(p1.name)
p1.name = "Ольга"
print(p1.name)
print(Person.is_adult(17))
p2 = Person.create_from_string("Кирилл-31-М")
print(p2)
