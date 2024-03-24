class Person:
    name = "John"
    age = 36  # Add the 'age' attribute
    country = "Norway"

# Create an instance of the Person class
person_instance = Person()

# Remove the 'age' attribute (just for demonstration)
delattr(person_instance, 'age') # tome doji chow aita comment kroa dakta paro

# Now let's access the 'age' attribute
print(person_instance.age)  # Output: 36

