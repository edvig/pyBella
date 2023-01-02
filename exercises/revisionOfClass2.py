# 1. Create a list which contains names of fruits. Let the length (size) of the list be 4. Print out the list!
fruitList = ["jaboticaba", "melão", "melancia", "uva."]
print (fruitList)
# 2. Add another fruit to the list. Then remove the first element of the list. Print out the first and the last element of the list.
fruitList.append ("goiaba")
fruitList.pop(0)
print (fruitList)
print(fruitList[0])
print(fruitList[-1])
# 3. Use the given list, count the number of "maçã" in the list, and print out this number. 
fruits = ["morango","maçã","banana","maçã","maçã","pêra"]
print (fruits)
fruits = fruits.count ("maçã")
print ("the number of maçãs is:",fruits) 
# 4. Use the given string and print out just the word "second". Use the string as a list.
string1 = "first second third"
#string1.pop (1)
print(string1[6:12])
print(string1)