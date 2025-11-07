class Product:
    def __init__(self, name, shop_name, price):
        self.__name = name
        self.__shop_name = shop_name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_shop_name(self):
        return self.__shop_name

    def get_price(self):
        return self.__price

    def __add__(self, other):
        if isinstance(other, Product):
            return self.__price + other.__price
        else:
            raise ValueError("")


class Storage:
    def __init__(self):
        self.__storage = []

    def add_product(self, product):
        self.__storage.append(product)

    def get_product_by_index(self, index):
        if index >= 0 and index < len(self.__storage):
            return self.__storage[index]
        else:
            return None


    def get_product_by_name(self, name):
        found_product = []
        for product in self.__storage:
            product_name = product.get_name().lower()
            if product_name == name.lower():
                found_product.append(product)
        if found_product:
            return found_product
        return None

    def sort_by_name(self):
        self.__storage.sort(key=lambda product: product.get_name())

    def sort_by_shop_name(self):
        self.__storage.sort(key=lambda product: product.get_shop_name())

    def sort_by_price(self):
        self.__storage.sort(key=lambda product: product.get_price())

    def sort_by_reverse_price(self):
        self.__storage.sort(key=lambda product: product.get_price(), reverse=True)

    def display_products(self):
        if not self.__storage:
            print("Склад пуст")
            return

        print("\nТовары на складе:")
        for i, product in enumerate(self.__storage, 1):
            print(f"\nИндекс товара: {i}"
                  f"\nНазвание: {product.get_name()}"
                  f"\nМагазин: {product.get_shop_name()}"
                  f"\nЦена: {product.get_price()} руб.")


product_one = Product("Ноутбук", "5 Элемент", 2500)
product_two = Product("Кофемашина", "DNS", 1000)
product_three = Product("Телефон", "DNS", 1000)
product_four = Product("Стиральная машина", "Samsung", 3000)

storage = Storage()
storage.add_product(product_one)
storage.add_product(product_two)
storage.add_product(product_three)
storage.add_product(product_four)

storage.display_products()

while True:
    user_input = input("\nВыберите режим программы:"
                       "\n1 -- Поиск товара по индексу"
                       "\n2 -- Поиск товара по названию"
                       "\n3 -- Сортировка товаров по названию товара"
                       "\n4 -- Сортировка товаров по названию магазина"
                       "\n5 -- Сортировка товаров по цене (возрастанию/убыванию)"
                       "\n6 -- Сложение товаров по цене"
                       "\n7 -- Выход из программы: ")


    if user_input == "1":
        index = input("Введите индекс товара: ")
        while True:
            if index.isdigit():
                index = int(index)
                break
            else:
                print("Неверный ввод! Введите целое число")

        found_product = storage.get_product_by_index(index)
        if found_product:
            print(f"Товар найден:"
                  f"\nНазвание: {found_product.get_name()}"
                  f"\nМагазин: {found_product.get_shop_name()}"
                  f"\nЦена: {found_product.get_price()} руб.")
        else:
            print("Товар не найден")

    if user_input == "2":
        foud_by_name = input("Введите название товара: ")
        found_product_by_name = storage.get_product_by_name(foud_by_name)
        if found_product_by_name:
            for product in found_product_by_name:
                print(f"Товар найден:"
                    f"\nНазвание: {product.get_name()}"
                    f"\nМагазин: {product.get_shop_name()}"
                    f"\nЦена: {product.get_price()} руб.")
        else:
            print("Товар не найден")

    if user_input == "3":
        print("\nСортировка по названию товара")
        storage.sort_by_name()
        storage.display_products()

    if user_input == "4":
        print("\nСортировка по названию магазина")
        storage.sort_by_shop_name()
        storage.display_products()

    if user_input == "5":
        print("\nСортировка по цене (по возрастанию)")
        storage.sort_by_price()
        storage.display_products()

        print("\nСортировка по цене (по убыванию)")
        storage.sort_by_reverse_price()
        storage.display_products()

    if user_input == "6":
        result_one = product_one + product_two
        result_two = product_three + product_four
        result = result_one + result_two
        print(f"Сумма цен всех товаров {result} руб.")

    if user_input == "7":
        break