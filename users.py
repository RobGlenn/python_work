# users.py

class User(object):
	"""Create User Class"""
	def __init__(self, name, age, country):
		super(User, self).__init__()
		self.name = name
		self.age = age
		self.country = country

	def describe_user(self):
		print('Name:' + self.name.title() + '   Age:' + str(self.age) + '   Country:' + self.country.title() )

	def greet_user(self):
		print('Welcome ' + self.name.title() + '. Nice to meet you.\n')

user = User('rob glenn', 18, 'canada')
user.describe_user()
user.greet_user()

user = User('david wells', 24, 'Brazil')
user.describe_user()
user.greet_user()

user = User('cindy bellows', 26, 'Israel')
user.describe_user()
user.greet_user()

