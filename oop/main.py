from Car import Car
from ElectricCar import ElectricCar

car = Car("Toyota", "Corolla")
ev = ElectricCar("Tesla", "Model S", "345")

car.start()
car.stop()

ev.start()
ev.stop()
ev.charge()
