class Tomatoes:
    states = {
        0: "отсутствует",
        1: "цветение",
        2: "зеленый",
        3: "красный"
    }

    def __init__(self, index):
        self._index = index  # Защищенный метод
        self._state = 0  # Защищенный метод

    def grow(self):
        if self._state <= 3:
            self._state += 1

    def is_ripe(self):
        return self._state == 3


class TomatoBush:
    def __init__(self, num_tomatoes):
        self.tomatoes = [Tomatoes(index) for index in range(1, num_tomatoes + 1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            print("Сбор урожая")
            self._plant.give_away_all()
        else:
            print("Урожай пока не созрел")

    @staticmethod
    def knowledge_base():
        print("База знаний садовода:")
        print("- Поливай растения регулярно.")
        print("- Нужно больше солнечного света.")
        print("- Иcпользуй удобрение.")
        print("- Не оставляй растения под солнечным светом надолго")
        print("- В холодное время суток закрывай растения")


# Тест 1
Gardener.knowledge_base()

# Тест 2
tomato_bush = TomatoBush(num_tomatoes=4)
gardener = Gardener(name="Sergey", plant=tomato_bush)

# Тест 4
gardener.harvest()

# Тест 3
gardener.work()
gardener.work()
gardener.work()

# Тест 4
gardener.harvest()

# Тест 5
# Выводим информацию о зрелости томатов в кусте после сбора урожая
print("\nВсе томаты созрели?", gardener._plant.all_are_ripe())
# Проверяем состояние каждого томата после сбора урожая
for i, tomato in enumerate(gardener._plant.tomatoes, 1):
    print(f"Tomato {i}: State - {Tomatoes.states[tomato._state]}, Ripe - {tomato.is_ripe()}")
