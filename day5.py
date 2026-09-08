
# INSERTING ELEMNETS INTO A LIST
# List me naya element dalna: insert() method
# Agar aapko apni list me kisi specific jagah (position) par koi naya item add
# karna hoto isska use hota hai

list1 = [879, 56, 3, 23, 78]
list1.insert(0, 900)  # ya pe 0 index par 900 insert ho gaya hai
print(list1)
print()  # space


list2 = ["sam", "abhimanu", "vishal", "vaibhav"]
print(list2)

list2.insert(2, "kumal")
print(list2)
print()  # space

# REMOVING ELEMNTS FROM A LISTS
# LIST ME ke elemts ko delete karne ke liye isska use hota hai
# del ( list name [index number ])

list3 = ["joker", "doge", "right", "quit"]
del list3[0]
print(list3)

del list3[2]
print(list3)

list3.append("elephathe")  # iss me biche se naya elements dala hai
print(list3)
print() # space

# REMOVING A ITEMS USING THE POP() METHOD .
# pop() method list me se kisi element ko remove bhi karta hai
# aur return bhi karta hai, taaki us removed item ko baad me use kiya ja sake.

books = ["english", "physics", "chemistry", "maths", "biology"]
pop_books = books.pop()  # isse list ka akhri elements hat gaya hai ..
print(books)
print(pop_books)  # mene iss elemnts ko hataya wo dikh jayega

print() # space

cars = ["supercars", "motercycle", "royalroyal" ]
pop_cars = cars.pop()
print(cars)
print(pop_cars)
print()  # space


  #  SORTING A LIST PERMANENTLY WITH THE SORT() METHOD
# sort() method aur sorted()
# function. Dono ka kaam list ko alphabetical order (A to Z) me lagana hai,

l2 = ["fsdf", "asd", "abc", "abcd"]
l2.sort()  # sort() method ka use alphabetical order me lagana hota hai
print(l2)
print() #   space


l3 = [74545, 56, 342, 45]
l3.sort()
print(l3)
print() #   space

#  TEMPORARY SORTING: SORTED() FUNCTION
# iska use alphabetical order lagane ke liye hota hai list ke item ko j

list4 = ["fdsf", "ukj", "ter", "abcd", "avb"]
print(sorted(list4))  # ab ye list ke jitem ko direct alphabetical order me laga sakta hai
print(list4)
print()   # space

#  PRINTING A LIST IN REVERSE ORDER

list5 = ["abc", "abcd", "hti", "cars"]
list5.reverse()
print(list5)



