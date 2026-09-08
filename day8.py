
# CHECKING MULTIPLE CONDITIONS

# AND OPERATOR
#Jab saari conditions True (sahi) hongi, tabhi poora answer True aayega. Agar ek bhi
# condition False (galat) hui, toh poora answer False ho jayega."
# SHORTCUT :  if the both value of true then answer is true .. other wise false

age = 21
age2 = 22
print(age >= 22 and age2 >= 19)
print() # sapce
# explation :
# first condition : age greather than hai mera 22 se ? nhi hai to ye false hai
# second codition : age2 grether than hai 19 se ? ye true hai
# result : false and true =  false

# ex (2)
pin_number = True
password = False  # T and F : F

if(pin_number == True and password == True):
    print("money translation sucessfull..")
else:
    print("money transaltion fail...")
print()  #space


# OR OPARETOR .
# agar koi ek condition bhi True ho jaye, toh kaam chal jaye,
# tab aap or ka use karte hain.
# If any one condition is true, then the result will be true.

age1 = 22
age2 = 18

print(age1 >= 21 or age >= 21)

# age_0 >= 21 →   22 >= 21   →   True ✅
# age_1 >= 21 →   18 >= 21   →   False ❌
# issme sirf ek hi true hai to result bhi true ayega ...

name1 = 18
name2 = 18

print(name1 >= 21 or name2 >= 21)
# issme dono conditons worng hai to anser bhi false ayega

if(name1 >= 21 or name2 >= 21):
    print("name1 is  grather than to 21 and name2 is grather than to 21..")

else:
    print("name1 is not grather than to 21 and name2 is not grather than to 21..")
    print( "And then answer is false ...")
print()  # sapce

# ex(2)

age2 = 12
name3 = True

print(age2 >= 21 or name3)
print() # space
# iska matlab mene kaha age2 = 12 hai to wo grether than hai kya 21 se to nhi hai to ye false hai
# second condition to true hi hai or jab or ke case me koi ek true hota hai to naser bhi true
# hota hai ..

# ex(3)

name5 = False
name6 = False
name7 = True

if(name5 or name6 or name7):
    print("The Program Successful ")   #  ye tre nikla to ye run honga

else:
    print("The Program Failed. ")
print()   # space
# Logic : name5  or  name6  or  name7
#        false   or   false  or  true
#        false   or     true                # issme ek to true hai
#            True




#  IN OPERATOR...
#    : in ka use kisi value ko list ke andar dhoondhne ke liye hota hai.
#     : It is used to find a value inside a list.

list = ["vihshal", "pravan", "harry", "vishakha"]
print("pravan" in list)              #  list me pravan hai to true

print("raman" in list)  # list me raman nhi hai to false

# ye dictonary me bhi use hota hai

dic = {
    "name": "samrat vijay kshirsagar",
    "roll_no": 7899
}

print("name" in dic) # kya dic me ye name hai hai to true ayega
print() # space

user_name = ["vishal", "abhimanyu", "pravin"]
user_name2 = "pravin"

if(user_name2 in user_name):
    print("username is access..")
else:
    print("user name is denied ...")
# kya username_2 me pravin hai kya user_name me pravin hai to true ayega





























































