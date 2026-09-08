
# LOOPING THROUGH A DICTIONARY.
    # Jab dictionary mein bahut saara data hota hai, tab har item ko alag-alag manually print
    # karna mushkil hota hai. Isliye hum for loop ka use karke dictionary ke sabhi
    # items ko ek-ek karke automatically access aur print karte hain.


# .ITEMS() METHOD
# : Dictionary ke andar se Key aur Value dono ko ek sath nikaalne ke liye items()
# mthod ka use hota hai

dic = {
    "sam": "samrat",
    "ram": "ramesh",
    "abhi": "abhishek",
}

for k, v in dic.items():
    print("\nkey : "+ k)    # issme \n se key and value ke bich me space banti hai
    print("value : "+ v)

print()  # space
# issme humne key and value dono print karvai hai

# ex :

fav_langauge = {
    "savrna": "python",
    "vishal": "c++",
    "diksha": "java",
    "rahul": "c langauge",
}

for name, langauge in fav_langauge.items():
    print(name.title()+"'s "+"favorate langauge is "+ langauge.title())

print()  # sapce

# extreme level :

    # Maan lijiye aap ek school ke liye system bana rahe hain, jahan alag-alag
    # students ke exam ke marks store hain. Hamein ek hi baar mein sabhi students ka
    # report card ready karna hai aur yeh bhi check karna hai ki kaun pass hai aur kaun fail!
    # pass and fail ke liye hum if elif ya else ka use karen ghe ..

# Dictionary: Isme Key student ka naam hai aur Value uske marks hain
class_results = {
    'rahul': 85,
    'sneha': 92,
    'amit': 32,    # Amit ke marks kam hain
    'priya': 78,
    'vikram': 40
}
 # condition agar marks 40 se uppar rahe to pass nahi to fail hum ye loop me conditions lagana
 # honga .. kyu ki pehle loop chalega phir jo 40 se kaam hai wo fail print honga ..

for name, marks in class_results.items():
    print("\nstudent : "+ name.title())
    print("scores : "+str(marks)+"/100")

     # Loop ke andar hum condition (if-else) bhi laga sakte hain!
    # agar marks 40 se jada rahe to pass nhi to fail

    if 40 < marks:
        print("status : PASS...💝💐🏆")

    else:
        print("status : FAILED...😔")
        print("please improvement your study...")

    print("-------------------------------------------------")  # akhri me line fene ke liye

print()   # space



# LOOPING THROUGH ALL THE KEYS IN A DICTIONARY
# : Jab humein dictionary ki sirf keys chahiye hoti hain aur values ki zarurat
# nahi hoti, tab hum .keys() method ka use karte hain.

langauge = {
    "vishal": "english",
    "pratiksha": "marathi",
    "abhijit": "hindi",
    "amar": "tamil",

}
  # issme ab pure key hi aayeghe ..
for key in langauge.keys():
    print(key.upper())

print()  # space

# agar apne .key() method ka bhi use nhi ki to python apko key hi print karke dena
for k in langauge:
    print(k.upper())

print()  # space
