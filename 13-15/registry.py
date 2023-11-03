from collections import Counter
from animal import Animal, DomesticAnimal, PackAnimal, YoungAnimal

class Registry:
    animals = []

    @classmethod
    def add_animal(cls, animal):
        cls.animals.append(animal)
        Counter.add()

    @classmethod
    def list_commands(cls, animal):
        for a in cls.animals:
            if a.name == animal.name and a.command == animal.command:
                return a.command
