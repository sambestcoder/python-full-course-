# NESTING
# : Nesting ka matlab hota hai "ek cheez ke andar doosri cheez ko rakhna
# : Nesting means placing one thing inside another. is calles as nesting

# there are three types of nesting :
# A List of Dictionaries: Ek badi List ke andar bohot saare Dictionaries rakhna.
# A List inside a Dictionary: Ek Dictionary ki value ke roop me poori List rakhna.
# A Dictionary inside a Dictionary: Ek Dictionary ke andar doosri Dictionary rakhna.

# mene three dictionary banaye .. innko ek list me karna hai ..
# Ab in teeno ko ek 'aliens' naam ki badi list me pack kar diya


alien_0 = {"colour": "green", "points": 90}
alien_1 = {"colour": "yellow", "points": 67}
alien_2 = {"colour": "red", "points": 20}

alien = [alien_0, alien_1, alien_2]

for k in alien:
    print(k)

print()  # sp

# PART 2: AUTOMATICALLY 30 ALIENS BANANA  (USING RANGE())
# Upar wale tarike me agar 30 ya 100 aliens banane hon, to baar-baar variable likhna boring
# ho jayega. Isliye hum range() loop ka use karke auto-generate karte hain.


# Ek khali (empty) list banayi jisme saare aliens rakhenge
aliens = []

for k in range(30):
    new_alien = {"colour": "green", "points": 50, "speed": "slow"}

    aliens.append(new_alien)
# issme 30 ke range ke hisab se alien bane ghe and 'aliens' me append ho ajyeghe

# aliens[:5]: Isko Slicing kehte hain. Iska matlab hai index 0 se lekar 4 tak
# (pehle 5 items) ko select karna.
# jayse humne range 30 li hai to ye 30 aliens ke data ko nhi print karenga ye sirf 0 se lekar 5
# tak ke aliens ke data ko print karenga..

for k in aliens[0:5]: # ab ye alies ke list se 5 aliens ke data ko bhi print karenga..
    print(k)

print("\ntotal aliens : "+str(len(aliens)))
print()  # sp


# AB SPECIFIC ALIENS MODIFY (GAME LEVEL)
#   matlba ab jo coda banaye aliens ka usse modify karna hai

for k in range(30):
    new_alien = {"colour": "green", "points": 50, "speed": "slow"}

    aliens.append(new_alien)

# AB UPDATE KARNA HAI:
# Humne sirf pehle 3 aliens ko select kiya using slice [0:3]

for k in aliens[0: 3]:
    if k["colour"] == "green":
        k["colour"] = "yellow"
        k["points"] = 100
        k["speed"] = "fast"


for k in aliens[0 : 5]:
    print(k)

# ab iss me alien ka coulur mix hai kisi ka yeelow hai kisi ka blue hai
# ab humne alien ka coluur red karna hai

#Upar wale example me humne sirf Green aliens ko Yellow banaya tha. Lekin game me
# aisa bhi to ho sakta hai ki jo pehle se Yellow hain, wo aur khatarnak hokar Red ban jayein!
# Yahan kaam aata hai elif (else if).

for k in aliens[0: 5]:
    if k["colour"] == "green":
        k["colour"] = "yellow"
        k["points"] = 100
        k["speed"] = "fast"
    # ye upper se ccondition ko wayse hi copy kiya hai
    # ab mujhe isse change karna ho to elif ka use karunga

    elif k["colour"] == "yellow":
        k["colour"] = "red"
        k["points"] = 150
        k["speed"] = "very fast"


for k in aliens[0 : 5]:
    print(k)