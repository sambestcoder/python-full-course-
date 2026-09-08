
#   OMITTING THE ELSE BLOCK
#  : Pehle hum aakhiri condition ke liye else: ka use kar rahe the agar upar ki saari
#  conditions fail ho gayin, to jo kuch bhi bacha, woh else ke andar chala jayega.
# Isme ek dikkat hai: Agar kisi ne galat data (jaise koi invalid  input)
# daal diya, to else block bina soche-samjhe chal jayega.  Isse bachne ke liye,
# hum else ki jagah ek aur elif laga kar specific condition check kar  sakte hain:

age = 14

if(age < 13):
    price = "-ve"
elif(age >= 17):
    price = "+ve"
elif(age <= 12):
    price = "-ve"
elif(age <= 15):
    price = "+ve"

print("Your price is .. "+str(price)+". ")
print() ## space


# . TESTING MULTIPLE CONDITIONS
#  :  Lekin agar aisi situation ho jahan ek se zyada cheezein True ho sakti hain aur
#  hamein un sabhi par kaam karna hai, to hum elif nahi lagate. Hum alag-alag,
#  independent if statements likhte hain.

car_list= ["roylroyal", "mg dragon", "R15", "BMW"]

if "roylroyal" in car_list:
    print("your car is very nice....")
if "mg dragon" in car_list:
    print("your bike is very nice..")
if "R15" in car_list:
    print("your bike is very nice..")
if "BMWR" in car_list:
    print("your car is very nice...")    # ye wali condion false hai to ye nhi print honga..

print("\n what is price in this Car/BIke ?")
print()  # space

# issme sari conditons true hai to if chalega hi agar issme ek bhi condtion false niklti
#   hai to agge ki condiitons check hongi..

# ex : check karna hai ki alien ka color 'green' hai ya nahi. Agar hai,
#          to points milenge, nahi to kuch nahi hoga.


alien = "green"

if(alien == "yellow"):
    print("congratutional you are win 10 points ...")
            # ye confdition wrong hai to kuch print nhi honga

# Alien ka color green set kiya
alien_color = 'green'
# Check kar rahe hain ki kya color green hai
if alien_color == 'green':
    print("Congratulations! You just earned 5 points.")
print()  # space


# FAVORITE FRUIT (INDEPENDENT IF STATEMENTS)
    #     Jab humein ek list me se multiple cheezein check karni hoti hain
    # (aur ek se zyada True ho sakti hain), to hum elif nahi use karte.
    # Uski jagah alag-alag if statements use karte hain taaki har condition alag se check ho sake.

fav_fruits = ["mango", "apple", "banana"]

if "mango" in fav_fruits:
    print("My favorite friuts is mango")
if "panapple" in fav_fruits:
    print("My favorite friuts is panapple")
if "banana" in fav_fruits:
     print("My favorite friuts is banana")
if "orange" in fav_fruits:
    print("My favorite friuts is orange")

print() # space
# jo mere fav_fruits ke andar hai vahi print honga


#     USING IF STATEMENTS WITH LISTS
#  :  pizza banane ka code hai jahan hum loop chala kar customer ki
#  saari toppings(saman pizza me dalne ka)  pizza me add kar rahe hain. ek problem aati hai:
#   green peppers khatam ho gaye hain! Ab hamein loop ke andar ek if
#  condition lagana padega taaki jaise hi 'green peppers' aaye, hum customer ko
# 'Sorry' bol sakein, aur baaki  toppings randomly add kare toppings randomly add kare

toppings = ["mashroom", "green peppers", "extra chees"]

for k in toppings:
    if k == "green peppers":
        print("sorry, we are out of green peppers right now..")
    else:
        print("adding .."+str(k)+ ". ")

print("\nfished pizza program ...")
print()  # sapce

# explaintion : Loop pehle mushrooms par gaya. if ne check kiya: kya mushroom
# green pepper hai? No. Python else me gaya aur print kiya: Adding mushrooms.
# Loop doosre item green peppers par aaya. if ne check kiya: kya ye
# green pepper hai? Yes! (True). Python ne if ke andar ka code chalaya
# aur bola: Sorry, we are out of green peppers right now. Aur else ko skip kar diya.
# Loop teesre item extra cheese par gaya. Condition fir se False hui, to else
# chala: Adding extra cheese.

cars = ["kawasake ninija", "r15", "bullet", "faraari"]

for k in cars:
    if k == "kawasake ninija":
        print("kawasake ninija is not availbe .. ")
    else:
        print("availbe : "+str(k)+ ". ")

print("all cars are availbles..")
print()  # space

# k mera sab ke paas jayega agar kawasake ninija par ayega to print honga ki mere pass kawasake ninja
# nhi hai baki jitn bhi cars hai wo prints ho jayegi














