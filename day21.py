from xml.dom.minidom import ProcessingInstruction

# USER INPUT()  FUCTION
# : THE INPUT() FUNCTION IS USED TO TAKE INPUT (DATA) FROM THE USER.

# name = input("Enter your name : ")
#
# print("hello, "+name+ "  welcome to python world..")
# print()  # space
#
# # input() hamesha String (text) deta hai.
# # 👉 Number chahiye to int() se Integer me badalte hain. ✅
# # input() = Text
# # int() = Text → Number
#
# number  = int(input("Enter your number : "))
# print("my favorite number is "+ str(number)+" .")
# print()  #sp

#ex :

# age = int(input("Enter your age  : "))
#
# if age > 18:
#     print("you are adult...")
#
# else:
#     print("you are kid..")

print()  #sp

# WHILE LOOP
# : A WHILE LOOP MEANS REPEATING A TASK AGAIN AND AGAIN AS LONG AS A CONDITION IS TRUE.
#while loop ka matlab hota hai: "Jab tak yeh condition sach (true) hai,
# tab tak is kaam ko karte raho."

# EX :

number = 1

# Jab tak number 5 ya usse chota hai, loop chalega
while number <= 5:
    print(number)
    number = number + 1  # isme number ke andar ek badhte hi rahe ga ..isse loop stop ho jayega

# agar me sirf print(number) hi likhta hu to while loop chalte rahe ga .. jab tak 5 se chota
# number nhi mil jata
#Agar hum chahte hain ki hamara program ek baar chal kar band na ho, balki chalta rahe jab tak
# user khud use band na karna chahe, tab hum while loop use karte hain.

print() #sp


# ex(2) Ek aisa program jo user se tab tak naam poochta rahega jab tak user 'quit'
# nahi likh deta.

# name = ("apne dost ka name bolo ya program exist karne ke liye 'quit' likho... ")
#
# # Ek khali variable banaya loop shuru karne ke liye
# name2 = " "
#
# while name2 != "quit":   # name2 agar not quit hai to ...
#     name2 = input(name)
#
#     # Agar user ne 'quit' nahi likha, to naam print karo
#     if name != "quit":
#         print("dost ka name hai : "+name2)
#
# print("\nprogram band ho gaya hai , thanks you...")

print()  #sp




#  MODULE OPERATOR :
# do numbers ko divide karte the, toh ek Remainder (sheshfal/bacha hua number) aata tha.
# Python mein % sign ko Modulo bolte hain, aur iska kaam sirf aur
# sirf Remainder batana hota hai.

#ex :
# 4 % 3 : Agar 4 ko 3 se divide karoge, toh  :  3 * 1 = 3  hamesha 3 hi bachenga to wo reminder hai

# Modulo ka sabse bada use hota hai yeh pata karne mein ki koi number Even (sam) hai ya
# Odd (visham) Duniya ka koi bhi Even number (jaise 2, 4, 12, 42) agar 2 se divide hoga,
# toh bachega kya? Hamesha 0  Agar remainder 0 nahi bacha (1 bacha), toh woh Odd number hai.



# number  = int(input("Enter your number : "))
#
# if number%2 == 0:
#     print("The number is "+str(number)+ " even..")
#
# else:
#     print("The number is "+str(number)+ "  odd...")


