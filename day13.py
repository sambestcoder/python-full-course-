
#  Dictionaries
# : Python mein dictionary banane ke liye hum Curly Braces { } ka use karte hain.
#   dictionary ek Word (shabd) dhoondte ho aur uske samne uska Meaning (arth) likha hota ha

car = {"AMW": "green",
       "rollsroyal": "balck",
       "maruti": "blue"
       }

print(car)

print(car["AMW"])  # abye uska colur print kaenga
print(car["maruti"])

print()  # space

points = {
    "rahul": 90,
    "vishal": 21,
    "abhay": 80
}
# issme mujhe dekhana hai ki vishal ko kitne points mile hai
new_point = points["vishal"]
# print(new_point)
new_point2 = points["abhay"]


print("you are earn "+str(new_point)+" points...")
print("you are earn "+str(new_point2)+" points...")
print() # space
# ya pe mujhe string and integer ko ek saath nhi jod sakte to
# mene points ko hi string bana diya


# ADDING NEW KEY VALUE PAIRS
#   : ython ki dictionaries Dynamic hoti hain. Iska matlab hai ki tum bani-banyee
#      dictionary me kabhi bhi naya saman (data) jod sakte ho.
# Dicnary me  Nayi Information ya data  Kaise Add Karte Hain

cars = {
    "rollroyal": "green",
    "maruti" : "yellow"
}

print(cars)
print()  # space

# abb issme ye sara data add ho gaya hai ...

cars["mahindra"] = "white"
cars["lanborgini"] = "blue"

print(cars)
print()   # space

# ex(2)

account = {
    "username": "sam",
    "password": 6485
}

account["account number"] = 648535465
account["ifc"] = 3698
account["branch"] = "mumbai"
account["mobile"] = 9123554789

print(account)
print()  # sapce

# for loop me kayse likhe

# items() → dictionary ke saare key-value pairs deta hai.
# key me key aayegi aur value me uski value.

for k, value in account.items():
    print(k, ": ", value)

# k me key aayeghi
# value me uski value ayeghi
print()  # space


# (STARTING WITH AN EMPTY DICTIONARY) : Pehle ek khali dibba banana aur phir usme samaan bharna.

# Ek khali student profile banayi
student_profile = {}

student_profile["name"] = "sam kshirsagar"
student_profile["Roll no"] = 4685
student_profile["address" ] = "adhikapur road"
student_profile["selected course"] = ["python", "html", "java"]
                                    #  agar jada data ho to [] issme likhana

for key, value in student_profile.items():
    print(key, ": ", value)

print()   # space


# MODIFYING VALUES IN A DICTIONARY

#    : Agar dictionary mein koi Key pehle se hai, aur aap usko naye tarike se likhte
#    hain (dict[key] = new_value) , toh purani value hat jati hai aur nayi
#    value uski jagah le leti hai.

car = {
    "maruti": "green",
    "giwangun": "yellow"
}

print("the car colour is "+ car["maruti"]+ " .")
# yaha pe hamne car ka colour green kar diya hai ab hum isse modify karenghe ..

# ya ha pe hamne maruti colour change kar diya
car["maruti"] = "Red"
print("the car colour is "+ car["maruti"]+ " .")

print()   #  space


# GAME LOGIC EXAMPLE: ALIEN MOVEMENT
# ek game ka logic hai. Alien ki speed ke hisab se uski position badalni hai.

# Alien abhi 0 position par hai (x_position: 0).Uski speed medium hai.
# Agar speed slow hai to use 1 step aage badhna hai.
# Agar speed medium hai to use 2 steps aage badhna hai.
# Agar speed fast hai to use 3 steps aage badhna hai.

alien = {
    "x_position": 0,
    "y_position": 25,
    "speed": "medium"
}
print("original_position :"+ str(alien["x_position"]))

# Step 1: Pata karo ki kitna aage badhana hai (x_increment)
# issme if elif, else conditon se pata karenghe ki X_position kitni badhani hai


if alien["speed"] == "low":
    x_increment = 1

elif alien["speed"] == "medium":
    x_increment = 2

else:
    x_increment = 3

# step 2 : iss me x_position me x_increment jod kar add kardo isse x_position change ho jayeghi

alien["x_position"] = alien["x_position"] + x_increment

# ab jo new  position aayi hai usse print kar do
print("new_postion : ", alien["x_position"])

print()  # space


