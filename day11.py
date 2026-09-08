
#  PRATICE...
# do varible hai cuurent user and new user .. jo
# Instagram par naya account bana rahe ho. Jab aap koi username dalte ho, toh Instagram
# piche se kaise check karta hai ki wo naam pehle se kisi ke paas hai ya nahi?
# Ye code bilkul wahi kaam kar raha hai.
# current_users: Ye wo log hain jinka account pehle se bana hua hai.
# new_users: Ye wo naye log hain jo abhi sign-up karne ki koshish kar rahe hain. Notice kiya
# Naye users me 'RAHUL' aur 'Priya' aise hain jo pehle se hain, bas unhone capital letters
# use kiye hain.
# Humne ek khali dabba (list) banaya: current_users_lower = [] name se
# for loop lagakar humne current_users ke saare naamo ko .lower() function ki madad
# se choti ABC me badla. Aur .append() ki madad se unhe us khali dabbe me daal diya.

current_users = ['rohit', 'rahul', 'admin', 'priya', 'amit']
new_users = ['RAHUL', 'suresh', 'Priya', 'deepak', 'vikram']

# Ek nayi list banayenge jisme current_users ke saare naam lowercase (choti ABC) me honge
current_users_lower = []
for k in current_users:
    current_users_lower.append(k.lower())

# Ab naye users ko check karenge
for k in new_users:
    if k.lower() in current_users_lower:
        print(f"Sorry, the username '{k}' is already exits. Please enter a new username.")
    else:
        print(f"Great, the username '{k}' is available!")

print() # sapce

# ex(2)

old_gamer = ["suraj gaming", "vishal gaming", "sk sabirboss", "total gamming"]

new_gamer = ["abhay_gaming", "TOTAL GAMMING", "payal gaming", "SURAJ GAMING"]

update_gamer = []

for k in old_gamer:
    update_gamer.append(k.lower())

for k in new_gamer:
    if k.lower() in update_gamer:
        print(f"the gamer is allready exist '{k}' please try again..")

    else:
        print(f"the gamer '{k}' is availbe..")

print() # space

# 1. 1 se lekar 9 tak ke numbers ko list mein store kiya
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 2. List ke har number par loop chalaya
for number in numbers:
    # 3. Agar number 1 hai, toh 'st' lagao (1st)
    if number == 1:
        print(f"{number}st")

    # 4. Agar number 2 hai, toh 'nd' lagao (2nd)
    elif number == 2:
        print(f"{number}nd")

    # 5. Agar number 3 hai, toh 'rd' lagao (3rd)
    elif number == 3:
        print(f"{number}rd")

    # 6. Baaki sabhi numbers (4 se 9) ke liye 'th' lagao
    else:
        print(f"{number}th")

