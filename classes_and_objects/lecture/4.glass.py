class Glass:
    capacity = 250

    def __init__(self) -> None:
        self.content = 0

    def fill(self, ml: float) -> str:
        if (self.content + ml) <= Glass.capacity:
            self.content += ml
            return f"Glass filled with {ml} ml"
        return f"Cannot add {ml} ml"

    def empty(self) -> str:
        self.content = 0
        return 'Glass is now empty'

    def info(self):
        space_left = self.capacity - self.content
        return f"{space_left} ml left"


#Test code
glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
