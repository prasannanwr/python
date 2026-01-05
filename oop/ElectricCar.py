from Car import Car

class ElectricCar(Car):
	
	def __init__(self, brand, model, battery):
		super().__init__(brand, model)
		self.battery = battery

	def charge(self):
		print(f"Charging {self.brand} {self.model}")

