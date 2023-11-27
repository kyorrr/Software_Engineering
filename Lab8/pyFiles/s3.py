class Flat:
    def __init__(self, area, cost):
        self.area = area
        self.cost = cost

    def sell(self):
        print(f'Покупаю квартиру площадью {self.area} и стоит она {self.cost}')

class Apartment(Flat):
    def __init__(self, area, cost, place):
        super().__init__(area, cost)
        self.place = place

    def placement(self):
        print(f'Покупаю квартиру площадью {self.area}, '
              f'стоит она {self.cost} и находится по адресу {self.place}')

my_flat = Apartment("80m2", "10,000$", "Mira ST.")
my_flat.sell()
my_flat.placement()