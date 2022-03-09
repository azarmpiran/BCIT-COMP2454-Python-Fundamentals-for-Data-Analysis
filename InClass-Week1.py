# This is a InClass Exercise for Week 1 - Python for Data Analytics
# Azarm Piran

# Example 1:
# Writing Your First Program
# Print
print("Hello World")
print("Azarm")
print("My first name is: Azarm")

# Variable
firstName = "Azarm"
lastName = "Piran"

# Example2
# Python instructions. Comments begin with '#'.
# The variable 'age' stores a whole number.
age = 25

# The variable 'firstName' stores a String which is any character combination
# within quotes.
firstName = "Jane"
# The variable 'earnings' storas a floating point number.
earnings = 15.22
# The variable 'isBCITStudent' storas a Boolean value. Booleans in
# Python can be either True or False. They are useful for implementing
# logic.
isBCITStudent = True
print("Age: " + str(age))
print("First Name: " + firstName)
print("Earnings: " + str(earnings))
#Exercise4
age = 28
firstName = "Azarm"
lastName = "Piran"
earnings = 19.88
isBCITStudent = True
print(age)
print("Age:" + str(age))
print("First Name:" + firstName)
print("Last Name:" + lastName)
print(f"My name is {firstName} {lastName}. I am {age} years old and I got {earnings} in math course.")
print("My full name is: " + firstName + " " + lastName)
#Example3
# Declare and initialize variables.
A = 5.3;
B = 4.2;
C = 6.0;
# output original values.
print("A = " + str(A)); # Outputs 'A = 5.3'
print("B = " + str(B));
print("C = " + str(C));
# Perform calculation
result = A + B;
# output the string value
print("A + B = " + str(result));
#Exercise5
A = 5.3
B = 4.2
C = 6.0
result = (A + B)*C
print(result)
print("Result is: " + str(result))
print(f"The result is {result}")
#Exercise6
A = 48
A = A - 1
print("A = " + str(A))
A = 48
A -= 1
print("A = " + str(A))
#Exercise7
A = 23
B = 5
C = A % B
print(f"The reminder of {A} devided by {B} is equal to {C}")
print(str(A) + " % " + str(B) + " = " + str(C))
#Example4
def showApplicationTitle():
    title = "THIS APPLICATION SHOWS HOW TO USE FUNCTIONS"
    print(title)
# This instruction *calls* our function.
showApplicationTitle()
#Example5
def showFullName(firstName, lastName):
    print(f"My full name is {firstName} {lastName}")
showFullName("Azarm","Piran")
showFullName("Roya","Oskuee")
#Exercise8
def showFullName(firstName,middleName,lastName):
    print(f"My full name is {firstName} {middleName} {lastName}")
showFullName("Jane","Jenny","Jones")
showFullName("Azarm","","Piran")
showFullName("Roya","Saee","Oskuee")
#Example6
def addTwoNumbers( operandA, operandB ):
   result = operandA + operandB;
   return result; # This return statement exits the function and gives a value
                  # to the calling instruction.

sum = addTwoNumbers(3,4) # This is the calling instruction.
print("The result from adding 3 and 4 is " + str(sum))
#Exercise9
#I created a global variable in the function
#to be able to have access to the amount of celsius outside of the function to print
def convertTemp(celsius):
    global x
    x = celsius
    result = (celsius * 9/5) + 32
    return result
fahrenheit = convertTemp(101)
print(f"{x}°C is equal to {fahrenheit}°F")
#Example7
a = 33
b = 32
# First conditional block
if b > a:
    print("b is greater than a")
# Otherwise if a equals b
elif a == b:
    print("a and b are equal")
# This condition is entered if all previous blocks are not selected.
else:
    print("* Program output *")
    print("b is less than a")

#Exercise10
def showLetterGrade(percentage):
    if percentage >= 90:
        end = "A"
    elif 80 <= percentage < 90:
        end = "B"
    elif 70 <= percentage < 80:
        end = "C"
    elif 60 <= percentage < 70:
        end = "D"
    elif 50 <= percentage < 60:
        end = "F"
    else:
        end = "Failed"
    print("The grade " + str(percentage) + " is " + end + ".")
showLetterGrade(95)
showLetterGrade(72)
showLetterGrade(51)

#Example8
a = 33
b = 32
if(a>32 and b>32):
    print("Both 'a' and 'b' are above freezing.")
elif(a<=32 and b<=32):
    print("Both 'a' and 'b' are freezing.")
elif(a<=32 or b<=32):
    print("Only one of 'a' and 'b' are freezing.")
#Exercise11
def showMedicalStatus(firstName, age, highBloodPressure):
    medicalAlert = f"Medical alert: {firstName} see a doctor"
    message = f"{firstName}, you are in good helath. See you next checkup"
    warning = f"Warning: {firstName}, seeing a doctor is recommended"
    if( age >= 55 and highBloodPressure == True):
        print(medicalAlert)
    elif( age < 55 and highBloodPressure == True):
        print(warning)
    else:
        print(message)

showMedicalStatus("Bob", 60, True)
showMedicalStatus("Jane", 60, False)
showMedicalStatus("Brad", 28, True)
print("\n")
showMedicalStatus("Azarm", 28, True)
showMedicalStatus("Azarm", 75, True)
showMedicalStatus("Azarm", 28, False)
showMedicalStatus("Azarm", 75, False)




