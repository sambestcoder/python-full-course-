# exersise :
# : Write a program that asks the user how many people
# are in their dinner group . If the answer is more than eight, print a message say
# ing they’ll have to wait for a table . Otherwise, report that their table is ready
from pygame.examples.moveit import GameObject

# people = int(input("kitne log hai group me : "))
#
# if people > 8:
#     print("they all have to wait for a table ...")
#
# else:
#     print("Their table is ready ...")
#
# print()  # sp



# FLAG
# : Flag ek special variable hota hai jo program ko ek signal deta hai.
# Isme hum True ya False (Boolean value) store karte hain.
# Loop tab tak chalta hai jab tak flag True hota hai, aur flag False hone
# par loop ruk jata hai.

# EXAMPLE 1: FLAG KA USE KARKE (GAME ACTIVE/INACTIVE)

# Humne ek flag banaya 'game_active' naam ka
# agar ye false ho jata to game rukh jata



# promt = "\n koi name likho ya game 'exit' karne ke liye exit lkho :  "
# game_active = True
#
# while game_active:
#     user_name = input(promt)
#
#     if user_name == "exit":
#         print("game over...")
#         game_active = False
#
#     else:
#         print("tumne type kiya : "+user_name)
#
print()

#  USING BREAK TO EXIT A LOOP
#  : break ek statement hota hai jo loop ko turant rok deta hai. Hum ise aksar while True
#  jaise infinite loop ke sath use karte hain, taaki condition milte hi loop band ho jaye.

# defination : The work of break is to stop the loop in the middle itself
#               (Break ka kaam loop ko beech me hi stop karna hota hai.")


promt = "aap kis city me rahte ho ?  (Band karne ke liye 'quit' likhein) : "

# while True ka matlab hai yeh loop chalta hi rahega jab tak break na mile
# isko rokh ne ke liye barmunda gaon ka name type karna
# issme true ko false karne ki jarurat nhi hai .. to direct break lagao code ko rokhne ke liye


# while True:
#     user_input = input(promt)
#
#     if  user_input == "barmunda":
#         print("ruk jao ye shehar mere pehchan ka hai ...")
#         break
#         # agar mene break nhi laga ya to ye code stop nhi honga chalega hi
#
#     print(" great the "+ user_input+ "  place" )
#
# print("loop ke bahar code chal raha hai ")
#
# print()  # sp




# USING CONTINUE IN A LOOP
# : continue ek statement hota hai jo loop ke current iteration ko skip karta hai aur loop ko agali
# iteration par bhej deta hai. Yeh loop ko band nahi karta, sirf us
# round ka baaki code chhod deta hai.

 # defination : Continue ka kaam current round skip karke next round par jana hota hai."

# Example 1: CONTINUE KA USE
# Agar hume 1 se 5 tak numbers print karne hain, lekin Even Numbers (2, 4) ko skip
# karna hai, toh hum continue ka use karte hain. Jab even number milta hai, loop us number
# ka code skip karke next number par chala jata hai


number = 0

while number < 5:
    number += 1  # Har chakkar mein number 1 se badhega

    # Agar number 2 se poora divide ho jaye (Even number)
    if number % 2 == 0:
        continue
        # Yeh line bolti hai: "Neeche mat jao, turant upar agle round pe bhago!"

    print("Odd  number  : " + str(number))
 print()   # sp








