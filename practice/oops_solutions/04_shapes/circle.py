from shapes import Shapes

class Circle(Shapes):

    def get_radius(self):
        radius = (float(input("Enter the radius: ")))
        return radius

    def calculate_area(self, radius):
        area = 22/7 * radius * radius
        print(f"The area of the circle is: {area}")

circle = Circle();
radius = circle.get_radius();
circle.calculate_area(radius);