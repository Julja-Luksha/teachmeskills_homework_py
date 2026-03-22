# Задание 1. Класс «Игровой персонаж»
# Создай класс GameCharacter, который описывает персонажа игры.
# Требования:
# 1. У персонажа есть имя, здоровье и уровень.
# 2. Здоровье хранится в приватном атрибуте.
# 3. Сделай property для здоровья, чтобы при попытке установить здоровье выше 100 оно
# автоматически становилось 100.
# 4. Сделай защищённый метод _level_up(), который увеличивает уровень на 1.
# 5. Добавь метод attack(other_character), который уменьшает здоровье другого
# персонажа на 10.
# 6. Сделай classmethod, который создаёт персонажа с максимальным здоровьем (100) и
# уровнем 1.
# 7. Сделай staticmethod, который сравнивает двух персонажей по уровню и возвращает
# того, у кого уровень выше.

class GameCharacter:
    def __init__(self, name: str, health: int, level: int) -> None:
        self.name = name
        self._health = 0
        self.health = health
        self.level = level

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        self._health = min(value, 100)

    def _level_up(self) -> None:
        self.level += 1

    def attack(self, other: GameCharacter) -> None:
        other.health = other.health - 10

    @classmethod
    def default_game_character(cls, name: str) -> GameCharacter:
        return cls(name, 100, 1)

    @staticmethod
    def sr(c1, c2) -> GameCharacter:
        return c1 if c1.level > c2.level else c2


hero = GameCharacter("Hero1", 120, 5)
hero.health = 150
print(hero.health)
hero.health = -20
print(hero.health)
hero._level_up()
print(hero.level)
enemy = GameCharacter("Hero2", 50, 2)
hero.attack(enemy)
print(enemy.health)
default_hero = GameCharacter.default_game_character("Hero3")
print(default_hero.health, default_hero.name, default_hero.level)
winner = GameCharacter.sr(hero, enemy)
print(winner.name)


# Задание 2. Класс «Магазин»
# Создай класс Store, описывающий магазин.
# Требования:
# 1. Атрибуты:
# o название магазина;
# o список товаров (список словарей вида {"name": ..., "price": ...,
# "quantity": ...}).
# 2. Методы:
# o add_product(name, price, quantity) — добавить товар в магазин.
# o remove_product(name) — удалить товар по имени.
# o update_price(name, new_price) — изменить цену товара.
# o sell_product(name, quantity) — продать указанное количество товара
# (уменьшить остаток, если хватает).
# o get_inventory() — вернуть список всех товаров и их количество.
# o find_most_expensive() — вернуть самый дорогой товар.
# o find_cheapest() — вернуть самый дешёвый товар.
class Store:
    def __init__(self, name: str, product_list: list[dict]) -> None:
        self.name = name
        self.product_list = product_list

    def add_product(self, name: str, price: int, quantity: int) -> None:
        product = {
            "name": name,
            "price": price,
            "quantity": quantity
        }
        self.product_list.append(product)

    def remove_product(self, name: str) -> None:
        for product in self.product_list:
            if product["name"] in self.product_list:
                self.product_list.remove(product)

    def update_price(self, name: str, new_price: int) -> None:
        for product in self.product_list:
            if product["name"] == name:
                product["price"] = new_price

    def sell_product(self, name: str, quantity: int) -> None:
        for product in self.product_list:
            if product["name"] == name and product["quantity"] > quantity:
                product["quantity"] -= quantity
            else:
                print(f"Осталось {product["quantity"]} шт товара для покупки")
                print(f"Продукт был распродан, вы приобрели {product["quantity"]} шт товара")
                product["quantity"] = 0
                self.product_list.remove(product)

    def get_inventory(self) -> list[dict]:
        return [{"name": p["name"], "quantity": p["quantity"]} for p in self.product_list]

    def find_most_expensive(self):
        print("Продукт с самой высокой ценой:")
        return max(self.product_list, key=lambda x: x["price"])

    def find_cheapest(self):
        print("Продукт с самой низкой ценой:")
        return min(self.product_list, key=lambda x: x["price"])


c = Store("Gippo", [])
c.add_product("choсolate", 10, 2)
c.add_product("tea", 30, 3)
print(c.name)
# print(c.product_list)
# c.update_price("choсolate", 15)
# print(c.product_list)
# c.sell_product("choсolate", 5)
# print(c.product_list)
# print(c.get_inventory())
print(c.find_most_expensive())
print(c.find_cheapest())


