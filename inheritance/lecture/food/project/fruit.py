from project.food import Food


class Fruit(Food):

    def __init__(self, name: str, expiraton_date: str):
        self.name = name
        super().__init__(expiraton_date)

