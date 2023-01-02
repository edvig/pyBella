# 1. Create a list which contains names of fruits. Let the length (size) of the list be 4. Print out the list!
fruits = ["morango","banana","maçã","pêra"]
print(fruits)

# 2. Add another fruit to the list. Then remove the first element of the list. Print out the first and the last element of the list.
fruits.append("kiwi")
fruits.pop(0)
print("first:",fruits[0],"last:",fruits[-1])
# 3. Use the given list, count the number of "maçã" in the list, and print out this number. 
fruits = ["morango", "maçã","banana","maçã","maçã","pêra"]
print(fruits.count("maçã"))
# 4. Use the given string and print out just the word "second". Use the string as a list.
string = "first second third"
print(string[6:12])