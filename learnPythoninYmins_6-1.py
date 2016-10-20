# Multiple Inheritance

class Bat:
	species = 'Baty'

	def __init__(self, can_fly=True):
		self.fly = can_fly

	# instance methods - always receive the current class as the 1st arg
	def say(self, msg):
		msg = '... ... ...'
		return msg

	def sonar(self):
		return '))) ... ((('

if __name__ == '__main__':
	b = Bat()
	print(b.say('hello'))  # '... ... ...' as msg is overidden in say()
	print(b.fly) 		   # 'True'

from human import Human
from bat import Bat

class Batman(Human, Bat):

	species = 'Superhero'

	def __init__(self, *args, **kwargs):
		# super(Batman, self).__init__(*args, **kwargs)  # doesn't work for multiple inheritance
		Human.__init__(self, 'anonymous', *args, **kwargs)
		Bat.__init__(self, *args, can_fly=False, **kwargs)

		self.name = 'Sad Affleck'

	def sing(self):
		return 'nan nan nan nan nan nan batman!'

if __name__ == '__main__':
	sup = Batman()

    # type checks
	if isinstance(sup, Human):
		print('I am human')
	if isinstance(sup, Bat):
		print('I am bat')
	if type(sup) is Batman:
		print('I am Batman')

	print(Batman.__mro__)
