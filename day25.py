
#                           FUNCTIONS

# Function code ka ek chhota block hota hai jo ek khaas kaam karta hai. Zarurat padne par uska
# naam call karke usi code ko baar-baar use kiya ja sakta hai.
# use :
#       Agar aapko koi kaam apne program me 10 baar karna hai, toh aapko 10 baar code
#       likhne ki zaroori nahi hai. Aap bas function ka naam bolao (call karo) aur
#       Python wo kaam kar dega.

# main points :
#  def Keyword: def Python ko batata hai ki ab ek function banaya ja raha hai.
# greet_user() : Yeh function ka naam hota hai. Function ka naam likhne ke
# baad () aur : lagana zaroori hota hai._
# greet_user() (Calling the function): Function ko jab tak hum call nahi karenge, wo chalega nahi.


# basic program :

def greet_user():
    print("sam digital computer center ...")

greet_user()  # function ko call kiya

def sum():
    print(25 + 25)

sum()

print() # sp


# FUNCTION KO INFORMATION PASS KARNA

# Ab function username accept karta hai. Jab call karte ho greet_user('samart'), toh
# 'samart' value function ke andar username mein store ho jaati hai.


def username(username):
    print("hello , "+username.title())

username("samrat") # ye value usename agrgument me store ho gaya hai


# ARGUMENTS VS PARAMETERS — DIFFERENCE

# Parameter = function definition mein jo variable hota hai (yahan username)
# Argument = function call ke time jo actual value pass karte ho (yahan 'samrat')


def username(username): # iss varible ko parameter kehte hai
    print("hello , "+username.title())

username("samrat") # mene ye value pass kiyi hai usse argument kehta hai

print()  # sp



# MULTIPLE PARAMETERS

def pets(pet_1, pet_2):
    print("mere pass "+pet_1+ " hai")
    print("mere pass "+pet_2+ " hai")

pets("dog", "cat")
# tumne iss me order ke nusaar input diya hain

print() # sp

# KEYWORD ARGUMENTS (order matter nahi karta)

def student(name1, name2):
    print("student ka name : "+name1.title())
    print("student ka dusra name : "+name2.title())

# call funiton
student(name1 = "sam", name2 = "samrat" )

# Yahan tumne naam (name1 =, name2 =) explicitly bataya, isliye order se koi farq nahi padta.
print() #sp


# RETUN FUNCITON :
# functions sirf print kar rahe the. Lekin functions return bhi kar sakte hain



def get_name(first_name, last_name):
    full_name  =  first_name + last_name
    return full_name.title()


print(get_name(first_name = "samrat ", last_name = "kshirsagar"))
print() # sp


# agar mene issme print nhi kiya to value retun wala print nhi honga iss
# liye print dena honga


# DEFAULT VALUES :

# Jab function define karte ho, tum har parameter ke liye ek default value set kar
# sakte ho. Rule simple hai:
# Agar function call karte time uss parameter ke liye argument diya, toh Python
# wahi value use karega
# Agar nahi diya, toh Python parameter ki default value use kar lega

# Default parameter ke baad non-default parameter nahi aa sakta.

def student(last_name, name = "samrat"): # name = ki default value samrat hai
    print("my name is "+name+" ")
    print("my surname is "+ last_name)


student("kshirsgar\n")  # default value ayese hi print hoti rahe gi
student(last_name= "kshirsagar")
student(name = "sam", last_name= "kshirsagar")  # ab meri defualt value yaha pe change ho gayi hai

print() # sp

# ex(2) default value :

def shopppy(shirt = 'M', brand = 'collection rock'):
    print("my shirt size is "+ shirt+ " and "+ "brand is "+brand)

shopppy()                                        # dono default use honge
shopppy(shirt= 'L')                                # sirf size override
shopppy(brand= " rajveer collection")               # sirf text override
shopppy('Xl', 'pravin collection')          # dono override, positional















