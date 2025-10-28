class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
    
area_of_rectangle = Rectangle(5, 3)
perimeter_of_rectangle = Rectangle(5, 3)

print (f"Area of Rectangle: {area_of_rectangle.area()}")
print (f"Perimeter of Rectangle: {perimeter_of_rectangle.perimeter()}")