# Creating an empty list called my_list
my_list = []

# You can also create an empty list using the list() constructor
# my_list = list()

print("Empty list created:", my_list)
print("Type of my_list:", type(my_list))
print("Length of my_list:", len(my_list))

# Appending elements to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print("\nAfter appending elements:", my_list)
print("Length of my_list after appending:", len(my_list))

# Inserting 15 at the second position (index 1)
my_list.insert(1, 15)

print("\nAfter inserting 15 at second position:", my_list)
print("Length of my_list after inserting:", len(my_list))

# Extending my_list with another list [50, 60, 70]
my_list.extend([50, 60, 70])

print("\nAfter extending with [50, 60, 70]:", my_list)
print("Length of my_list after extending:", len(my_list))

# Removing the last element from my_list
removed_element = my_list.pop()

print("\nAfter removing the last element:", my_list)
print("Removed element:", removed_element)
print("Length of my_list after removing:", len(my_list))

# Sorting my_list in ascending order
my_list.sort()

print("\nAfter sorting in ascending order:", my_list)
print("Length of my_list after sorting:", len(my_list))

# Finding and printing the index of value 30 in my_list
index_of_30 = my_list.index(30)

print("\nIndex of value 30:", index_of_30)
print("Value at index", index_of_30, ":", my_list[index_of_30]) 