# Lists: Lists are ordered collections of items that can be of any data type. They are defined using square brackets and items are separated by commas.

# Define a list of integers
my_list = [1, 2, 3, 4, 5]

# Define a list of strings
my_list = ['apple', 'banana', 'cherry']

# Define a list of mixed data types
my_list = [1, 'apple', 3.14, True]

# Access elements in a list
print(my_list[0])  # 1
print(my_list[2])  # 3.14

# Modify elements in a list
my_list[1] = 'orange'
print(my_list)  # [1, 'orange', 3.14, True]

# Add elements to a list
my_list.append('mango')
print(my_list)  # [1, 'orange', 3.14, True, 'mango']

# Remove elements from a list
my_list.remove(3.14)
print(my_list)  # [1, 'orange', True, 'mango']