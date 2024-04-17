#The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.

#Task 1: Create functions for each arithmetic operation.
#Task 2: Implement user input to receive numbers and an operation choice.
#Task 3: Ensure your program can handle division by zero and other potential errors.

first = True
sol = 0

def add(int_list):
    for num in range(len(int_list)-1):
        sol = int_list[num] + int_list[num+1]
    return sol

def sub(int_list):
    for num in range(len(int_list)-1):
        sol = int_list[num] - int_list[num+1]
    return sol

def mult(int_list):
    for num in range(len(int_list)-1):
        sol = int_list[num] * int_list[num+1]
    return sol

def div(int_list):

    for num in range(len(int_list) - 1):
        if int_list[num+1] != 0:  # Check for division by zero
            sol = int_list[num] / int_list[num+1]
        else:
            print("Error: Division by zero!")
            return None
    return sol
    


print("Welcome to the calculator.")

while True:
    number = int(input("Please enter a number to use in your calculation. "))
    if first == True:
        num_list = [number]
        number2 = int(input("Please enter another number to use in your calculation. "))
        num_list.append(number2)
        first = False

    choice = input("Would you like to use another number in your calculation? Y or N ")
    if choice == 'Y':
        pass
    elif choice == 'N':
        calc_choice = input("What calculation would you like to perform? Choices: Addition, Subtraction, Multiplication, Division. ")
        if calc_choice == 'Addition':
            print('Result is: ', add(num_list))
        elif calc_choice == 'Subtraction':
            print('Result is: ', sub(num_list))
        elif calc_choice == 'Multiplication':
            print('Result is: ', mult(num_list))
        elif calc_choice == 'Division':
            print('Result is: ', div(num_list))

        end_choice = input("Would you like to make another calculation? Y or N ")
        if end_choice == 'Y':
            pass
        else:
            break

    else:
        print('Unrecognized input.')
