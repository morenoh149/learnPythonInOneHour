# We use the "class" operator to get a class
class Human:

    # A class attribute. It is shared by all instances of this class
    species = "H. sapiens"

    # Basic initializer, this is called when this class is instantiated.
    # Note that the double leading and trailing underscores denote objects
    # or attributes that are used by python but that live in user-controlled
    # namespaces. Methods(or objects or attributes) like: __init__, __str__,
    # __repr__ etc. are called magic methods (or sometimes called dunder methods)
    # You should not invent such names on your own.
    def __init__(self, name):
        # Assign the argument to the instance's name attribute
        self.name = name

        # Initialize property
        self.age = 0

    # An instance method. All methods take "self" as the first argument
    def say(self, msg):
        print ("{name}: {message}".format(name=self.name, message=msg))

    # Another instance method
    def sing(self):
        return 'yo... yo... microphone check... one two... one two...'

    # A class method is shared among all instances
    # They are called with the calling class as the first argument
    @classmethod
    def get_species(cls):
        return cls.species

    # A static method is called without a class or instance reference
    @staticmethod
    def grunt():
        return "*grunt*"

    # A property is just like a getter.
    # It turns the method age() into an read-only attribute
    # of the same name.
    @property
    def age(self):
        return self._age

    # This allows the property to be set
    @age.setter
    def age(self, age):
        self._age = age

    # This allows the property to be deleted
    @age.deleter
    def age(self):
        del self._age


# When a Python interpreter reads a source file it executes all its code.
# This __name__ check makes sure this code block is only executed when this
# module is the main program.
if __name__ == '__main__':
    # Instantiate a class
    i = Human(name="Ian")
    i.say("hi")                     # "Ian: hi"
    j = Human("Joel")
    j.say("hello")                  # "Joel: hello"
    # i and j are instances of type Human, or in other words: they are Human objects

    # Call our class method
    i.say(i.get_species())          # "Ian: H. sapiens"
    # Change the shared attribute
    Human.species = "H. neanderthalensis"
    i.say(i.get_species())          # => "Ian: H. neanderthalensis"
    j.say(j.get_species())          # => "Joel: H. neanderthalensis"

    # Call the static method
    print(Human.grunt())            # => "*grunt*"
    print(i.grunt())                # => "*grunt*"

    # Update the property for this instance
    i.age = 42
    # Get the property
    i.say(i.age)                    # => 42
    j.say(j.age)                    # => 0
    # Delete the property
    del i.age
    # i.age                         # => this would raise an AttributeError

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

# from human import Human
# from bat import Bat

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

	print(sup.get_species())  # calls parent method but with own class attribute  # 'Superhero'

	print(sup.sing())  		  # overloading

	sup.say('I agree') 		  # calls method on human, inheritance order matters

	print(sup.sonar())

	sup.age = 100
	print(sup.age)

	print('Can I fly? ' + str(sup.fly))
