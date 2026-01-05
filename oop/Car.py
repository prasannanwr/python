class Car:
	def __init__(self, brand, model):
		self.brand = brand
		self.model = model
		self._is_running = False #protected attribute
		self.__engine_status = False #private
	
	def start(self):
		self._is_running = True
		print(f"{self.brand} {self.model} started")
	
	def stop(self):
		self._is_running = False
		print(f"{self.brand} {self.model} stopped")

