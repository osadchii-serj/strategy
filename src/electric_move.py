from interface import IMovable


class ElectricMove(IMovable):

    def move(self):
        print("Перемещение на электричестве")
