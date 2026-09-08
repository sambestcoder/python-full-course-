# changing case with methods 

name = "samrat vijay kshirsagar "

print(name)  
             # ab jo varible me name hai wo print honga 

print(name.title())  
                   #' .title '  Ye method kisi bhi text ke har word ka pehla letter
                    # Capital kar deta hai.
print()  # sapce 

name2 = "mauli college khamgaon "
print(name2.title()) 
print() #space


# upper() Method  
# Ye poore text ko CAPITAL LETTERS mein badal deta hai.

name_3 = "mauli college khamgaon .."
print(name_3.upper())

name_4 = "king of the worlds "
print(name_4.upper())
print() #space

#  lower() Method
#  Ye poore text ko small letters mein badal deta hai

name_5 = "SAMRAT VIJAY KSHIRSAGAR ..."
print(name_5.lower())
print() #space

# combining and concateting strings

# Strings ko Jodna (Concatenation)
# Jab hum do ya do se zyada strings ko ek saath milate hain, toh use concatenation
#  kehte hain. Python mein iske liye plus symbol (+) ka istemal hota hai.

first_name = "samrat"
last_name = "kshirsagar"
full_name = first_name +" "+ last_name
print(full_name)

print(full_name.title()) # bade akashroke saath 
print() #space


# ADDING WHITESPCE TO STRINGS WITH TABES OR NEWLINES

# Tab (\t) ka Istemal
# Jab aapko text ke shuru mein thodi extra jagah chahiye ho (jaise ek paragraph shuru
# karte waqt hota hai), toh \t ka use karein.

print("samrat")
print("\tsamrat")  # ab samrat thoda aaghe likhe ga 
print("\t\t sam digital computer center ")  # ye usse thosda aaghe likh ta hai 
print() #space

# NEWLINES USE 

print("samrat \nkshirsagar")
print() #space

print("python \n javascript \n c++ \n htmk ")
print() #space

# WHITESPCE AND NEWLINES COMEBELING 

print("sam \n digital computerse \t center")
print() #space

print("vishal \n \t deshmukh ")
print() #space

# TRIPPING WHITESPACE
# iss me galat jada spce de diya to usse remove karta hai 
# rstrip() — Right Side se space hatana
# strip() — Dono side se space hatana
# lstrip() — Left Side se space hatana


obj = "samrat kshirsagar "
print(obj.rstrip())
print() #space

obj2 = "   digial computer center ..."
print(obj2)
print(obj2.lstrip())
print()   # sapce

obj3 = "   sam digital center   "
print(obj3)
print(obj3.strip())