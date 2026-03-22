# Задание 3. Класс «Библиотека» и класс «Книга»
# Создай два класса: Book и Library.
# Book:
# • Атрибуты: название, автор, год издания, статус (в библиотеке или выдана).
# • Метод info() — выводит информацию о книге.
# • Метод mark_as_taken() — меняет статус на «выдана».
# • Метод mark_as_returned() — меняет статус на «в библиотеке».
# Library:
# • Атрибуты: название библиотеки, список книг.
# • Методы:
# o add_book(book) — добавляет книгу в библиотеку.
# o remove_book(book) — удаляет книгу из библиотеки.
# o find_by_author(author) — находит все книги автора.
# o find_by_year(year) — находит все книги указанного года.
# o available_books() — возвращает список всех книг, которые в библиотеке.
# o taken_books() — возвращает список всех выданных книг.
class Status:
    def __init__(self) -> None:
        self.in_lib = "в библиотеке"
        self.not_in_lib = "выдана"
        self.now = self.in_lib


class Book:
    def __init__(self, name: str, author: str, year: int, status: Status) -> None:
        self.name = name
        self.author = author
        self.year = year
        self.status = status

    def info(self) -> str:
        return (f"Название: {self.name} | Автор: {self.author} | Год издания: {self.year}"
                f" | Статус: {self.status.now}")

    def book_is_taken(self) -> None:
        self.status.now = self.status.not_in_lib
        print("Книга выдана")

    def book_is_returned(self) -> None:
        self.status.now = self.status.in_lib
        print("Книга возвращена в библиотеку")


class Library:
    def __init__(self, name: str, books: list) -> None:
        self.books = books
        self.name = name

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        print("Книга добавлена в список")

    def remove_book(self, book: Book) -> None:
        self.books.remove(book)

    def available_books(self) -> None:
        print("Список книг в библиотеке:")
        count = 0
        idx = 1
        for book in self.books:
            if book.status.now == book.status.in_lib:
                print(f"{idx}: {book.info()} ")
                count += 1
                idx += 1
        if count == 0:
            print("В бибилиотеке нет книг для выдачи")

    def taken_books(self) -> list:
        print("Список выданных книг:")
        result = []
        for book in self.books:
            if book.status.now == book.status.not_in_lib:
                result.append(book)
        if len(result) == 0:
            print("Не выдано ни одной книги")
        return result

    def find_by_author(self, author: str) -> list:
        result = []
        for book in self.books:
            if book.author == author:
                result.append(book)
        return result

    def find_by_year(self, year: int) -> list:
        result = []
        for book in self.books:
            if book.year == year:
                result.append(book)
        return result


s = Status()
b = Book("Мастер и Маргарита", "Булгаков", 1984, Status())
c = Book("Мертвые души", "Гоголь", 1842, Status())
d = Book("Вий", "Гоголь", 1835, Status())
print(b.info())
# b.book_is_taken()
# print(b.info())
l = Library("Центральная", [])
print(f"{l.name} библиотека")
l.add_book(b)
l.add_book(c)
l.add_book(d)
l.available_books()
books = l.find_by_author("Гоголь")
for book in books:
    print(book.info())
b_year = l.find_by_year(1835)
for book in b_year:
    print(book.info())
l.taken_books()



# Задание 4. Класс «Кошелёк»
# Создай класс Wallet, описывающий электронный кошелёк.
# Требования:
# 1. Приватный атрибут _balance.
# 2. Методы:
# o deposit(amount) — пополнить кошелёк.
# o withdraw(amount) — снять деньги (если хватает).
# o transfer_to(other_wallet, amount) — перевести деньги другому кошельку.
# o __apply_bonus() (приватный метод) — добавить 1% бонуса к балансу,
# вызывается автоматически после каждой операции пополнения.
# 3. property balance — позволяет просматривать баланс.
# 4. Статический метод wallet_info(wallet) — выводит краткую информацию о кошельке.

class Wallet:
    def __init__(self) -> None:
        self._balance = 0.0

    def __apply_bonus(self) -> None:
        self._balance *= 1.01

    def deposit(self, amount: float) -> None:
        self._balance += amount
        self.__apply_bonus()
        print(f"Кошелек пополнен на {amount}")

    def withdraw(self, amount: float) -> None:
        if amount > self._balance:
            print("Недостаточно денег на счете для выдачи")
        else:
            self._balance -= amount

    def transfer_to(self, other_wallet: Wallet, amount: float) -> None:
        if amount > self._balance:
            print("Недостаточно денег на счете для перевода")
        else:
            self._balance = self._balance - amount
            other_wallet.deposit(amount)
            print(f"Перевод осуществлен, сумма перевода: {amount}")



    def property_balance(self) -> str: #В принципе, аналог статического, но такое задание
        return f"Баланс счета: {self._balance}"

    @staticmethod
    def wallet_info(wallet: Wallet) -> str:
        return f"Баланс счета: {wallet._balance}"


w = Wallet()
ww = Wallet()
print(w.wallet_info(w))
w.deposit(100)
print(w.wallet_info(w))
w.withdraw(500)
w.transfer_to(ww, 500)
print(ww.wallet_info(ww))
w.transfer_to(ww, 100)
# print(ww.wallet_info(ww))
# print(w.wallet_info(w))
print(w.property_balance())
