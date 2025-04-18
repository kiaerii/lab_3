#3
import math
from abc import ABC, abstractmethod

class Shape(ABC): #фигура
    @abstractmethod
    def area(self): #площадь
        pass
    
    @abstractmethod
    def perimeter(self): #периметр
        pass


class Rectangle(Shape): #прямоугольник
    def __init__(self, width, height):
        self.width=width
        self.height=height
    
    def area(self): #площадь
        return self.width * self.height #ширина*высота
    
    def perimeter(self):
        return 2*(self.width + self.height)
    
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return math.pi*self.radius**2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def __str__(self):
        return f'Circle(radius={self.radius})'


class Triangle(Shape): #треугольник
    def __init__(self, side1, side2, side3):
        self.side1=side1
        self.side2=side2
        self.side3=side3
    
    def area(self): #по формуле Герона
        s=self.perimeter()/2
        return math.sqrt(s*(s-self.side1)*(s-self.side2)*(s-self.side3)) #math.sqrt - квадратный корень
    
    def perimeter(self):
        return self.side1+self.side2+self.side3
    
    def __str__(self):
        return f'Triangle(side1={self.side1}, side2={self.side2}, side3={self.side3})'


def print_shape_info(shape):
    print(f'Фигура: {shape}')
    print(f'Площадь: {shape.area():.2f}')
    print(f'Периметр: {shape.perimeter():.2f}') #.2f - 2 знака после запятой
    print()


# Демонстрация полиморфизма
if __name__ == "__main__":
    shapes = [
        Rectangle(4, 5),
        Circle(3),
        Triangle(3, 4, 5)
    ]
    
    for shape in shapes:
        print_shape_info(shape)
