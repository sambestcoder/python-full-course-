# REMOVING ALL INSTANCES OF SPECIFIC VALUES FROM A LIST

# .remove() list me se kisi item ko sirf ek baar delete karta hai. Agar wahi
# item list me baar-baar ho, to while loop ka use karke us item ko poori list se delete
# kiya ja sakta hai.

# Example: Agar list me 'cats' kai baar ho aur hume saare 'cats' ko list se hatana ho,
# to while loop ka use kiya jata hai.


pets = ["cows", "cats", "goats", "rabbits", "cats", "mouse", "cats"]

print("my pets : ")
for k in pets:  # YE SIRF PRINT KARNE KE LIYE HAI
    print(k)

# Jab tak 'cats' is list ke andar maujood hai, tab tak loop chalega
while "cats" in pets:
    pets.remove("cats")

print("\nmy pets : ")
for k in pets:  # YE SIRF PRINT KARNE KE LIYE HAI
    print(k)

print()  # space

# Example 2:


# Humein is list me se 'out of stock' ko hatana hai

products = [
    'laptop',
    'out of stock',
    'mouse',
    'keyboard',
    'out of stock',
    'monitor',
    'out of stock'
]

print("old product : ")
for k in products:
    print(k)

while "out of stock" in products:
    products.remove("out of stock")

print("\nnew products : ")

for k in products:
    print(k)

print("\n")  # space

# FILLING A DICTIONARY WITH USER INPUT

# Jab humein kisi user ke alag-alag data ko ek saath jodkar store karna ho
# (jaise Naam = Answer), tab hum Dictionary ka use karte hain.

# Example:
# Is example me ek Poll Program (Survey) banaya gaya hai, jo har user se uska
# naam aur uski favourite game ka naam poochta hai, aur use ek dictionary
# me save karta jata hai.

# Ek khali dictionary banayenge
dic = {}

# Ye ek flag variable hai jo batata hai ki while loop chalu hai ya band
polling_active = True

while polling_active:

    name = input("\nEnter the your name : ")
    game_name = input("Enter the your favourite game name : ")

    # Dictionary me data store kiya: key = name , value = game_name
    dic[name] = game_name

    # Phir ek question poochega ki game phir se shuru karna hai ya nahi
    question = input("kya app phir se game shuru karna chate hai (yes / no)  : ")

    # Condition
    if question == "no":
        polling_active = False

# printing

print("\n logo ki hobbies lists : ")

for key, value in dic.items():
    print(name.title() + "  isse ye pasand hai " + value.upper())

print("\n\n")  # space



# Example (2)

# Maan lijiye aap ek College Canteen me order le rahe hain.
# Har student apna naam aur favorite food batata hai.

# Dictionary me:
# Key = Student ka naam
# Value = Favorite food

# Ek khali dictionary hai jisme students order karenge
order = {}

ordering = True

while ordering:

    name = input("\nTell me your name : ")
    fav_food = input("Which food do you want ? :  ")

    # Dictionary ko arrange kiya
    order[name] = fav_food  # key = name , value = fav-food

    # Question
    question = input("Do you want anything else? Yes or no? : ")

    # Condition:
    if question == "no":
        ordering = False

print(" \n===== ORDER =====\n")

for keys, values in order.items():
    print(keys.title() + " this is your " + values.title())