#.…......…Random Number guessing game.................

import random
# random ka use python kuch random dene ke liye karta hai

computer = random.randrange(1, 100)
# ab iss me  computer hai 1 se lekar to 100 tak number chunega

user = int(input(" Enter the your number : "))

if computer > user:
    print("The Computer Number is high ..", computer)
    print("your Number : ", user)

elif computer < user:
    print("The Computer Number is low ..", computer)
    print(" YOU ARE WINNER...")
    print("your Number : ", user)

else:
    print("The computer Number is Equal to the Your number :")
    print("your Number : ", user)
    print("computer Number :", computer)