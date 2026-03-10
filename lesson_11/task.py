import time

class auto:
    def __init__(self, brand, age, mark, weight=None, color=None):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.weight = weight
        self.color = color

    def move(self):
        print("move")

    def stop(self):
        print("stop")

    def birthday(self):
        self.age += 1

car = auto("Subaru", 3, "WRX")
print(car.age, car.brand, car.mark)

class truck(auto):
    def __init__(self, brand, age, mark, max_load, weight=None, color=None):
        super().__init__(brand, age, mark, weight, color)
        self.max_load = max_load

    def move(self):
        print("attention")
        super().move()

    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)

class car(auto):
    def __init__(self, brand, age, mark, max_speed, weight=None, color=None):
        super().__init__(brand, age, mark, weight, color)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f"max_speed is: {self.max_speed}")


t1 = truck("Volvo", 5, "654", 20000)
t2 = truck("MAN", 4, "AG", 18000, color="white")

t1.move()
t2.load()
print (t2.max_load, f"Цвет: {t2.color}")

c1 = car("Mazda", 22, "RX8", 220, 1350)
c1.move()
c1.stop()
c2 = car("Subaru", 3, "WRX", 260, color="orange")

c1.move()
print(c1.weight)
c2.move()
print(c2.max_speed)

