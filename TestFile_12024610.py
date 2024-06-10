#intialize

parking_lot = []

def output_a_message(msg1):
    print(msg1)


def park_car(spot, car_number):
    if spot in parking_lot:
        output_a_message(f"Scram! Car{car_number} is already parked at spot {spot}!")
    else:
        parking_lot[spot] = car_number
        output_a_message(f"Car {car_number} has been parked in spot {spot}")

def remove_car(spot):
    if spot in parking_lot:
        output_a_message("Car has been removed")
        remove_car = parking_lot.pop(spot) 
    else:
        output_a_message("The car has already been removed!")

print("Meow")