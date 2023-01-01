import random

# 1. Print out "Hello World" on the console
print("Hello World!")
# 2. Create a variable and name it however you like, assign your name as the value of this variable
# variableName = variableValue
bella = "Bella"
# 3. Create a "rolling dice": Make a variable that chooses a random value, like a rolling dice. Print out its value on the console.
start = 1
stop = 6
dice = random.randrange(start,stop)
print(dice)
# 4. Create a variable that chooses a value between 1 and 10. If the value is odd print "Odd", if its even, print "Even".
randomVariable = random.randrange(1,10,1)
if(randomVariable % 2 == 1):
    print("The number is odd.")
else:
    print("The number is even.")


asd = 1 == 1
print(asd)
print(type(asd))