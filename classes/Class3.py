# Explicitly cast string into list
stringVariable = "Bella is beautiful"
print(stringVariable)

listOfChars = list(stringVariable)
print(listOfChars)

print(stringVariable[0])
print(listOfChars[0])

# 3rd class
# Getting the last element of a list
print("Lets print the last element of the list:")
exampleList = [1,2,3,4]
print(exampleList[-1])

# How to check if an element is in the list?
listOfFruits = ["jaboticaba", "melão", "melancia", "uva"]
if(listOfFruits.count("uva") > 0):
    print("in the list")
else:
    print("not in the list")

if("melancia" in listOfFruits):
    print("in the list")
else:
    print("not in the list")

# Lets add an item if its NOT already in the list
# Get a new fruit name from a the console
print("Tell me a new fruit and if its not in the list im gonna add it to it:")
newItem = "maca"
print("Your input is:",newItem)
if (newItem not in listOfFruits):
    listOfFruits.append(newItem)
print("The updated list is",listOfFruits)

# Lets sort a list of fruits by their names from A to Z.
unorderedList = ["banana", "grapes", "apple", "cherry"]
print("Lets sort some words alphabetically")
print("Before sorting",unorderedList)
unorderedList.sort()
print("After sorting",unorderedList)

# Lets sort a list of fruits by their names from Z to A.
unorderedList = ["banana", "grapes", "apple", "cherry"]
print("Lets sort some words alphabetically reverse")
print("Before sorting",unorderedList)
unorderedList.sort(reverse=True)
print("After sorting",unorderedList)

# Lets sort a list of numbers from smallest to the largest
print("Lets sort some numbers from smallest to the largest")
unorderedList = [4,3,5,1,4,3]
print("Before sorting",unorderedList)
unorderedList.sort()
print("After sorting",unorderedList)

# Lets sort some numbers from largest to the smallest
print("Lets sort some numbers from largest to the smallest")
unorderedList = [4,3,5,1,4,3]
print("Before sorting",unorderedList)
unorderedList.sort(reverse=True)
print("After sorting",unorderedList)

# sort and reverse in 2 steps
print("-----------------------------")
unorderedList = [4,3,5,1,4,3]
print(unorderedList)
unorderedList.sort()
unorderedList.reverse()
print(unorderedList)

# <listName>.sort(reverse=True)  is the exact same as <listName>.sort()  AND <listName>.reverse()   together

# We already know how to get one element of the list: <listName>[x]
listOfFruits = ["jaboticaba", "melão", "melancia", "uva"]
print("Lets print the whole list of fruits:",listOfFruits)
firstFruit = listOfFruits[0]
print("Lets print just the first item:", listOfFruits[0])

# if we want to show all the elements 1by1 we would need to print each 1by1, like listOfFruits[0], listOfFruits[1], ....
# its not scaleable, and would take a long time to write it
# LOOPS
# for
# for <item> in <list>:

print("Lets print every fruit one by one:")
for fruit in listOfFruits:
    print(fruit)

# Lets print out the fruits which starts with "m"
print("Lets print out only the fruits that starts with 'm'")
for fruit in listOfFruits:
    if (fruit.startswith("m")):
        print(fruit)

# for loops in a different way
# for x in range(from, to, steps)

print("Lets print the number from 0 to 9")
for x in range(0, 10, 1):
    print(x)

# Lets fill a list with the word "Apple" + 1-9 numbers
print("for loop example with an empty list")
listOfNumbers = []
for x in range(0, 10, 1):
    newItem = "Apple"+str(x)
    listOfNumbers.append(newItem)

print(listOfNumbers)

# There's a shorter way to make a list with looping
print("the shorter way to create a list from looping")
bigList = ["apple"+str(x) for x in range(1000)]

# Lets say you have a BIG list of numbers and you just want some specific ones in a new list (the ones that end with '15')
# so you loop through the original list and only add the ones that ends with '15' to the new list
newList=[]
for item in bigList:
    if(item.endswith("15")):
        newList.append(item)
print(newList)

# This is a more complex exercise for changing all the bananas to laranja in a list
print("This is a more complex exercise for changing all the bananas to laranja in a list")
fruits = ["banana","graviola","banana","acerola","pera","banana"]

# This is the one-line solution
newFruits = ["laranja" if(fruit == "banana") else fruit for fruit in fruits]

# This delivers the same result, but with regular for loop
anotherNewFruits = []
for fruit in fruits:
    if(fruit == "banana"):
        anotherNewFruits.append("laranja")
    else:
        anotherNewFruits.append(fruit)

print("original:",fruits)
print("one-line method:",newFruits)
print("regular for loop:",anotherNewFruits)


# How to change items in a list
# You can redifine any item of the list by assigning another value to the indexed item.
print("Lets change the first item of the following list to 'laranja':")
fruits = ["banana","graviola","banana","acerola","pera","banana"]
print(fruits)
print(fruits[0])
fruits[0] = "laranja"
print(fruits)
print(fruits[0])

# lets use regular for loop (with range) and print each items of the list
for fruit in fruits:
    print(fruit)

numberOfFruits = len(fruits)
for x in range(numberOfFruits):
    print(fruits[x])

