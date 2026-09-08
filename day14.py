


# 1. Shuruat mein cart khali hai
shopping_cart = {}

# 2. User ne ek Laptop add kiya
shopping_cart['item'] = "Gaming Laptop"
shopping_cart['price'] = 75000
shopping_cart['quantity'] = 1
shopping_cart['delivery_status'] = "Pending"

print("Initial Cart:")
for k, value in shopping_cart.items():
    print(k, ": ", value)

print("\n--- Updated Cart after changes ---")

# 3. EXTREME UPDATE 1: User ne laptop ki quantity badha kar 3 kar di!
# Purani price 75000 thi, ab naye quantity ke hisab se price bhi update karni hogi
shopping_cart['quantity'] = 3
shopping_cart['price'] = shopping_cart['price'] * shopping_cart['quantity'] # 75000 * 3

# 4. EXTREME UPDATE 2: Delivery status badal gaya kyuki saman nikal chuka hai
shopping_cart['delivery_status'] = "Shipped"

print()  # space

print("Initial Cart:")

for k, value in shopping_cart.items():
    print(k, ": ", value)

print()    # space


# REMOVING KEY-VALUE PAIRS
#  : Jab hamein dictionary ke kisi data ki zaroorat nahi rehti, toh hum Python ke
#  del keyword ka use karke use hamesha ke liye delete kar sakte hain.
#           del dictionary_name['key_name']


dictionary = {
    "name": "samrat",
    "books": "right thought",
    "course": "python, java",
    "duration": " 3 years"
}
# mujhe iss dictionry me se diration wale key ko delete karna hai
del dictionary["duration"]

for k, value in dictionary.items():
    print(k, ": ", value)
print()   # sapce

# example 2 :

my_following = {
    "friend_1": "amit kumar",
    "friend_2": "vishal thakur",
    "friend_3": "suraj jadhav",
    "friend_4": "abhay raut",
    "friend_5": "abhishek kumar",
}
print("Before Unfollowing : ")
for k, value in my_following.items():
    print(k, ": ", value )

print() # space
# Unfollow karne se pehle

del my_following["friend_5"]
del my_following["friend_3"]

# Unfollow karne se pehle

print("After Unfollowing : ")
for k, value in my_following.items():
    print(k, ": ", value )

print()  # space



