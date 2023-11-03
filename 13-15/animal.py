class Animal:
    def __init__(self, name):
        self._name = name # Инкапсуляция имени животного
        self._command = ""

    def set_command(self, command):
        self._command = command

    def get_command(self):
        return self._command

class DomesticAnimal(Animal):
    def set_command(self, command):
        if command.lower() in ["sit", "stay", "fetch"]:
            super().set_command(command)
        else:
            print("Недопустимая команда для домашнего животного.")

class PackAnimal(Animal):
    def set_command(self, command):
        if command.lower() in ["carry", "pull", "transport"]:
            super().set_command(command)
        else:
            print("Недопустимая команда для вьючного животного.")

class CommandCounter:
    def __init__(self):
        self._count = 0  # Инкапсуляция счетчика

    def add(self):
        self._count += 1

    def get_count(self):
        return self._count