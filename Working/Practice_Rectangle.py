class Rectangle(object):
    def __init__(self):
        self.width = 0
        self.height = 0


def rectangle_area(rectangular_shape):
    return (rectangular_shape.width * rectangular_shape.height)


def main():
    rectangle1 = Rectangle
    rectangle1.width = int(input("insert width: "))
    rectangle1.height = int(input("insert height: "))

    print("The rectangle width is "+str(rectangle1.width)+", and the height is "+str(rectangle1.height)+"")

    rectangle_area(rectangle1)

main()
