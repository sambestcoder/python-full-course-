
#  NOT IN  (not in)  OPERATOR
#     :  The not in operator is used to check whether a value does not exist in a list.
# agr koi value list me nhi hai to isska use hota hai j

name_list = ["rohit", "roshan", "pravin", "niraj"]
name_list2 = "ritsh"

if(name_list2 not in name_list):
    print(name_list2.title()+" " +"the student name is not exits in name_list..")

else:
    print("the ritsh is exist in name_list..")
# name_list2 me ritsh hai agar name_list me ritsh nhi hai to print(lines) nhi to else
# else wali line print hongi ...
print()  # space

student_banned = ["vishal", "amit", "yuraj"]
student_unbanned = "avinash"

if(student_unbanned not in student_banned):
    print(student_unbanned.upper() + " "+ ", he is exist in student banned")

else:
    print("this student is exist in student banned")
print()   # space


# IF  ELSE
#  : if-else Statement ka use tab hota hai jab condition true bhi ho or false bhi ho
#  : The if-else statement is used when a condition can be either true or false

# ex(1)

 #       if condition:
#             code1
 #        else:
 #            code2


marks = 50

if marks >= 60:
    print("pass..")

else:
    print("fail")



#     IF  ELIF ELSE
#   :    The if-elif-else statement is used to check multiple conditions
#  Yahan sirf 2 possibilities hoti hain:
# Condition True
# Condition False
# Lekin agar 3 ya usse zyada possibilities ho to?
# :     If any condition is `True`, Python executes the code block for that
#     condition and skips all the remaining conditions.

age = 12

if(age < 4):
    print("your addmision cost ki zero ,...")

elif(age < 18):
    print("your addmision cost is 5 rupess")

else:
    print("your addmision cost is 10 rupess")



# explaintion :
# mene age varible me 12 strore kar diye
# 1st condition : agar mera age 4 se lessthan hai to zero print honga... ye false hai
# 2nd conditon  : agar mera age 18 se  lesssthan hai to 5 rupess print  honga .... ye true hai
# 3rd condiotn : innme ek condtion true nikli ab code chalna band hojayega
#   wo aaghe ki conditon fllow nhi karenga ....

# varible use :
#         Pehle tarike me hum har jagah print(...) likh rahe the. Isse achha tarika
#         yeh hai ki hum pehle sirf price decide karein, aur baad me ek hi baar print karein.

age = 14

if(age < 4):
    price = 0

elif(age < 16):    # ye conditon true hai
    price = 5

else:
    price = 10

print("you addminstion cost is  "+str(price)+ " ")  # isse time bachta hai print likha ne se accha
print() #       space

# Ex 3:


marks  = 90;

if(marks <= 60):
   grade = "D"

elif(marks >= 24):
    grade = "C"

elif(marks >= 92):
    grade = "A"

else:
    grade = "E"

print("Your rsult is .. "+ str(grade)+ ". ")


