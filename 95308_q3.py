class fleet:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"vehicle with Registration number {vehicle.registration_number} added to fleet.")

    def display_all_vehicles(self):
        if not self.vehicles:
            print("No vehicles in the fleet.")
            return
        for vehicle in self.vehicles:
            print(vehicle.display_info())
        
    def search_vehicle_by_registration(self, registration_number):
        for vehicle in self.vehicles:
            if vehicle.registration_number == registration_number:
                print(vehicle.display_info())
                return
        print(f"vehicle with registration Number {registration_number} not found.")

        # Demonstrating the functionalities

        def main():
             #create an instance of the fleet
            fleet = fleet()
             # add vehicles to the fleet
        car = car("ABC123","Toyota","Prado",5)
        Truck = Truck("DEF432","Volvo","FH",20)
        Motorcycle = Motorcycle("GHI456","Yamaha","YZF-R1",988)

        fleet.add_vehicle(car)
        fleet.add_vehicle(Truck)
        fleet.add_vehicle(Motorcycle)

        #Display all the vehicles

        print("\nAll Vehicles in the fleet:")
        fleet.display_all_vehicles()

        #search for a vehicle by registration number

        print("\nSearch for a vehicle with registration number 'DEF432':")
        fleet.search_vehicle_by_registration("DEF432")

        #search for a non-existent vehicle

        print("\nSearch for  vehicle with registration number 'XYZ234':")
        fleet.search_vehicle_by_registration('XYZ234')

    
            

