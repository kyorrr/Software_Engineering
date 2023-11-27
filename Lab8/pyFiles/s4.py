class Flat:
    def __init__(self, area, cost):
        self._area = area
        self.__cost = cost

    def sell(self):
        print(f'Покупаю квартиру площадью {self._area} и стоит она {self.__cost}')

my_flat = Flat("80m2", "10,000$")
my_flat.sell()
print(my_flat._area)