
# example

# CODE :

# def send_remider(name):
#
#     for key in name:
#         print("Reminder: ", key.title(), ", apka exam kal hai ")
#
# list = ["samrat", "vishal", "harry", "prakash"]
#
# send_remider(list)




# MODIFYING LIST IN FUNCTION :

# meaning :
# ab list function ke andar modify hoti hai, to woh changes permanent hote hain,
# original list par bhi reflect hote hain. Isse bada data efficiently handle
# karna easy ho jaata hai (kyunki puri list ko copy nahi karna padta).


# Items ki ek list banayi hai.
# Finished items ko store karne ke liye ek empty list banayi hai.
# while loop tab tak chalega jab tak items list empty nahi ho jaati.
# pop() list ke last item ko remove karke current_item mein store karega.
# Processed item ko finished_items list mein add kiya jayega.
# Sabhi items complete hone ke baad for loop se finished_items ko ek-ek karke print karenge.


# code :

# items = ["pen", "pencil", "book", "laptop"]
#
# finished_items = []
#
# while items:
#
#     current_item = items.pop()
#
#     print("Processing item:", current_item)
#
#     finished_items.append(current_item)
#
#
# print("\nThe following items are completed:")
#
# for item in finished_items:
#     print(item)



# ab isko 2 function me thod ke likh te hai matalb 2 funiton me likh te hai

# Ye Python ka ek important principle hai: "Har function ek hi specific kaam kare"
#
# print_models() sirf printing simulate karta hai
# show_completed_models() sirf result dikhata hai


def print_items(items, finished_items):

    while items:

        # items ke last element ko nikalo aur current_items mein store karo.
        current_items = items.pop()

        print("Processing items :" + current_items)
        finished_items.append(current_items)
        # ab aakhri ek elemnts ek ek karke finished item me jayege \

# ek funiton banaya show karne ke liye

def show_items(finished_items):

    print("\nthe following items are complited..")

    # ye sare finished items ke sare elements ko print karenga
    for k in finished_items:
        print(k)




# items and finished items ko define karna
items = ["pen", "pencil", "book", "laptop"]

finished_items = []

# funtion 1 ko call karna
print_items(items, finished_items)

# funtion 2 ko call karna
show_items(finished_items)

print("\n\n") # sp


# example 2


def mark_present(student):
    """Har student ka naam print karke bataye ki wo present hai."""

    for k in student:
        print(k.title() + "is present today")

def move_to_absent(present_list, absent_list):
    """Ek student ko present list se absent list mein move karo."""

    student = present_list.pop()
    absent_list.append(student)

    print(student.title() + " has been marked absent ")
    # jo last ka element honga ho print honga


# original list

student = ["rahul", "abhishek", "raaj", "vishal"]

# function 1 sab ko p[resent bolo
mark_present(student)

# funciton 2 : student list ko midify karo

absent_student = []
move_to_absent(student, absent_student)


print("\nStudents still in class list:", student)
print("Students moved to absent list:", absent_student)


print("\n\n")  # sp


