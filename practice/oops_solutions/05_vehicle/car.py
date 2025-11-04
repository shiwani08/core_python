from vehicle import Vehicle

class Car(Vehicle):

    def start_engine(self):
        print("Car is starting")

    def stop_engine(self):
        print("Car is stopping")

car = Car()
car.start_engine()
car.stop_engine()