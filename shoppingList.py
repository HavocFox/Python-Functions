#Objective: The aim of this assignment is to create a program that helps users make a shopping list.

#Task 1: Write a function that lets the user add items to a list until the user replies "stop", and then returns the shopping list.
#Task 2: Include a feature to remove items from the list.
#Task 3: Add a feature that prints out the entire list in a formatted way.

def add():
    added_item = input("What would you like to add? ")
    shopping_list.append(added_item)

def remove():
    remove_item = input(("What item do you want to remove? "))
    if remove_item in shopping_list:
        shopping_list.remove(remove_item)
    else:
        print("That item isn't in the list. ")
    
def printH():
    print("Here is your list: ", shopping_list)
    print("Enjoy your shopping trip!")
    
def printV():
    print("Here is your list: ")
    for num in range(len(shopping_list)):
        print('*', shopping_list[num])
    print("Enjoy your shopping trip!")

shopping_list = []
print("Let's make a shopping list! ")

while True:
    choice_intro = input("Would you like to add or remove an item? Reply 'stop' to stop doing so. ")
    if choice_intro == 'add':
        add()

    elif choice_intro == 'remove' and len(shopping_list) == 0:
        print("There's nothing in the list to remove! ")

    elif choice_intro == 'remove' and len(shopping_list) != 0:
        remove()
 

    elif choice_intro == 'stop':
        print_choice = input("Would you like your list formatted vertically or horizontally? ")

        if print_choice == 'horizontally':
            printH()
            break

        elif print_choice == 'vertically':
            printV()
            break

        else:
            print("That's not a valid format. ")
            printH()
            break