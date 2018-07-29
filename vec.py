class Vehicle():

	no_of_wheels = 0
	speed = 0
	weight = 0
	mileage = 0
	

	def __init__(self, no_of_wheels, speed, weight, mileage):
		self.no_of_wheels = no_of_wheels
		self.speed = speed
		self.weight = weight
		self.mileage = mileage
	

	def go_forward(self):
		print("The vehicle with {0} wheels started moving forward")

	def reverse(self):
		print("The vechicle with {0} wheels is reversing")

	def stop(self):
		print("The vechicle is stopped")

	
					
					
