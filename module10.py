"""1. Write an Elevator class that receives the numbers of the bottom and top floors as initializer parameters.
The elevator has methods go_to_floor, floor_up and floor_down. A new elevator is always at the bottom floor.
 If you make elevator h for example the method call h.go_to_floor(5), the method calls either the floor_up
 or floor_down methods as many times as it needs to get to the fifth floor. The methods run the elevator one
 floor up or down and tell what floor the elevator is after each move. Test the class by creating an elevator
 in the main program, tell it to move to a floor of your choice and then back to the bottom floor."""


class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print(f"Invalid floor: {target_floor}. Must be between {self.bottom_floor} and {self.top_floor}.")
            return

        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Going up... Current floor: {self.current_floor}")
        else:
            print("Already at the top floor.")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Going down... Current floor: {self.current_floor}")
        else:
            print("Already at the bottom floor.")

"""2.Extend the previous program by creating a Building class. The initializer parameters for the class are the numbers 
of the bottom and top floors and the number of elevators in the building. When a building is created, the building
 creates the required number of elevators. The list of elevators is stored as a property of the building. 
 Write a method called run_elevator that accepts the number of the elevator and the destination floor as its parameters.
  In the main program, write the statements for creating a new building and running the elevators of the building."""
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print(f"Invalid floor: {target_floor}. Must be between {self.bottom_floor} and {self.top_floor}.")
            return

        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator going up... Current floor: {self.current_floor}")
        else:
            print("Already at the top floor.")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator going down... Current floor: {self.current_floor}")
        else:
            print("Already at the bottom floor.")

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        if elevator_number < 0 or elevator_number >= len(self.elevators):
            print(f"Invalid elevator number: {elevator_number}.")
            return
        print(f"Running Elevator {elevator_number + 1} to floor {destination_floor}:")
        self.elevators[elevator_number].go_to_floor(destination_floor)

"""3.Extend the program again by adding a method fire_alarm that does not receive any parameters and moves all 
elevators to the bottom floor. Continue the main program by causing a fire alarm in your building."""


class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print(f"Invalid floor: {target_floor}. Must be between {self.bottom_floor} and {self.top_floor}.")
            return

        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator going up... Current floor: {self.current_floor}")
        else:
            print("Already at the top floor.")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator going down... Current floor: {self.current_floor}")
        else:
            print("Already at the bottom floor.")


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        if elevator_number < 0 or elevator_number >= len(self.elevators):
            print(f"Invalid elevator number: {elevator_number}.")
            return
        print(f"Running Elevator {elevator_number + 1} to floor {destination_floor}:")
        self.elevators[elevator_number].go_to_floor(destination_floor)

    def fire_alarm(self):
        print("Fire alarm activated! Moving all elevators to the bottom floor.")
        for idx, elevator in enumerate(self.elevators):
            elevator.go_to_floor(elevator.bottom_floor)

