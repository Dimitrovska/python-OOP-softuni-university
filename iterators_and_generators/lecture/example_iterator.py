class range_:
    def __init__(self, start, stop):
        self.start = start - 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start < self.stop:
            return self.start
        raise StopIteration


for el in range(1, 5):
    print(el)
