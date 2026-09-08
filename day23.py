#
#  question :
# 7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
# that do each of the following at least once:
#  •	Use a conditional test in the while statement to stop the loop .
#  •	Use an active variable to control how long the loop runs .
#  •	Use a break statement to exit the loop when the user enters a 'quit' value

# matlab :
# Question kya tha: User se pizza toppings maangte raho jab tak woh 'quit' na likh de.
# Hume is same program ke 3 alag-alag versions banane hain:
# Version 1: while ke theek aage condition check karna.
# Version 2: Ek Flag (Active Variable) ka use karna.
# Version 3: break statement ka use karna.
# Chalo teeno ko ek-ek karke bilkul basic se samajhte hain.


# tooping name ka varible me string khali dali hai isse loop ko shuru hone ke liye

# VERSION 1

topping = " "
promt = "\n pizza par konsa topping dalna hai (exist karne ke liye quit karo) : "

# while topping != "quit":
#     topping = input(promt)
#
#     if topping != "quit":
#         print(" i will add "+topping+ "  your pizza")
#
# print("tumne quit dabaya hai program exit hua hai ")
#
# print() # space



# VERSION 2
# Version 2: Ek Flag (Active Variable) ka use karna.

# active = True
#
# while active:
#
#     topping = input(promt)
#
#     if topping == "quit":
#         active = False
#         print("tumne quit dabaya hai program exit hua hai ")
#
#     else :
#         print(" i will add "+topping+ "  your pizza")
#
# print()  # sp



# VERSIONN 3 : BREAK STATEMNET :

# while True:
#     topping = input(promt)
#
#     if topping == "quit":
#         print("tumne quit dabaya hai program exit hua hai ")
#         break
#
#     print(" i will add " + topping + "  your pizza")
#
# print()  # sp


# USING A WHILE LOOP WITH LISTS AND DICTIONARIES

# for loop list ko sirf padhne (read) ke liye best hai. List ko badalna
# (modify) ho, to while loop use karo.

# for loop se list ke har item par ja sakte hain, lekin usi time list ko modify
# (add, remove, update) nahi karna chahiye, kyunki loop confuse ho sakta hai.
# Agar list me badlav karna ho, to while loop use karna behtar hota hai.


# MOVING ITEMS FROM ONE LIST TO ANOTHER

# ex : Maan lijiye website par kuch naye users register hue hain, lekin abhi
# unverified hain. Jaise hi hum unhe verify karte hain, while loop aur .pop()
# ki madad se unhe unverified list se nikal kar confirmed users ki list me add
# kar dete hain.


unconformed_user = ["vishal", "abhimanyu", "pratiksha"]
# user unconformed_user se confirmed_user ke list me jayege
confirmed_user = []

while unconformed_user:
    varible = unconformed_user.pop()
    # pop() function last ke list ka data varible me dalenga
    # last data varible me store honga

    print("varified user : " + varible.title())

    confirmed_user.append(varible)
    # ab varible ka data confirmed user me jayenga

# ab loop se bahar nikalna hai
# confirmed_user me jo data bheja varible ka usko arrage me print
# karna hai


print("\nthe following confirmed user : ")

for k in confirmed_user:
    print(k.upper())

print()  # sp

# explation :

# Program while loop ki madad se unconfirmed_users list se har user ko
# .pop() se nikalta hai, usse verify karta hai, aur .append() ki madad se
# confirmed_users list me add karta hai. Jab pehli list khali ho jaati hai,
# loop ruk jata hai aur aakhir me sabhi confirmed users ko print kar diya
# jata hai.


# ex (2)

pending_order = ["pizza", "cheese", "burger"]

conformed_order = []  # confirmed nhi huye hai

while pending_order:
    var = pending_order.pop()

    print("preparing order : " + var.upper())  # banna chalu hai

    conformed_order.append(var)

print("\nthere will be confirmed order : \n")

for k in conformed_order:
    print(k.title())

print()  # sp

# REMOVING ALL INSTANCES OF SPECIFIC VALUES FROM A LIST

