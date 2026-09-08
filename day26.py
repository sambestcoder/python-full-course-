from day2 import first_name


# Question :

#  8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt . The function should print
# a sentence summarizing the size of the shirt and the message printed on it .
#  Call the function once using positional arguments to make a shirt . Call the
# function a second time using keyword arguments

# explain : funtion define karna hai 2 parameter lene hai

def make_tshirt(size, massage):
    print("tumne order kiya "+size+" "+ "tumara massage hai "+ massage )

# Call 1: Positional arguments (order matters)
make_tshirt("middium", "i love python")

# Call 2: Keyword arguments (order doesn't matter)
make_tshirt(massage= "i am very busy", size= "large")

print() # sp

#  question 2 :

# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python . Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message

 # explain :

def make_shirt(size = "large", massage = "i love python"):
    print("you ordered a size "+size+", "+ "shirt with a massage "+massage)


make_shirt()

make_shirt(size = "small") # issme me ne sirf size overwrite kiyi hai

make_shirt(size= "very small", massage= "i love java")

print() #sp


 # ek function banayeghe

def build_persion(first_name, last_name):
    # dic me key and value dali
    dic = {'first name :', first_name, 'last name : ', last_name }
    return dic  # ye dictionry ko bahar bhej denga

print(build_persion("pravin", "sharma"))
# mene call kiya value set kiyi hai
print() # sp


# OPTIONAL PARAMETER KE SAATH (AGE ADD KARNA)

# age='' ek optional parameter (default empty string) hai.
# Agar user age pass karega, toh if age: condition true hogi aur dictionary me 'age'
# key add ho jayegi.

def function2(first_name, last_name, age = ""):
    person = {"first name":  first_name, "last name": last_name}
    # agar age diyi honga to ye chalega

    if age:
        person["age"] = age
        # me persion dic me age print karunga and uska parameter honga
    return  person

# call funtion

var = function2("amit", "singh", 26)
print(var)


print()   # sp

# example 2

def built_car(make, model, colour, year):
    car = {"make ": make, "car model": model}

    if colour:
        car["car colour "] = colour

    if year:
        car["car which year "] = year

    return car

call_funtion = built_car("harry worte", "19163i5", "Red", 1990)

# for loop me print kayse hota hai

for key, value in call_funtion.items():
    print(key + ": "+str(value))  # value kis kis me string bhi ho sakti hai


# FUNTION USDED TO WHILE LOOP

# get_formatted_name() → first name + last name ko jodta hai.
# .title() → naam ke first letters capital karta hai.
# while True → program ko baar-baar chalata hai.
# input() → user se first aur last name leta hai.
# Function ko naam bhejta hai aur formatted naam return hota hai.
# print() → Hello, Name! print karta hai.

def user_name(fist_name, last_name):

    full_name = first_name+ " "+last_name
    return full_name # full_name ko wapas bhejega

while True:

    print("\n\nplease tell me your name ...")
    first_name = input("enter the first name : ")
    second_name = input("enter the last name : ")

    call_funtion2 = user_name(first_name, second_name)  # call funtion me user se name lege

    print("hello, ", call_funtion2)

# ye program chalte hi rahe ga jab tak me break ka use nhi karu



























