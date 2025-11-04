from shapes import Shapes

class Rectangle(Shapes):
    
    def get_sides(self):
        length = (float(input("Enter the length: ")))
        breadth = (float(input("Enter the breadth: ")))

        return (length, breadth)
    
    def calculate_area(self, length, breadth):
        area = length * breadth
        print (f"The area of the rectangle is: {area}")
    
rectangle = Rectangle()

length, breadth = rectangle.get_sides();
rectangle.calculate_area(length, breadth);