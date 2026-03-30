from enum import StrEnum

from sqlalchemy.sql.functions import user


class MainMenu(StrEnum):
    products = "1) Товары"
    registrate = "2) Зарегистрироваться"
    log_in = "3) Войти"
    exit = "4) Завершить сеанс"

class UserMenu(StrEnum):
    products = "1) Товары"
    buy = "2) Купить"
    profile = "3) Профиль"
    ticket = "4) Тикет"
    log_out = "5) Выйти"

def print_main_menu():
    print("""
=== Добро пожаловать в "Не магазин" === 
   
Здесь вы можете обменивать тикеты для того, чтобы приобретать товары 

Для взаимодействия выберите нужный пункт меню:       
    """)
    for item in MainMenu:
        print(f"> {item}")

def print_user_menu(user):
    print(f"""
=== Добро пожаловать в "Не магазин", {user.username}! === 

У вас {user.points} поинтов

Для взаимодействия выберите нужный пункт меню:    
    """)
    for item in UserMenu:
        print(f"> {item}")

def show_products(products):
    if not products:
        print("Нет доступных товаров")
        return
    line_products = f"{"ID":<4}{"Название":<25}{"Цена":<10}{"Количество":<12}"
    print(line_products)
    print("="*len(line_products))

    for p in products:
        print(
            f"{p.id:<4}"
            f"{p.name:<25}"
            f"{p.cost:<10}"
            f"{p.count:<12}"
        )


def show_profile(user, orders):
    print(f"\nПрофиль пользователя: {user.username}")
    print(f"Поинтов: {user.points}")
    print("Заказы:")
    if not orders:
        return

    for order, product in orders:
        line = (f"{order.order_date:%Y-%m-%d %H:%M} | {product.name:<25} | Количество: {order.count:<3} шт | "
                f"Сумма: {order.count * product.cost:>6} руб")
        print("=" * len(line))
        print(line)
        print("=" * len(line))



