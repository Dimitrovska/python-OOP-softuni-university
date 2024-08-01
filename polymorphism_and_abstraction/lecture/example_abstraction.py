from abc import ABC, abstractmethod


class Person(ABC):

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 2:
            raise ValueError('Person name must be a least two chars')
        self.__name = value

    @abstractmethod
    def go_to_work(self):
        pass


class Teacher(Person):
    def go_to_work(self):
        return 'Going to the school'


class Student(Person):
    def go_to_work(self):
        return 'Going to the library'


t = Teacher('Liya')
print(t)
