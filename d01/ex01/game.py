class GotCharacter:

	house_words = ''

	def __init__(self, first_name, is_alive=True):
		assert first_name and isinstance(first_name, str),\
			"Please enter a name of type str"
		assert isinstance(is_alive, bool), "Please enter a alive of type bool"
		self.first_name = first_name
		self.is_alive = is_alive

	def die(self):
		if self.is_alive == True:
			self.is_alive = False

	def print_house_words(self):
		print(self.house_words)


class Stark(GotCharacter):
	"""A class representing the Stark family.\
	Or when bad things happen to good people."""

	def __init__(self, first_name=None, is_alive=True):
		super().__init__(first_name=first_name, is_alive=is_alive)
		self.family_name = "Stark"
		self.house_words = "Winter is Coming"


class Targaryen(GotCharacter):
	"""A class representing the Targaryen family.\
	Or when bad things happen to good people."""

	def __init__(self, first_name=None, is_alive=True):
		super().__init__(first_name=first_name, is_alive=is_alive)
		self.family_name = "Targaryen"
		self.house_words = "Fire & Blood"
