list = [1,2,3,4,5,6,7,8,9,10,11]

list2 = [12,13,14]

# Adds an object onto the end of the list
list.extend(list2)

# Inserts a value/object/element at (index, value)
list.insert(5,12)

# Inserts a value at [index]
list[5] = list[5] / 2

# Removes elements by their index
del list[5:7]

# Removes elements by their value
list.remove(9) # Produces ValueError if value is not in the list

# Reverses the elements in a list
list.reverse()


print(list)