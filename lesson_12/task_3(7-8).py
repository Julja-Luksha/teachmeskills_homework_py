# Задание 7. Класс «Игровой инвентарь»
# Создай класс Inventory, представляющий инвентарь игрока.
# Требования:
# 1. Атрибуты: список предметов (каждый предмет — словарь с полями name, weight, value).
# 2. Методы:
# o add_item(name, weight, value) — добавить предмет.
# o remove_item(name) — удалить предмет.
# o get_total_weight() — вернуть общий вес.
# o get_total_value() — вернуть общую стоимость.
# o find_heaviest() — найти самый тяжёлый предмет.
# o find_most_valuable() — найти самый дорогой предмет.
# o sort_by_value() — вернуть предметы, отсортированные по стоимости.
# o sort_by_weight() — вернуть предметы, отсортированные по весу.

class Inventory:
    def __init__(self) -> None:
        self.items = []

    def add_item(self, name: str, weight: float, value: int) -> None:
        item = {
            "name": name,
            "weight": weight,
            "value": value
        }
        self.items.append(item)

    def remove_item(self, name: str) -> bool:
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                return True
        return False

    def get_total_weight(self) -> float:
        total_weight = 0
        for item in self.items:
            total_weight += item["weight"]
        return total_weight

    def get_total_value(self) -> int:
        total_value = 0
        for item in self.items:
            total_value += item["value"]
        return total_value

    def find_heaviest(self) -> float:
        return max(item["weight"] for item in self.items)

    def find_most_valuable(self) -> int:
        return max(item["value"] for item in self.items)

    def sort_by_value(self) -> list:
        return sorted(self.items, key=lambda item: item["value"])

    def sort_by_weight(self) -> list:
        return sorted(self.items, key=lambda item: item["weight"])

i = Inventory()
i.add_item("ящик", 12, 50)
i.add_item("нож", 0.3, 10)
print(i.find_heaviest())
print(i.find_most_valuable())
print(i.sort_by_value())
print(i.sort_by_weight())
print(i.get_total_weight())
print(i.get_total_value())