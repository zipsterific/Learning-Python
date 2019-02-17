#!/usr/bin/env python3

def add():
    return 2 + 3

def multiply():
    return 2 * 3

def cube():
    return 2 ** 3

def sqauare_area():
    side_lenght = 5
    area = side_length **2
    return area

def sqauare_area(side_length=5): #set a default value
    area = side_length **2
    return area

def rectangle_perimeter(width, height):
    perimeter = width * 2 + height * 2
    return perimeter
