 #  WORKING WITH LISTS
#  matlab hame list par kaam karna hai

list1 = ["samrat", "vishal", "prasik", "abhay"]
for k in list1:
    print(k)
print()   # space

list2 = ["sam", "ram", "sunny"]
for k in list2:
    print(k.title()+ ".. how are you ? ")
    print(" I Am fine ..."+ k.title())
print()   # space

# USING RANGE() TO MAKE A LIST OF NUMBERS
# the range() function is used to genrate a sequence of numbers

# range directly list nhi deta use list me convert karne ke liye list() use karte hai

numbers = list(range(1, 11))
print(numbers)
print()   # space

# how to creat even numbers ?

# start = 2
# stop = 11
# step = 2

even_numbers = list(range(2, 11, 2))  # akhri me jo 2 hai insaltion ka kaam karti hai
print(even_numbers)
print()  # space

# SQUARES
# ek khali empty banaya squares name ka issme kuch nhi hai
# square name ka varibles liya usse me k**2
# append ka use kiya hai uska use last elements ko add karna hota hai ussne squares
# list ke andaar wo elemnts dale baad me usse print kiya


squares = []  # this is empty list
for k in range(1, 11):
    square = k**2
    squares.append(square)

print(squares)
print()  # space

cubes = []
for j in range(1, 11):
    cube = j**3
    cubes.append(cube)
print(cubes)
print() # space

#  SLICING A LIST

list = [23, 45, 67, 23, 12]
print(list[0:4])      # AB 0 index se print honga to 4 index ke biche se
print()   # space

list2 = ["smrat", "happyness", "ghsot", "names", "kings"]
print(list2[0:])     # AB 0 index se print honga to pure index tak print honga
print(list2[3:])
print(list2[0:-3])
print()   # space

# LOOPING THROUGH A SLICE (SLICE PAR LOOP CHALANA)

# players[:3] ka matlab: Python zero index se
# shuru karega aur index 3 se pahle (yaani index 0, 1, aur 2)
# tak ke items uthayega

list3 = ["smrat", "happyness", "ghsot", "names", "kings"]

for k in list3[:3]:   # mene zero likha nhi bhi chalta
    print(k.title())

print() # space


# TUPLES
# IT IS A IMMUTABLE AND IT IS USED TO STORE THE MULTIPLE VALUE IN LIST
# AND IT CANNOT BE CHANGE THE VALUE OF LIST
# # Tuple ko ( ) parentheses ke andar likha jata hai

# List vs Tuple ka Farq:
# List: Square brackets [ ] use karti hai. (Badli ja sakti hai)
# Tuple: Parentheses ( ) use karta hai. (Badli nahi ja sakti)

speed = (200, 300, 56)
print(speed[0:3])
print()   # space

# 1. Purana tuple
dimensions = (200, 50)
print("Original dimensions:")
print(dimensions)

# 2. Naya tuple usi naam ke variable me daal diya
dimensions = (400, 100)  # ✅ Yeh valid hai!
print("Modified dimensions:")
print(dimensions)
print()  # space


