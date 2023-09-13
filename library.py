import numpy as np

class Figure:
    def __init__(self, *args:float) -> None:
        if 0 in args:
            raise ValueError("Аргументы не могут быть равны нулю.")
        for i in args:
            if not isinstance(i, float | int):
                raise TypeError("Аргументы не могут иметь тип данных, отличный от int и float.")
        for i in args:
            if i < 0:
                raise ValueError("Аргументы не могут быть отрицательными.")
        self.radius = args[0] if len(args) == 1 else 0
        self.side1, self.side2, self.side3 = sorted(args) if len(args) == 3 else [0, 0, 0]
        self.square_info = None
        if len(args) not in (1, 3):
            raise ValueError("Для создания объекта необходимо ввести 1 или 3 аргумента.")
    def square(self) -> float:
        if self.radius:
            return round(np.pi*self.radius**2, 2)
        else:
            if self.side3**2 == self.side2**2 + self.side3**2:
                self.square_info = 'Треугольник прямоугольный.'
                return self.side1 * self.side2 / 2
            self.square_info = 'Треугольник не прямоугольный.'
            p = (self.side1 + self.side2 + self.side3)/2
            return round((p * (p - self.side1) * (p - self.side2) * (p - self.side3))**0.5, 2)
    

