from vehicle import Vehicle

class Truck(Vehicle):

    def start_engine(self):
        print("Truck is starting")

    def stop_engine(self):
        print("Truck is stopping")

truck = Truck()
truck.start_engine()
truck.stop_engine()