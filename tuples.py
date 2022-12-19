# Tuples: Tuples are ordered collections of items that can be of any data type, similar to lists. However, tuples are immutable, meaning that once they are created, their items cannot be modified. They are defined using parentheses and items are separated by commas.

# Define a tuple of integers
my_tuple = (1, 2, 3, 4, 5)

# Define a tuple of strings
my_tuple = ('apple', 'banana', 'cherry')

# Define a tuple of mixed data types
my_tuple = (1, 'apple', 3.14, True)

# Access elements in a tuple
print(my_tuple[0])  # 1
print(my_tuple[2])  # 3.14

# Modifying elements in a tuple is not allowed
# my_tuple[1] = 'orange'  # This will raise a TypeError

# Add elements to a tuple is not allowed
# my_tuple.append('mango')  # This will raise an AttributeError

# Remove elements from a tuple is not allowed
# my_tuple.remove(3.14)  # This will raise an AttributeError
