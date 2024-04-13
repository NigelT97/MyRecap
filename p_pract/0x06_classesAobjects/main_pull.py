#!/usr/bin/python3

import square_class

if __name__ == "__main__":
    side = 5
    my_square = square_class.square(side)




    print(type(my_square))
    print(my_square.__dict__)

    area = my_square.area()
    print(f"Area of {my_square.size()}: {area}")

    my_square.my_print()

    width, height = 17, 20
    my_rectangle = square_class.rectangle(width, height)
    print(type(my_rectangle))
    print(my_rectangle.__dict__)

    perimeter = my_rectangle.perimeter()
    area = my_rectangle.area()

    print(f"Width: {my_rectangle.width()} & Height: {my_rectangle.height()}\nPerimeter: {perimeter} & Area: {area}")
