from day26 import build_persion


def checkout(cart_items, receipt):
    """Cart se items nikaal ke receipt mein daalo (jaise items purchase ho rahe hain)."""

    while cart_items:
        item = cart_items.pop()
        print("Purchasing: " + item)
        receipt.append(item)

# Case 1: Bina copy ke - original cart khaali ho jayega
my_cart = ['shoes', 'watch', 'bag']
my_receipt = []

checkout(my_cart, my_receipt)

print("Cart after checkout:", my_cart)        # khaali ho gaya
print("Receipt:", my_receipt)

#   Ab agar hum chahte hain ki my_cart list safe rahe
# (jaise "wishlist" ke record ke liye), toh copy bhejenge:

# to ye use karo

#     checkout(my_cart[:], my_receipt)   # yahan copy bheji [:]

print("\n\n")  # sp



# ARBITRARY NUMBER OF ARGUMENTS

# Kabhi-kabhi humein pehle se pata nahi hota ki function mein
# kitne arguments pass kiye jayenge.

# Example:
# Pizza mein customer 1, 3 ya 5 toppings maang sakta hai.

# Aise situation mein * (asterisk) ka use karte hain.
# *toppings saare arguments ko collect kar leta hai.

# Isliye hum jitne chahein utne arguments pass kar sakte hain.

# ex :

# Function banaya
def make_pizza(*toppings):
    # Saare toppings print karenge
    print("Toppings:", toppings)

# Function ko sirf 1 argument diya
make_pizza("Cheese")

# Function ko 3 arguments diye
make_pizza("Chocolate", "Gulab Jamun", "Rasgulla")

# Function ko 5 arguments diye
make_pizza("Cheese", "Corn", "Onion", "Tomato", "Capsicum")
print("\n")


# ab ham yehi funiton for loop ke saath kare ghe

#ex 2

def make_pizza(*toppings):

    print("\npizza me ye topings hai : ")

    for k in toppings:
        print("- ", k)


make_pizza("pepperoni") # ek argument diya

# bahut sare argument diye
make_pizza("mushrooms", "green peppers", "extra cheese")

print("\n\n") # sp




# MIXING POSITIONAL AND ARBITRARY ARGUMENTS

# Agar function ko normal argument (jaise size) aur arbitrary arguments
# (jaise toppings) dono chahiye, toh rule ye hai:
#
# Arbitrary argument (*toppings) hamesha SABSE LAST mein aana chahiye
# function definition mein


# ex : Creating birthday card example

def make_birthday_card(name, *wishes):

    print("\n Happy Birthday : ", name.title())
    # issme log wihses kareghe

    for k in wishes:
        print("-- ", k)

# calling function

make_birthday_card("rahul", "🎉 Wishing you lots of happiness, "
                            "success and good health. Have a wonderful day! ❤️")

make_birthday_card("sumit", "🎂🔥 Keep smiling, keep growing and keep rocking!")


# meaning
# name → birthday person ka naam
# *wishes → jitni bhi wishes aayengi, sab collect karega
# for wish in wishes → wishes ko ek-ek karke print karega.

print("\n\n") # sp





