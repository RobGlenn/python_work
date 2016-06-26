# restaurant.py

class Restaurant(object):
	"""Declare Restaurant Class"""
	def __init__(self, name, cuisine):
		super(Restaurant, self).__init__()
		self.name  = name
		self.cuisine = cuisine

	# print description of restaurant
	def describe_restaurant(self):
		print('The restaurant\'s name is ' + self.name.title()+ '.')
		print('They serve ' + self.cuisine.title() + ' food.')

	# Tell the user the restaurant is now open
	def open_restaurant(self):
		print(self.name.title()+ ' is now open.')




restaurant = Restaurant('mings', 'chinese')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant = Restaurant('luigi', 'italian')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant = Restaurant('Zorba', 'Greek')
restaurant.describe_restaurant()
restaurant.open_restaurant()

