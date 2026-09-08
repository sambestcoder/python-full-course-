# LISTS
#  list is a collection of data or item in particular order is called as LISTS

list = ["samrat ", "pratik", "vishal"]
print(list)
print() # sapce

list2 = ["sam ", 567,"ghoast", "youra", 768]
print(list2)
print(list2[0])  # 0 number par jo index no honga wo print honga
print(list2[3])
print()  # space

# title and upper case use huye hai

print(list2[3].title())
print(list2[2].upper())
print()   # space

list3 = ["samrat", 756, 767, 23, 45]
print(list3[-1])   #  - sign se ulta kaam karenga ..
print(list3[-2])

# CHANGANING ADDING , REMOVEING , AND DELETING ELEMENTS 


classroom = ["sumit", "prashik", "vishal", "rohit"]
print(classroom)

classroom[1] = "hobbine"
print(classroom) # issme 1 index pe jo prashik name tha usko change kiya 
                  #  uski jagah hobbine dala 

classroom[3] = "rohan"  # rohit = change  =  rohan 
print(classroom)
print()   # space 


# ADDING ELEMENTS TO THE END OF THE LIST 

# append():iss ka use  hamesha list ke last mein item jodne ka hota  hai

tusion = ["pravin", "pranav", "abhi"]
tusion.append("prachit")
print(tusion)  # ab list ke bhiche ek prachit name ka elemnt add ho gaya 

tusion.append("ravin")
print(tusion)






