class Flat:
    def __init__(self, area, cost):
        self.area = area
        self.cost = cost

    def sell(self):
        print(f'Покупаю квартиру площадью {self.area} и стоит она {self.cost}')

my_flat = Flat("80m2", "10,000$")
my_flat.sell()