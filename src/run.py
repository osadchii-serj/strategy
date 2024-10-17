from electric_move import ElectricMove
from petrol_move import PetrolMove
from car import Car

if __name__ == "__main__":

    car = Car("Volvo", PetrolMove())
    car.move()

    car.set_strategy(ElectricMove())
    car.move()
