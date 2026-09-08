
#
# Hum chahte hain ki sabhi logon ke naam print hon, lekin agar unme se koi
# mera dost (`phil` ya `sarah`) nikalta hai,  toh use ek special message
# mile jisme uski favorite language ka bhi zikr ho.

fav_lanaguage = {
    "rahul": "python",
    "prashik": "java script",
    "vishal": "c++",
    "pratik": "c",
    "abhisek": "html",
}

# mmene ek friend_list name ki list banayi jissme agar ye mere 2 name aaye to unko alag message
# milenga ..mere fav_langauge me ye 2 log aye to unko alag messagae milenga

friend_list = ["pratik", "prashik"]

for name in fav_lanaguage.keys():
    print(name.title())

    if name in friend_list:
        print("HI .."+ name.title()+" I see your Fav langauge "+ fav_lanaguage[name])

print() # space


team_A = {
    "gavrov": 900,
    "vishal": 400,
    "rahul": 560,
    "thomas": 500,
}

team_B = ["rahul", "thomas"]

for key in team_A.keys():

    if key in team_B:
        print(key.upper())
        print("hey.."+key.upper()+" your score is "+str(team_A[key]))

    elif key == "gavrov":
        print(key.upper())
        print("your score is very high..")

    elif key == "vishal":
        print(key.upper())
        print("your score is low...")

    else:
        print(key.upper())

# ye code khud ka hai isse samjhao

print()  # space

# this is a expample


play_group = {
    "vishakha": "c rank",
    "abhid": "d rank",
    "monar": "a rank",

}
# hum dekhe ghe ki vishal name ki key iss play gorup me hai ya nhi nhi hai to print karenga

if "vishal" not in play_group:
    print("please vishal join to play group..")

else:
    print("vishal not in the play group..")

print()  # space


# ex(2)

# Maan lijiye aap ek **Office Security System** bana rahe hain. Is dictionary mein employees ke
# `usernames` (Keys) hain aur unke `access_levels` (Values) hain.
# 1. Sabhi employees ka access status check karna hai, aur agar koi `Admin` group ka hai,
# toh use Special Access Alert dena hai.
# 2. Agar koi anjaan vyakti (Unknown User) system mein login karne ki koshish kare jo
# dictionary mein nahi hai, toh Security Alarm bajana hai.


office = {
    "vihshal": "admin",
    "prashik": "manager",
    "samrat": "chef",
    "rahul": "acting director",
}

print("=======  System security scan  =======\n")
for key in office.keys():    #  office ke nadar ke sare keys
    print("Scaning user : "+key.title())

    if office[key] == "admin":
        print(" ?? Alert : "+ key.upper()+ " Normal employee..")
        # agar office ke andar ek admin wala nikala to usko ke alert hai

    else:
        print("!! security .. unknown person in the office..")

    print("-" * 30)


guest_user = "thomas"
# agar guest user office me nahi hai to usse ye alarm bajega .. agar hai to to alag bajega

if guest_user not in office.keys():
    print(" \n! Access denied.. "+ guest_user.upper()+ " is not in office..")
    print("?? TRIGGERING SECURITY ALARM! LOCKING DOWN THE SYSTEM!")

else:
    print("Welcome back "+ guest_user.title())

# ye guest user wala part extra add kar diya agar office me thomas
# hai to ye if wala print honga  nhi hai to else wala print honga
print()  # space


