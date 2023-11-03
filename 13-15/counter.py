class Counter:
    def __init__(self):
        self.count = 0

    def add(self):
        self.count += 1

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.count > 0:
            if exc_type is None:
                print("Ресурс закрыт успешно.")
            else:
                print("Произошла ошибка при работе с ресурсом.")
            self.count = 0
