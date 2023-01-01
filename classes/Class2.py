# LISTS
# list is a variable type
integerList = [1,2,3] # list of integers
stringsList = ["morango", "cafe", "banana"] # list of strings
mixedList = ["maçã", 1, "pêra", True] # list of mixed variable types

# Lets print the list
print("Lets print a list:")
print(stringsList)

# Lets print the type of the list
print(type(stringsList))

# the values stored in a list are called elements.
# We can get elements from a list by indexing:
# INDEXING STARTS FROM 0. ALWAYS
firstElementOfTheList = stringsList[0]
print("Lets print the first element of the list:")
print(firstElementOfTheList)

# You can use built-in functions to make operations on the list
# To add another element/item to a list you use <variableName>.append (The new element will be the last element - It is being appended to the end of list.):
print("Lets add another item to the list and print the whole list:")
stringsList.append("chocolate")
print(stringsList)

# To get the size/number of elements of a list, you use the len() function:
print("Lets print the number of elements of the list:")
sizeOfTheList = len(stringsList)
print(sizeOfTheList)

# You can have duplicate values in a list:
print("Lets add another morango to the list:")
stringsList.append("morango")
print(stringsList)

# You can count the number of occurancies using the count() function:
print("Lets count the number morangos in the list:")
numberOfMorangos = stringsList.count("morango")
print(numberOfMorangos)

# How to get the last element of a list:
# Combine two things: indexing of a list and the length/size of a list
print("Lets get the last element of the list:")
sizeOfTheList = len(stringsList)
indexOfTheLastElement = sizeOfTheList - 1
print("Size:",sizeOfTheList)
print("Last index:",indexOfTheLastElement)
lastElementOfTheList = stringsList[indexOfTheLastElement]
print("Last element:",lastElementOfTheList)

# Add multiple items (another list) to an existing list with "extend"
print("Lets add multiple elements to a list:")
stringsList.extend(["tea","abacaxi"])
print(stringsList)
# Pop out an element of a list (pop = get an element and remove from the list)
# by default it pops the last element of the list but you can always define the index as a parameter: <listName>.pop(1)
print("Lets pop the last element of the list:")
print(stringsList.pop())
print(stringsList)

# To remove an item from a list, use remove
print("Lets remove chocolate from the list:")
stringsList.remove("chocolate")
print(stringsList)

# Lets remove the first occurrence of "morango"
print("Lets remove morango from the list")
stringsList.remove("morango")
print(stringsList)

# Lets reverse the order of the elements
print("Lets reverse the order of the list")
print(integerList)
integerList.reverse()
print(integerList)

# Get just a part of the list
print(stringsList)
print("Lets get the first 3 elements of the list:")
print(stringsList[0:3])
print("Lets get all elements except the first and the last")
lastIndex = len(stringsList) - 1
print(stringsList[1:lastIndex])

# Strings
stringVariable = "some text"

# Strings are made up of characters.
# a string = a list of chars
print(stringVariable[0:4])
print(stringVariable[:4])
print(stringVariable[5:])