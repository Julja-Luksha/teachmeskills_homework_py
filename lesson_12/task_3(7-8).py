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

# Задание 8. Класс «Тренажёрный зал»
# Создай класс Gym.
# Требования:
# 1. Атрибуты: название зала, список клиентов (имя, возраст, абонемент активен/не
# активен).
# 2. Методы:
# o add_client(name, age) — добавить клиента.
# o remove_client(name) — удалить клиента.
# o activate_membership(name) — активировать абонемент клиента.
# o deactivate_membership(name) — деактивировать абонемент.
# o get_active_members() — вернуть список клиентов с активным абонементом.
# o find_youngest_client() — вернуть самого молодого клиента.
# o find_oldest_client() — вернуть самого старшего клиента.
# o average_age() — средний возраст клиентов.

class Gym:
    def __init__(self, name: str) -> None:
        self.name = name
        self.clients = []

    def add_client(self, name: str, age: int) -> None:
        client = {
            "name": name,
            "age": age,
            "active": False
        }
        self.clients.append(client)

    def remove_client(self, name: str) -> bool:
        for client in self.clients:
            if client["name"] == name:
                self.clients.remove(client)
            return True
        return False

    def activate_membership(self, name: str) -> bool:
        for client in self.clients:
            if client["name"] == name:
                client["active"] = True
                return True
        return False

    def deactivate_membership(self, name: str) -> bool:
        for client in self.clients:
            if client["name"] == name:
                client["active"] = False
                return True
        return False

    def get_active_members(self) -> list:
        return [client for client in self.clients if client["active"] == True]

    def find_youngest_client(self) -> int:
        return min(self.clients, key=lambda client: client["age"])

    def find_oldest_client(self) -> int:
        return max(self.clients, key=lambda client: client["age"])

    def average_age(self) -> float:
        return sum(client["age"] for client in self.clients) / len(self.clients)

g = Gym("24h")
g.add_client("Юлия", 31)
g.add_client("Анна", 20)
print(g.find_youngest_client())
print(g.find_oldest_client())
print(g.average_age())
print(g.clients)
g.activate_membership("Юлия")
print(g.clients)