# exercise :
#  People: Start with the program you wrote for Exercise 6-1 (page 102) .
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people . Loop through your list of people . As you
# loop through the list, print everything you know about each person
# :
#   Is exercise me hume alag-alag logo ki details (jaise unka naam, city) ko alag dictionaries me
#   rakhna hai, aur phir un sabhi dictionaries ko ek single List me store karna hai.
from day2 import first_name, last_name

person = {
    "first_name": "rahul",
    "last_name": "digital",
    "city": "dilhi",
}
person2 = {
    "first_name": "vishal",
    "last_name": "pavar",
    "city": "mumbai"
}
person3 = {
    "first_name": "snehal",
    "last_name": "sharma",
    "city": "mumbai"
}

people = [person, person2, person3]

for k in people:
    print("Full name : " + k["first_name"] + " " + k["last_name"])
    print("city : " + k["city"] + "\n")

print()   # sp

# exercise :
# Favorite Places: Make a dictionary called favorite_places . Think of three
# names to use as keys in the dictionary, and store one to three favorite places
# for each person . To make this exercise a bit more interesting, ask some friends
# to name a few of their favorite places . Loop through the dictionary, and print
# each person’s name and their favorite places

# Key: Insaan ka naam hoga (String).
# Value: Uske pasandida shehron ya jagahon ki ek List hogi (kyunki ek insaan ki ek se zyada favorite
# jagah ho sakti hain). Isme hum Dictionary ke andar List use kar rahe hain.
# Jab hum is par loop chalayenge, toh hume .items() ka use karna padega taaki hum
# e Key (Naam) aur Value (Places ki list) dono ek sath mil sakein.

fav_place = {
    "manisha": ["chikli", "varinda", "raigad"],
    "vishal": ["mumbai", "hedrabaad"],
    "abhimanyu": ["himachal pradesh", "pakistan", "aurangabaad"]
}
# Step 2: Loop chalakar person aur unki places ko print kiya

for key, value in fav_place.items():
    print(key+ ",  Favorote place are .. ")

    # Kyunki 'value' ek list hai, isliye iske andar ek aur loop chalega
    # iss liye hum ne phir ek for loop lagaya ..

    for k in value:
        print(k)

    print()  # bich me space aa sake iss liye ..

print()  #sp

# exercise :
# . FAVORITE NUMBERS: MODIFY YOUR PROGRAM FROM EXERCISE 6-2 (PAGE 102) SO
# EACH PERSON CAN HAVE MORE THAN ONE FAVORITE NUMBER . THEN PRINT EACH PERSON’S
# NAME ALONG WITH THEIR FAVORITE NUMBERS

#     : ek aisa program banana hai jahan ek insaan ke ek se zyada favorite numbers ho sakte hain.
#     Iska matlab har ek naam (Key) ke samne hume numbers ki ek List (Value) rakhni hogi.


fav_numbers = {
    "amit": [90, 34, 56],
    "vishal": [84, 23, 78.89],
    "pranav": [789, 6485, 34]
}

# Step 2: Loop chalakar person aur unke numbers ko print kiya

for key, value in fav_numbers.items():
    print(" NAME : "+ key.upper()+ "'s "+ "Favroite number are..")

    # isse list sidhi print karenghi
    for k in value:
        print(k)

    print()  # sp ke liye

print() # sp


