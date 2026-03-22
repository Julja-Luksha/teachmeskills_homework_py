# Задание 5. Класс «Система заказов»
# Создай класс Order и класс OrderSystem.
# Order:
# • Атрибуты: номер заказа, список товаров (список словарей {"name": ..., "price":
# ..., "quantity": ...}), статус заказа.
# • Методы:
# o calculate_total() — возвращает сумму заказа.
# o add_item(name, price, quantity) — добавляет товар в заказ.
# o remove_item(name) — удаляет товар из заказа.
# o change_status(status) — изменяет статус заказа (например, «новый», «в
# работе», «завершён»).
# OrderSystem:
# • Атрибуты: список всех заказов.
# • Методы:
# o create_order() — создаёт новый заказ.
# o get_order_by_id(order_id) — возвращает заказ по номеру.
# o get_total_revenue() — возвращает общую сумму по всем завершённым
# заказам.
# o list_orders_by_status(status) — возвращает все заказы с определённым
# статусом.
from typing import Optional, List


class Status:
    def __init__(self) -> None:
        self.new = "новый"
        self.in_work = "в работе"
        self.end = "завершен"
        self.default = self.new


class Order:
    def __init__(self, order_number: int, status: Status) -> None:
        self.order_number = order_number
        self.product_list = []
        self.status_obj = status
        self.status = status.default

    def add_product(self, name: str, price: float, quantity: int) -> None:
        self.product_list.append({"name": name, "price": price, "quantity": quantity})

    def remove_product(self, name: str) -> bool:
        for item in self.product_list:
            if item["name"] == name:
                self.product_list.remove(item)
                return True
        return False

    def calculate_total(self) -> float:
        return sum(item["price"] * item["quantity"] for item in self.product_list)

    def change_status(self, status_name: str) -> None:
        if status_name == "новый":
            self.status = self.status_obj.new
        elif status_name == "в работе":
            self.status = self.status_obj.in_work
        elif status_name == "завершен":
            self.status = self.status_obj.end


class OrderSystem:
    def __init__(self) -> None:
        self.orders = []
        self.status = Status()
        self._id = 1

    def create_order(self) -> Order:
        order = Order(self._id, self.status)
        self.orders.append(order)
        self._id += 1
        return order

    def get_order_by_id(self, order_number: int) -> Optional[Order]:
        for order in self.orders:
            if order.order_number == order_number:
                return order
        return None

    def get_total_revenue(self) -> float:
        total_revenue = 0
        for order in self.orders:
            if order.status == self.status.end:
                total_revenue += order.calculate_total()
        return total_revenue

    def list_orders_by_status(self, status_name: str) -> List[Order]:
        return [order for order in self.orders if order.status == status_name]


system_order = OrderSystem()
order1 = system_order.create_order()
print(order1.order_number)
order2 = system_order.create_order()
print(order2.order_number)
print(order2.status)
order2.change_status("в работе")
print(order2.status)
order1.add_product("капучино", 10, 1)
order1.add_product("бигмак", 21, 1)
print(order1.calculate_total())
found = system_order.get_order_by_id(1)
print(found is order1)
order2.change_status("завершен")
print(system_order.get_total_revenue())
order1.change_status("завершен")
print(system_order.get_total_revenue())
