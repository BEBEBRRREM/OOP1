#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

class Triangle:

    def __init__(self, a=1, b=1, c=1):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
        self.angles = self.calculate_angles()


    def read(self):
        self.a = int(input("Сторона AB треугильника ABC = "))
        self.b = int(input("Сторона AC треугильника ABC = "))
        self.c = int(input("Сторона BC треугильника ABC = "))
        self.angles = self.calculate_angles()
        
        if self.a < 1 and self.b < 1 and self.c < 1:
            raise ValueError("Некорректные введённые данные, стороны и углы должны быть больше 0")
        

    def is_right_triangle(self):
        # Проверка на прямоугольный треугольник
        return (math.isclose(self.a**2 + self.b**2, self.c**2) or
                math.isclose(self.a**2 + self.c**2, self.b**2) or
                math.isclose(self.b**2 + self.c**2, self.a**2))
    

    def type(self):
        if self.a == self.b == self.c:
            return "равносторонний"
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return "равнобедренный"
        elif self.is_right_triangle():
            return "прямоугольный"
        else:
            return "разносторонний"
        
              
    def calculate_angles(self):
        # Используем закон косинусов для вычисления углов
        A = math.degrees(math.acos((self.b**2 + self.c**2 - self.a**2) / (2 * self.b * self.c)))
        B = math.degrees(math.acos((self.a**2 + self.c**2 - self.b**2) / (2 * self.a * self.c)))
        C = 180 - A - B
        return (A, B, C)


    def FindP(self):
        return self.b + self.a + self.c
    

    def FindS(self):
        S = self.FindP() / 2
        return math.sqrt(S * (S - self.a) * (S - self.b) * (S - self.c))
    

    def height(self, side):
        # Высота вычисляется как (2 * площадь) / основание
        return (2 * self.FindS()) / side
    

    def display(self):
        print(f"Углы: {self.angles}")
        print(f"Стороны АВ = {self.a} АС = {self.b} ВС = {self.c}")
        print(f"S = {self.FindS()}")
        print(f"P = {self.FindP()}")
        print(f"Type = {self.type()}")
        print(f"Высота относительно стороны a: {self.height(self.a)}")
        print(f"Высота относительно стороны b: {self.height(self.b)}")
        print(f"Высота относительно стороны c: {self.height(self.c)}")


if __name__ == '__main__':
    Tria = Triangle()
    Tria.read()
    Tria.display()

