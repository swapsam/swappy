from vec import Vehicle

class truck(Vehicle):
	max_load = 0
	speedlimit = 0 

	def __init__(self, max_load, speedlimit):
		self.max_load = max_load
		self.speedlimit = speedlimit
		super().__init__(no_of_wheels, speed, weight, mileage)

	def load(self):
		print("The truck is loaded")

	def unload(self):
		print("The truck is nloaded")


