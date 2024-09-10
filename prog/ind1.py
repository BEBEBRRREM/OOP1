#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Pair:
    def __init__(self, first, second):
        # Проверка корректности значений
        if not isinstance(first, int) or first <= 0 or first not in [1, 2, 5, 10, 50, 100, 500, 1000, 5000]:
            raise ValueError("Поле 'first' должно быть положительным целым числом из заданного набора.")
        if not isinstance(second, int) or second <= 0:
            raise ValueError("Поле 'second' должно быть положительным целым числом.")
        
        self.first = first
        self.second = second

    def read(self):
        self.first = int(input("Введите номинал купюры (1, 2, 5, 10, 50, 100, 500, 1000, 5000): "))
        self.second = int(input("Введите количество купюр: "))
        # Проверка корректности введенных значений
        if self.first not in [1, 2, 5, 10, 50, 100, 500, 1000, 5000] or self.first <= 0:
            raise ValueError("Некорректный номинал купюры.")
        if self.second <= 0:
            raise ValueError("Количество купюр должно быть положительным числом.")

    def display(self):
        print(f"Номинал купюры: {self.first}, Количество купюр: {self.second}")

    def summa(self):
        return self.first * self.second

def make_pair(first, second):
    try:
        return Pair(first, second)
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    # Реализация вводы данных из кода
    pair = make_pair(5000, 67)
    pair.display()
    print(f"Общая сумма: {pair.summa()}")
    # Реализация с вводом текста
    pairs = Pair(1,1)
    pairs.read()
    pairs.display()
    print(f"Общая сумма: {pairs.summa()}")
