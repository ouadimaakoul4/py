class Dog:
    # Class attribute
    attr1 = "big dog"

    # Constructor method
    def __init__(self, name):
        self.name = name

    # Instance method
    def bark(self):
        print("Woof!")
# End class Dog


# instance method
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))

# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))

# Calling instance methods
Rodger.bark()
Tommy.bark()
