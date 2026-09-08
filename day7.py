
# IF STATEMENT

# Programming me bhi jab computer ko koi decision lena hota hai,
# to hum if statement ka use karte hain.
# Yeh program ki current situation (state) ko check karta hai
# aur uske hisab se sahi action leta hai.
# In programming too, when the computer has to make a decision, we use an if statement

# Hum chahte hain ki saari cars ka naam normal format me print ho
# (jaise Audi, Subaru), lekin bmw ka naam poora capital letters me print ho (jaise BMW).

car_list = ["kawasake ninja ", "farari", "roylroyal", "bmw"]

for k in car_list:
    if k == "bmw":
        print(k.upper())
    else:
        print(k.title())
print()  # space

#  CONDITIONAL TESTS (true or False)

# Sabse Badi Confusion: single equal sign( = ) vs ( == ) doble equal sign
# Single Equal Sign (=) Value Dena (Assignment)
car =  "farari"

# Double Equal Sign (==)Sawaal Poochna
# Jab aapko do cheezon ko aapas me compare karna ho ki wo barabar hain ya nahi.

car == "BMW"

print() # space

# Q : kya bike kawasake ninja hai ?
bike = "kawasake ninja"

print(bike == "farari") # statement true honga to true nhi to false denga

print(bike == "rollesroyal")

print(bike == "kawasake ninja")
print()  # space

car_2 = "bmw"

print(car_2 == "BMW")  # yape mujhe otp false milenga kyu ki letter ka fark hai
print(car_2.upper() == "BMW") # issne bmw ko temp.. BMW bana diya hai to ye true denga
print() # space

car_3 = "FARARI"
print(car_3.lower() == "farari")
print() #space

#  CHECKING FOR INEQUALITY: != (BARABAR NAHI HONA)

boy_name = "sumit"
print(boy_name != "samrat")
print() # space

answer = 89
if(answer != 90):
    print("that is not correct answer... ")

# agar answer 90 nhi hai to not correct ayega
print()  # space

age = 18
if(age == 18):
    print("true")
else:
    print("false")

#   OR

# Kya age 18 ke barabar hai?"
# Kyunki dono barabar hain, isliye answer aaya True
print(age == 18)
print(age != 18 )
print()  # space

# GREATER THAN AUR LESS THAN SIGNS

# LESSTHAN SIGN : <
# GREATERTHAN SIGN : >

# Sawaal: Is 19 smaller than 21
# Jawaab: Haan, chhota hai. Isliye aaya True.

age = 19
print(age < 21)

# Less Than or Equal To
print(age <= 21)  # agar age chota hai 21 se to true ayega agar equal hai to true ayega

age  = 45
print(age > 45) # kya age 45 se greater than hai nhi to false ayega










































