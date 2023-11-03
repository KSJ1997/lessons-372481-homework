from animal import Animal, DomesticAnimal, PackAnimal, YoungAnimal
from registry import Registry
from menu import Menu
from counter import Counter

def main():
    try:
        with Counter() as counter:
            while True:
                Menu.display_menu()
                choice = input("Выберите опцию: ")

                if choice == "1":
                    name = input("Введите имя животного: ")
                    command = input("Введите команду животного: ")

                    if name and command:
                        animal = Animal(name, command)

                        if name.lower() == "собака":
                            animal = DomesticAnimal(name, command)
                        elif name.lower() == "лошадь":
                            animal = PackAnimal(name, command)
                        elif name.lower() == "молодое животное":
                            animal = YoungAnimal(name, command)

                        Registry.add_animal(animal)
                        counter.add()

                        print(f"Животное успешно добавлено в реестр. Всего животных: {counter.count}")
                    else:
                        print("Имя и команда животного должны быть заполнены.")

                elif choice == "2":
                    name = input("Введите имя животного: ")
                    command = Registry.list_commands(Animal(name, ""))
                    if command:
                        print(f"Команда животного: {command}")
                    else:
                        print("Животное не найдено в реестре.")

                elif choice == "3":
                    name = input("Введите имя животного: ")
                    new_command = input("Введите новую команду: ")
                    animal = Animal(name, new_command)
                    Registry.add_animal(animal)
                    print(f"Животное успешно обучено новой команде: {new_command}")

                elif choice == "4":
                    print("Выход из программы.")
                    break

                else:
                    print("Неверный выбор. Попробуйте снова.")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
