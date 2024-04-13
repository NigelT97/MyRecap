#!/usr/bin/python3

class square:
    def __init__(self, size):
        self.__size = size

    
    def size(self):
        return (self.__size)

    def area(self):
        area_value = self.__size * self.__size
        return area_value
    
    def my_print(self):
        square_value = self.__size
        square_shape = ""
        for value in range(0, square_value):
            for value2 in range(0, square_value):
                square_shape = f"{square_shape}#"
            print(square_shape)
            square_shape = ""

class rectangle:
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
    
    def height(self):
        return self.__height
    
    def width(self):
        return self.__width
    
    def area(self):
        area = self.__height * self.__width
        return area
    
    def perimeter(self): 
        perimeter = 2 * (self.__width + self.__height)
        return perimeter
    
    