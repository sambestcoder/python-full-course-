

# ARBITRARY KEYWORD ARGUMENTS (**kwargs)

# Kabhi-kabhi humein key aur value dono chahiye hote hain,
# lekin pehle se pata nahi hota ki kitni key-value pairs aayengi.

# Example:
# Har user ka first name aur last name fixed hai,
# lekin location, city, job, hobby etc. alag ho sakte hain.

# Aise situation mein ** ka use karte hain.

# **user_information saari extra key=value pairs ko
# ek dictionary mein collect karta hai.


# Function banaya
def build_profile(first_name, last_name, **user_information):
    # Empty dictionary banayi
    profile = {}

    # First name aur last name dictionary mein add kiye
    profile["first_name"] = first_name
    profile["last_name"] = last_name

    # Extra information ko dictionary mein add karenge
    for key, value in user_information.items():
        profile[key] = value

    return profile

# Function ko call kiya
obj = build_profile("Sam", "Sharma",
    location="Hira Nagar", city="Mumbai"
                    )

# Profile ki saari information print karenge
for key, value in obj.items():
    print(key, ":", value)


print("\n") # sp



# example (resturant)

def create_order(customer_id, customer_name, **extra_deatils):

    order = {"customer id ": customer_id, "customer name": customer_name}

    for key, value in extra_deatils.items():
        order[key] = value

    return order

order1 = create_order(12345687, "vihshal")

order2 = create_order(568456, "sumit",
                      table_number = 12, post = "police officer")

for key, value in order1.items():
    print(key, ": ", value)

print("") # sp

for key, value in order2.items():
    print(key, ": ", value)