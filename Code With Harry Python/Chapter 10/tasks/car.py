class Vehicle:
    def __init__(self, brand, model, wheels=4):
        self.brand = brand
        self.model = model
        self.wheels = wheels
    
    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Wheels: {self.wheels}")

class Car(Vehicle):
    def __init__(self, brand, model, fuel):
        super().__init__(brand, model)
        self.fuel = fuel

    def info(self):
        super().info()
        print(f"Fuel Type: {self.fuel}")

class Electric:
    def __init__(self, battery):
        self.battery = battery

    def charge(self):
        print(f"Charging... Battery at {self.battery}%")

class Tesla(Car, Electric):
    def __init__(self, model, battery):
        Car.__init__(self, "Tesla", model, "Electric")
        Electric.__init__(self, battery)

    def info(self):
        super().info()
        print(f"Battery: {self.battery}%")
    
    def honk(self):
        print("🎵 Tesla Honk: Dooo Dooo! 🔋⚡")

# Create objects
v = Vehicle("Honda", "Civic")
c = Car("Toyota", "Corolla", "Petrol")
e = Electric(98)
t = Tesla("Model X", 85)

# Call methods
print("\n--- Vehicle Info ---")
v.info()

print("\n--- Car Info ---")
c.info()

print("\n--- Electric Charging ---")
e.charge()

print("\n--- Tesla Info ---")
t.info()
t.charge()
t.honk()
