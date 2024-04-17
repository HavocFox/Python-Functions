#Objective: The aim of this assignment is to analyze a set of grades and provide statistics.

#Task 1: Code a function to calculate the average grade.
#Task 2: Implement a function to find the highest and lowest grade. 

grades = [85, 92, 78, 95, 87, 89, 45, 66, 69, 92, 12]

def average():
    avg = sum(grades)/len(grades)
    return round(avg)

def hilo():
    grades.sort(reverse = True)
    hi = grades[0]
    lo = grades[len(grades)-1]
    return hi, lo

print("Welcome to the grade calculator. \n" )
print("Given the following list of grades: ")
print(grades, '\n')

print("The average of these grades is: ", average())
print("The highest and lowest of these grades are: ", hilo())