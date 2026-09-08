# exercise 1 :
#  Use a dictionary to store information about a person you know .
# Store their first name, last name, age, and the city in which they live . You
# should have keys such as first_name, last_name, age, and city . Print each
# piece of information stored in your dictionary


person = {
    "first_name": "vishal",
    "last_name": "mankar",
    "age": 20,
    "city": "pune",
}

print("first name: ", person["first_name"])
print("last name: ", person["last_name"])
print("age : ", person["age"])
print("city: ", person["city"])

print() # space

# exercise 2:
#  Use a dictionary to store people’s favorite numbers .
# Think of five names, and use them as keys in your dictionary . Think of a favorite
# number for each person, and store each as a value in your dictionary . Print
# each person’s name and their favorite number . For even more fun, poll a few
# friends and get some actual data for your program

# matalb : Is exercise mein hum Similar Objects wali dictionary banayenge. Yaani yahan keys honge
# alag-alag logon ke naam (5 log), aur unki values honge unke favorite numbers.
# ko print karne ko bola hai

fav_numbers = {
    "rohit": 90,
    "vishal": 78,
    "abhimanyu": 67,
    "harry": 24,
    "rahul": 12,
}

for key, value  in fav_numbers.items():
    print(key.title()+",s "+ "favorite number is "+str(value) )

# innko ek alga alg print karna musibat hai to ek saath print kiya ..








