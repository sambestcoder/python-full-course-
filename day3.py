# AVODING TYPE ERROR IN STR()  FUNCTION

# Python mein jab aap do alag tarah ka data ek saath
# jodte hain (jaise Text + Number), toh Python confuse
# ho jata hai. iss liye error deta hai

age =  18
name = "sam kshirsgar "
percentage = 78.9

#  print(name + age + percentage)... error denga
print(name + str(age) + " "+str(percentage))
print()  # space

age2 = 67
name2 = "sanket gawai "
print(str(age2) + name2)
print()  # space

