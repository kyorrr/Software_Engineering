class Cost:
    def cost(self):
        pass

class Flat(Cost):
    def __init__(self, area, placement):
        self.area = area
        self.placement = placement

    def cost(self):
        return self.area * 2 * self.placement * 1000

class Apartment(Cost):
    def __init__(self, area, placement):
        self.area = area
        self.placement = placement

    def cost(self):
        return self.area * 4 * self.placement * 1000


places = [Flat(62, 5), Apartment(80, 9)]
for place in places:
    print(place.cost())