#!/usr/bin/env python3

# Import our classes
from lib.dog import Dog
from lib.person import Person

# Test Dog class
print("Testing Dog class:")
fido = Dog()
print("Dog barking:")
fido.bark()
print("Dog sitting:")
fido.sit()

print("\n" + "="*30 + "\n")

# Test Person class
print("Testing Person class:")
guido = Person()
print("Person talking:")
guido.talk()
print("Person walking:")
guido.walk()
