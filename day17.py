

# LOOPING THROUGH A DICTIONARY’S KEYS IN ORDER

# Python mein jab hum loop chalate waqt `.keys()` ke bahar `sorted()` laga dete hain,
# toh Python pehle saari keys ko uthakar unhe **A to Z** ke order mein saja deta hai
#agar humen dictinary ke keys ko alphabetical order me lagana hai to sorted() function ka
# use karna honga

fav_langauge = {
    "sumit": "English",
    "vishal": "marathi",
    "abhimanyu": "hindi",
    "kartik": "france",
}

for key in sorted(fav_langauge.keys()):
    print(key.upper() + ", how are you .. ?")
 # ab ye sare key alphabetical order me lagen ghe ..

# game Tornament example :
# : ek game tornament hai isse me bahut sae logo ne particiet kiya hai unno ne scores
# bhi kiya hai ab hum sorted() ka use kar ke inn ke name me aphabetical order se lagaye
# ghe ..

tournament_score = {
    "vishal": 900,
    "abhijit": 700,
    "raaj": 450,
    "amit": 950,
    "harsh": 400,
}

print("\n\n======= Game Tournament score =======")

for key in sorted(tournament_score.keys()):
    value = tournament_score[key]
      # srt(tournament_score[key]) iss ka matlba direct
      # dictionary ke value ko access karta hai ..
    print("\nplayer name : "+key.title())
    print("player score : "+ str(value))

    # ek chotisi conditions laga dete hai
    # agar player ka score 500 se grether than nikala to pro player.. nhi to average player
    if value > 500:
        print(" !! pro player..")

    else:
        print(" average palyer ..")

    print("-"*40)

print()  # space
