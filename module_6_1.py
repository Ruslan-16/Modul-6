class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False


class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False  


class Mammal(Animal):
    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                self.fed = True
                print(f"{self.name} съел {food.name}")
            else:
                self.alive = False
                print(f"{self.name} не стал есть {food.name} и погиб")
        else:
            print(f"{self.name} не может есть это - требуется растение.")


class Predator(Animal):
    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                self.fed = True
                print(f"{self.name} съел {food.name}")
            else:
                self.alive = False
                print(f"{self.name} не стал есть {food.name} и погиб")
        else:
            print(f"{self.name} не может есть это - требуется растение.")


class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)



class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True


# Пример использования:

# Создаем объекты классов
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

# Проверяем имена объектов
print(a1.name)  # Ожидаем: Волк с Уолл-Стрит
print(p1.name)  # Ожидаем: Цветик семицветик

# Проверяем начальные состояния
print(a1.alive)  # Ожидаем: True
print(a2.fed)    # Ожидаем: False

# Пробуем накормить животных
a1.eat(p1)       # Ожидаем: Волк с Уолл-Стрит не стал есть Цветик семицветик и погиб
a2.eat(p2)       # Ожидаем: Хатико съел Заводной апельсин

# Проверяем конечные состояния
print(a1.alive)  # Ожидаем: False (волк погиб)
print(a2.fed)    # Ожидаем: True (Хатико накормлен)
