from shapes import Shapes

class Triangle(Shapes):
    
    def get_sides(self):
        base = (float(input("Enter the base: ")))
        height = (float(input("Enter the height: ")))

        return (base, height)
    
    def calculate_area(self, base, height):
        area = (base * height) / 2
        print (f"The area of the Triangle is: {area}")
    
triangle = Triangle()

base, height = triangle.get_sides();
triangle.calculate_area(base, height);