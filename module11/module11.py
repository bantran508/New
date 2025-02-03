
class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, pagecount):
        super().__init__(name)
        self.author = author
        self.pagecount = pagecount

    def print_information(self):
        print(f"Book Name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Page Count: {self.pagecount}")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Magazine Name: {self.name}")
        print(f"Chief Editor: {self.chief_editor}")


if __name__ == "__main__":

    magazine = Magazine("Donald Duck", "Aki Hyyppä")
    book = Book("Compartment No. 6", "Rosa Liksom", 192)

    magazine.print_information()
    print()
    book.print_information()


class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.km_counter = 0

    def drive(self, hours):
        self.km_counter += self.max_speed * hours

class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume

if __name__ == "__main__":

    electric_car = ElectricCar("ABC-15", 180, 52.5)
    gasoline_car = GasolineCar("ACD-123", 165, 32.3)

    electric_car.drive(3)
    gasoline_car.drive(3)

    print(f"{electric_car.registration_number} has driven {electric_car.km_counter} km.")
    print(f"{gasoline_car.registration_number} has driven {gasoline_car.km_counter} km.")