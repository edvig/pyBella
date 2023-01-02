import random


# Initializing variables, modifying their values.
from operator import truediv


print("Initializing variables, modifying their values.")
brazil = 0
hungary = 0
print("The result in the beginning is Brazil "+str(brazil)+" - "+str(hungary)+" Hungary")
brazil = 1
print("Then Brazil scored a goal, Brazil "+str(brazil)+" - "+str(hungary)+" Hungary")
brazil += 1
print("Then Brazil scored another goal, Brazil "+str(brazil)+" - "+str(hungary)+" Hungary")
brazil -= 1
print("Then the referee disallowed a goal, Brazil "+str(brazil)+" - "+str(hungary)+" Hungary")
print("Final whistle, the match finished")
if(brazil > hungary):
    print("Brazil won")
print("-------------------------------------------")

# Basic variable types
print()
print("Basic variable types")
print("-------------------------------------------")
integerVariable = 1 
print(integerVariable)
print(type(integerVariable))

floatVariable = 3
print(floatVariable)
print(type(floatVariable))

stringVariable = "some text"
print(stringVariable)
print(type(stringVariable))

boolVariable = True
print(boolVariable)
print(type(boolVariable))

modifiedType = str(1) + " = one"
print(modifiedType)
print(type(modifiedType))

noneType = None 
print(noneType)
print(type(noneType))

# Practice with variable types
practiceFirst = 4==3
print(practiceFirst)
print(type(practiceFirst))

# Random values
# first you import the "random" package with "import random" (usually in the beginning of the file)
print("Random values")
print("-------------------------------------------")
start = 0
stop = 10
steps = 1
randomVariable = random.randrange(start, stop, steps)
print("The random number:",randomVariable)
#print(type(randomVariable))

#print(10/2)
#print(10%2)
#print(10%3)

if(randomVariable %2 == 0):
    print("The random number is even.")
else:
    print("The random number is odd.")