
# get_formatted_name() function first name + last name ko jodta hai aur .title()
# se first letters capital karta hai. while True program ko baar-baar chalata hai. User se
# First name input leta hai.  Agar user q likhe → break se
# program band ho jata hai. Phir Last name leta hai; q ho to program band.
# Function dono names ko format karta hai. Finally "Hello, Name!" print hota hai
from day9 import marks

# code :

def get_formatted_name(first_name, last_name):
    full_name = first_name+" "+last_name
    return full_name

while True:
    f_name = input("enter the first name : ")
    if f_name == "quit":
        break  # agar mene quit likha to while loop khatam ho jayega

    s_name = input("enter the last name : ")
    if s_name == "quit":
        break

    varible = get_formatted_name(f_name, s_name)
    print() # sp
    print("hello, ", varible)

print("\nyou are press quit then program are exit...")

print("\n\n") # sp


# example 2

#code :

# Function banaya: student ka name, subject aur optional marks lega
def student_class(stu_name, stu_subject, stu_marks=None):
    student = {
        "student name ": stu_name,
        "student subject ": stu_subject
    }

    # Agar marks diye hain, to dictionary me add karo
    if stu_marks:
        student["student marks "] = stu_marks

    return student


while True:

    print("\n===== Student record entry =====")
    print("enter ( quit ) at any time to exit...")

    name_input = input("\nenter the student name : ")

    # Name me "quit" dala to loop se bahar aa jao
    if name_input == "quit":
        break

    subject_input = input("enter the student subject : ")

    # Subject me "quit" dala to loop se bahar aa jao
    if subject_input == "quit":
        break

    marks_input = input("enter the student marks : ")

    # Marks me "quit" dala to loop se bahar aa jao
    if marks_input == "quit":
        break

    # Agar marks diye hain, to integer me convert karke function ko bhejo
    if marks_input:
        student = student_class(
            name_input,
            subject_input,
            stu_marks=int(marks_input)
        )
    else:
        # Agar marks nahi diye, to marks ke bina record banao
        student = student_class(
            name_input,
            subject_input
        )

    # Student ka record print karo
    print("\nstudent records :")

    for key, value in student.items():
        print(key, ": ", value)


# Ye line tab chalegi jab while loop break hoga
print("\nAll record entered program closed")


print("\n")  # sp





# PASSING A LIST
#
# MATLAB:
# Jab hum kisi list ko function ke argument ke roop me pass karte hain,
# to function us list ke elements ko access kar sakta hai.
# Function ke andar hum list par loop chala sakte hain
# aur list ke har element ke saath alag-alag kaam kar sakte hain.

def greet_user(names):
    # List ke har element ko ek-ek karke access karna
    for key in names:
        # Har name ko uppercase me convert karke print karna
        print("Hello, " + key.upper())


list = ["vishal", "prashik", "abhimanyu"]

# List ko function me pass karna
greet_user(list)

print() # sp






























