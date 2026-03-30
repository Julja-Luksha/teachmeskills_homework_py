from lesson_15.src.db_connector import session
from lesson_15.src.models import User
from lesson_15.src.services import ProductService, UserService, OrderService, TicketService
from lesson_15.src.views import print_main_menu, show_products, print_user_menu, show_profile


def main():
    current_user: User | None = None

    while True:
        if current_user is None:
            print_main_menu()
            choice = input("Введите номер пункта меню: ").strip()

            if choice == "1":
                products = ProductService.get_available_products()
                show_products(products)

            elif choice == "2":
                data = input("Введите логин и пароль через пробел: ").split()
                if len(data) != 2:
                    print("Нужно ввести два значения.")
                    continue
                username, password = data
                user = UserService.register(username, password)
                if user is None:
                    print("Пользователь с таким именем уже существует.")
                else:
                    current_user = user
                    print(f"Пользователь {user.username} успешно зарегистрирован и авторизован.")

            elif choice == "3":
                data = input("Введите логин и пароль через пробел: ").split()
                if len(data) != 2:
                    print("Нужно ввести два значения.")
                    continue
                username, password = data
                user = UserService.login(username, password)
                if user is None:
                    print("Неверный логин или пароль.")
                else:
                    current_user = user
                    print(f"Вы вошли как {user.username}.")

            elif choice == "4":
                print("Завершение сеанса...")
                session.close()
                break
            else:
                print("Такого пункта меню нет.")
                continue

        else:
            print_user_menu(current_user)
            choice = input("Введите номер пункта: ").strip()

            if choice == "1":
                products = ProductService.get_available_products()
                show_products(products)

            elif choice == "2":
                products = ProductService.get_available_products()
                show_products(products)

                try:
                    product_id = int(input("Введите ID товара: ").strip())
                    count = int(input("Введите количество: ").strip())
                except ValueError:
                    print("Нужно вводить числа.")
                    continue

                product = ProductService.get_product_by_id(product_id)
                if not product:
                    print("Товар не найден.")
                    continue

                order = OrderService.create_order(current_user, product, count)

                if order is None:
                    print("Недостаточно товара или поинтов.")
                else:
                    print(
                        f'Вы успешно купили "{product.name}" в количестве {count}. '
                        f"У вас осталось {current_user.points} поинтов."
                    )

            elif choice == "3":
                orders = current_user.orders(session)
                show_profile(current_user, orders)

            elif choice == "4":
                ticket_uuid = input("Введите UUID тикета: ").strip()
                ok = TicketService.redeem_ticket(current_user, ticket_uuid)

                if ok:
                    print(
                        f"Вы успешно обменяли тикет на 20 поинтов!\n"
                        f"Теперь у вас - {current_user.points} поинтов."
                    )
                else:
                    print("Неверный или уже использованный тикет.")

            elif choice == "5":
                print(f"Пользователь {current_user.username} вышел.")
                current_user = None

            else:
                print("Такого пункта меню нет.")
                continue


if __name__ == "__main__":
    main()
