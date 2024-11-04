#1
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0  # Automatically set to zero
        self.travelled_distance = 0  # Automatically set to zero

my_car = Car("ABC-123", 142)

print(f"Registration Number: {my_car.registration_number}")
print(f"Maximum Speed: {my_car.maximum_speed} km/h")
print(f"Current Speed: {my_car.current_speed} km/h")
print(f"Travelled Distance: {my_car.travelled_distance} km")
#2
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0  # Automatically set to zero
        self.travelled_distance = 0  # Automatically set to zero

    def accelerate(self, change):
        new_speed = self.current_speed + change
        if new_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

my_car = Car("ABC-123", 142)
my_car.accelerate(30)
my_car.accelerate(70)
my_car.accelerate(50)
print(f"Current Speed after acceleration: {my_car.current_speed} km/h")
my_car.accelerate(-200)
print(f"Final Speed after emergency brake: {my_car.current_speed} km/h")
#3
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        new_speed = self.current_speed + change
        if new_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

    def drive(self, hours):

        self.travelled_distance += self.current_speed * hours

my_car = Car("ABC-123", 142)
my_car.accelerate(30)
my_car.accelerate(70)
my_car.accelerate(50)
print(f"Current Speed after acceleration: {my_car.current_speed} km/h")
my_car.drive(1.5)
print(f"Travelled Distance after driving: {my_car.travelled_distance} km")
my_car.accelerate(-200)
print(f"Final Speed after emergency brake: {my_car.current_speed} km/h")
my_car.drive(1)
print(f"Travelled Distance after driving again: {my_car.travelled_distance} km")
