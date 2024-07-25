""""СКИЦА"""

class Building:
    def __init__(self, floors_count, color, material):
        self.floors_count = floors_count
        self.color = color
        self.material = material


sofia_building = Building(floors_count=12, color='red', material='xG')
print(sofia_building.color)
varna_building = Building(floors_count=12, color='red', material='xG')

print(id(sofia_building))
print(id(varna_building))
plovdiv_building = Building(floors_count=4, color='green', material='zX')