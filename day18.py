
# LOOPING THROUGH ALL VALUES IN A DICTIONARY
# : agar dictinary me value ko print karna ho to value()  method ka use kiya jata hai ..
# isse sirf value hi nikalti hai ..

fav_langauge = {
    "sumit": "English",
    "vishal": "marathi",
    "abhimanyu": "hindi",
    "kartik": "france",
}

for value in fav_langauge.values():
    print(value.upper())

print()  # space

fav_langauge = {
    "sumit": "English",
    "vishal": "marathi",
    "abhimanyu": "hindi",
    "kartik": "france",
    "pranav": "English",  # pranav ne english ko repet kiya hai

}

# Python mein set() ek aisi data structure hoti haijisme **koi bhi item repeat
# nahi ho sakta issko hamesha bahar hi likhte hai .. iss dictinary me value jo bar bar
# likhi gayi hai wo repet nhi hoti hai

for value in set(fav_langauge.values()):
    print(value.upper())

print()  # space

# example :

glossary = {
    "varibles": "varibles is a container and it is used to store the data..",
    "string": "string writen inside the double / single quotes",
    "intger": "integer is a whole number without decimal point ",
    "Loop": "loop is the way to run code repeatedly",
    "list": "collection of items stored in oder",
    "Boolean": "A value that is either True or False.",
    "Float": "A number with a decimal point.",
    "Comment": " A note in code that Python ignores.",
    "Function": "A reusable block of code that performs a specific task.",
}

for words , meaning in glossary.items():
    print("words : " + words)
    print("meaning : "+ meaning + "\n")

print()   # space

# example (2) :
#   Rivers: Make a dictionary containing three major rivers and the country
# each river runs through . One key-value pair might be 'nile': 'egypt' .
#  •	Use a loop to print a sentence about each river, such as The Nile runs  through Egypt .
#  •	Use a loop to print the name of each river included in the dictionary .
#  •	Use a loop to print the name of each country included in the dictionary

# matlab :

# Is exercise me hum seekhenge ki agar hume sirf Keys (rivers) chahiye ya sirf Values (countries)
# chahiye, toh kaise nikaalte hain.
# Sirf Keys ke liye: .keys() ya fir normal loop.
# Sirf Values ke liye: .values()

rivers = {
    "niles": "france",



    "ganga": "india",
    "jamuna": "india",
    "amazon": "brazil",
}
print("======== RIVERS AND CONTERIES ========")

for river, contries in rivers.items():
    print(" RIVERS : "+ river+",  conteries : "+ contries)

print()  #sp



