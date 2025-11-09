class Bus:
    def __init__(self, max_seat, max_speed, passengers_list=None):
        self.speed = 0
        self.max_seat = max_seat
        self.max_speed = max_speed
        self.passenger_surnames_list = []
        self.free_seat = True
        self.seats = {}

        for num_seat in range(1, max_seat + 1):
            self.seats[num_seat] = None

        if passengers_list:
            for passenger in passengers_list:
                self.board_passenger(passenger, None)

    def update_free_seats(self):
        self.free_seat = len(self.passenger_surnames_list) < self.max_seat

    def board_passenger(self, passenger, num_seat=None):
        if not self.free_seat:
            print("Свободных мест нет!")
            return False
        if passenger in self.passenger_surnames_list:
            print("Пассажир уже в автобусе!")
            return False

        if num_seat is None:
            for seat, taken in self.seats.items():
                if taken is None:
                    num_seat = seat
                    break

        if self.seats[num_seat] is not None:
                print("Место уже занято!")
                return False

        if num_seat not in self.seats:
            print("Такого места не существует!")
            return False

        self.seats[num_seat] = passenger
        self.passenger_surnames_list.append(passenger)
        self.update_free_seats()
        print("Пассажир посажен в автобус")
        return True

    def board_passengers(self, passengers):
        for passenger in passengers:
            board = self.board_passenger(passenger, None)
            if not board:
                break

    def unboard_passenger(self, passenger):
        if passenger not in self.passenger_surnames_list:
            print("Пассажира нет в автобусе!")
            return False

        for num_seat, taken in self.seats.items():
            if taken == passenger:
                self.seats[num_seat] = None
                break

        self.passenger_surnames_list.remove(passenger)
        self.update_free_seats()
        print("Пассажир высажен из автобуса")
        return True

    def unboard_passengers(self, passengers):
        for passenger in passengers:
            self.unboard_passenger(passenger)

    def more_speed(self, value):
        self.speed = min(self.speed + value, self.max_speed)
        print(f"Новая скорость: {self.speed}")

    def less_speed(self, value):
        self.speed = max(self.speed - value, 0)
        print(f"Новая скорость: {self.speed}")

    def __contains__(self, passenger):
        return passenger in self.passenger_surnames_list

    def __iadd__(self, passenger):
        self.board_passenger(passenger, None)
        return self

    def __isub__(self, passenger):
        self.unboard_passenger(passenger)
        return self

    def __str__(self):
        free_seats = self.max_seat - len(self.passenger_surnames_list)
        return (f"\nАвтобус:"
                f"\nСкорость: {self.speed}/{self.max_speed} км/ч"
                f"\nКоличество пассажиров: {len(self.passenger_surnames_list)}/{self.max_seat}"
                f"\nКоличество свободных мест: {free_seats}")

passengers_list = ["Иванов", "Сидоров", "Петров"]

while True:
        max_seats = input("Введите количество максимальных мест: ")
        if max_seats.isdigit():
            max_seats = int(max_seats)
            break
        else:
            print("Введите целое число!")
while True:
    max_speed = input("Введите максимальную скорость автобуса: ")
    if max_speed.isdigit():
        max_speed = int(max_speed)
        break
    else:
        print("Введите целое число!")

bus = Bus(max_seats, max_speed, passengers_list)
print(f"\nСозданный автобус:"
      f"\nМаксимальное количество мест: {bus.max_seat}"
      f"\nМаксимальная скорость: {bus.max_speed}"
      f"\nСписок пассажиров: {bus.passenger_surnames_list}")

while True:
    user_input = input("\nЧто вы хотите сделать? "
                       "\n1 -- Добавить одного пассажира"
                       "\n2 -- Добавить нескольких пассажиров"
                       "\n3 -- Высадить одного пассажира"
                       "\n4 -- Высадить нескольких пассажиров"
                       "\n5 -- Проверить, есть ли пассажир в автобусе"
                       "\n6 -- Увеличить скорость автобуса"
                       "\n7 -- Уменьшить скорость автобуса"
                       "\n8 -- Выход из программы: ")
    if user_input == "1":
        new_passenger = input("Введите фамилию нового пассажира: ")
        bus += new_passenger
        print(f"Список пассажиров: {bus.passenger_surnames_list}")

    elif user_input == "2":
        passengers_input = input("Введите фамилии новых пассажиров (через запятую): ")
        some_new_passengers = [name.strip() for name in passengers_input.split(",")]
        bus.board_passengers(some_new_passengers)
        print(f"Список пассажиров: {bus.passenger_surnames_list}")

    elif user_input == "3":
        print(f"Список пассажиров: {bus.passengers_surnames_list}")
        unboard_surname = input("Введите фамилию пассажира, которого хотите высадить: ")
        bus -= unboard_surname
        print(f"Список пассажиров: {bus.passenger_surnames_list}")

    elif user_input == "4":
        print(f"Список пассажиров: {bus.passenger_surnames_list}")
        passengers_input = input("Введите фамилии пассажиров, которых хотите высадить (через запятую): ")
        some_unboard_passengers = [name.strip() for name in passengers_input.split(",")]
        bus.unboard_passengers(some_unboard_passengers)
        print(f"Список пассажиров: {bus.passenger_surnames_list}")

    elif user_input == "5":
        print(f"Список пассажиров: {bus.passenger_surnames_list}")
        check_passenger = input("Введите фамилию пассажира: ")
        if check_passenger in bus:
            print("Пассажир в автобусе")
        else:
            print("Пассажир не в автобусе")

    elif user_input == "6":
        while True:
            value = input("Введите новую скорость (увеличить скорость): ")
            if value.isdigit():
                value = int(value)
                break
            else:
                print("Введите целое число!")
        bus.more_speed(value)
        print(bus)

    elif user_input == "7":
        while True:
            value = input("Введите новую скорость (уменьшить скорость): ")
            if value.isdigit():
                value = int(value)
                break
            else:
                print("Введите целое число!")
        bus.less_speed(value)
        print(bus)

    elif user_input == "8":
        break

    else:
        print("Неверный ввод! Выберите пункт из меню программы!")