class Building:
    def __init__(self, name: str, floors: int):
        self.name = name
        self.floors = floors

    def add_floors(self, amount: int) -> None:
        self.floors += amount

my_building = Building('My House', 2)
print(my_building.floors)

my_building.add_floors(3)
print(my_building.floors)