class BeeElefant:
    def __init__(self, bee_part, elefant_part):
        self.bee_part = bee_part
        self.elefant_part = elefant_part

    def fly(self):
        if self.bee_part >= self.elefant_part:
            return True
        else:
            return False

    def trumpet(self):
        if self.elefant_part >= self.bee_part:
            return "tu-tu-doo-doo!"
        else:
            return "wzzzz"

    def eat(self, meal, value):
        if meal == "nectar":
            self.elefant_part -= value
            self.bee_part += value
        elif meal == "grass":
            self.elefant_part += value
            self.bee_part -= value

        if self.elefant_part > 100:
            self.elefant_part = 100
        elif self.elefant_part < 0:
            self.elefant_part = 0
        if self.bee_part > 100:
            self.bee_part = 100
        elif self.bee_part < 0:
            self.bee_part = 0

    def __str__(self):
        return f"BeeElefant(bee={self.bee_part}, elephant={self.elefant_part})"

while True:
    bee_part = input("Введите пчелиную часть: ")
    elefant_part = input("Введите слоновью часть: ")
    if bee_part.isdigit() and elefant_part.isdigit():
        bee_part = int(bee_part)
        elefant_part = int(elefant_part)
        break
    else:
        print("Введите целые числа!")
bee_elefant = BeeElefant(bee_part, elefant_part)
print(f"\nПчёлоСлон готов!"
      f"\nПчелиная часть: {bee_part}"
      f"\nСлоновья часть: {elefant_part}")

print("\nМожет ли ваш ПчёлоСлон летать?")
if bee_elefant.fly() is True:
    print("Да, может!")
else:
    print("Нет, не может!")

print("\nКакие звуки издает ваш ПчёлоСлон?")
print(bee_elefant.trumpet())

eat_input = input("\nЧем вы хотите накормить ПчёлоСлона?"
                  "\n1 -- нектар"
                  "\n2 -- трава: ")

if eat_input == "1":
    while True:
        value = input("Введите количество съеденного: ")
        if value.isdigit():
            value = int(value)
            break
        else:
            print("Введите целое число!")
    bee_elefant.eat("nectar", value)

if eat_input == "2":
    while True:
        value = input("Введите количество съеденного: ")
        if value.isdigit():
            value = int(value)
            break
        else:
            print("Введите целое число!")
    bee_elefant.eat("grass", value)

print(f"\nПчёлоСлон после легкого перекуса"
      f"\nПчелиная часть: {bee_elefant.bee_part}"
      f"\nСлоновья часть: {bee_elefant.elefant_part}")

print("\nМожет ли теперь ваш ПчёлоСлон летать?")
if bee_elefant.fly() is True:
    print("Да, может!")
else:
    print("Нет, не может!")

print("\nКакие звуки теперь издает ваш ПчёлоСлон?")
print(bee_elefant.trumpet())