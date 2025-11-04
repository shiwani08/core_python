from vehicle import Vehicle

class Bike(Vehicle):

    def start_engine(self):
        print("Bike is starting")

    def stop_engine(self):
        print("Bike is stopping")

bike = Bike()
bike.start_engine()
bike.stop_engine()