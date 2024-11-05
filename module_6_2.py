class Sedan:
    ALLOWED_COLORS = {'blue', 'red', 'green', 'black', 'white'}

    def __init__(self, owner, model, color, mileage):
        self.owner = owner
        self.model = model
        self.mileage = mileage
        self.set_color(color)

    def set_color(self, color):

        if color.lower() in self.ALLOWED_COLORS:
            self.color = color.lower()
        else:
            print(f"Нельзя сменить цвет на {color}")

    def print_info(self):

        print(f"Владелец: {self.owner}")
        print(f"Модель: {self.model}")
        print(f"Цвет: {self.color}")
        print(f"Пробег: {self.mileage} км")

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

vehicle1.print_info()

vehicle1.set_color('Pink')   # Нельзя сменить цвет на Pink
vehicle1.set_color('BLACK')  # Цвет изменится на BLACK
vehicle1.owner = 'Vasyok'    # Меняем владельца

# Проверяем, что поменялось
vehicle1.print_info()
