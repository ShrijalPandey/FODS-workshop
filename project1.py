
'''
PART-1
Translate the following statements into Python expressions in IDLE:
Note down the response to each. Do they differ from what you would expect?

The perimeter of a rectangle with length 9 & width 7

perimeter = 2 * (9 + 7)
print(perimeter)

Your name stored as a variable

my_name = "Shrijal Pandey"
print(my_name)

Python is great, it’s wild!

print("Python is great, it's wild!")

The difference between Beth’s age (57) and Tom’s (34)

age_diff = 57 - 34
print(age_diff)

2 to the 10th power

power = 2 ** 10
print(power)

7 factorial minus 5 factorial

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

factorial_of_seven = factorial(7)
factorial_of_five = factorial(5)

diff_of_factorials = factorial_of_seven - factorial_of_five
print("The difference between 7! and 5! is:", diff_of_factorials)

Your forename multiplied by 5

forename = "Pandey"
out_put = forename  * 5
print(out_put)

Your name left justified 15 spaces

name='Shrijal Pandey'
n_name=name.ljust(15)
print(n_name)

PI to 5 decimal places

import math
pi_value = round(math.pi, 5)
print(pi_value)

A variable with the name def that stores the number 7

def= 7
print(def)
#def cannot be used because it is a keyword.

200 modulus 12

result = 200 % 12
print(result)

7.2 as an integer value

inte = int(7.2)
print(inte)

The Unicode encoding for your name

name = "Shrijal Pandey"
for char in name:
    print(f"Unicode encoding for '{char}': {ord(char)}")


PART 2

1.Write a Python program that prompts the user for two integer values and displays the results
of the first number divided by the second, with exactly two decimal places displayed.

a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
print("Result is :", format((a/b), '.2f'))
        


2.Write a Python program that prompts the user for two floating-point values and displays the
results of the first number divided by the second, with exactly two decimal places displayed.

a = float(input("Enter first integer: "))
b = float(input("Enter second integer: "))
print("Result is :", format((a/b), '.2f'))
        

3.Write a Python program that prompts the user for two floating-point values and displays the
results of the first number divided by the second, with exactly two decimal places displayed in
scientific notation.

first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))

result = first / second
print("Result: {:.2e}".format(result))

4.Write a Python program that prompts the user to enter a UTF-8 value between 32 and 126,
and displays the corresponding character.

utf_value = int(input("Enter a UTF-8 value between 32 and 126: "))
if 32 <= utf_value <= 126:
    character = chr(utf_value)
    print("Corresponding character:", character)
else:
    print("Invalid input! Please enter a UTF-8 value between 32 and 126.")


PART 3

Define a function,

1.squared that take an integer and returns the value squared.

def squared():
    a=float(input("Enter a number whose square is to be found:"))
    print(a**2)
        
squared()

2. print_ast that takes an integer value n and a string value symbol, with a default value of "*".
This character should be printed n times to the console.

def print_ast():
    a=int(input("Enter the number of times you want to print *:"))
    result="*"*a
    print(result)
    
print_ast()

3. Create a function that prompts the user for two integer values and displays the results of the
first number divided by the second to two decimal places.

def result():
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
print("Result is :", format((a/b), '.2f'))

result()


4. Create a Python program called calculator with functions to perform the following arithmetic
calculations, each should take two decimal parameters and return the result of the arithmetic
calculation in question.
A. Addition
B. Subtraction
C. Multiplication
D. Division
E. Truncated division
F. Modulus
G. Exponentiation

first = input("Enter a number: ")
operator = input("Enter operator [+,-,*,/,//,%,**]: ")
second = input("Enter a number: ") 
first = float(first) 
second = float(second) 
if operator == "+":
    print('The sum is {:.2f}'. format(first + second))
elif operator == "-":
    print('The difference is {:.2f}'.format(first - second)) 
elif operator == "*": 
    print('The product is {:.2f)'.format(first * second)) 
elif operator == "/": 
    if second != 0: 
        print('The division is {:.2f}'.format(first / second)) 
    else: 
        print("Division by zero is not allowed!") 
elif operator == "//":
    if second != 0: 
        print( "The truncated division is {:.2f}".format(first // second))
    else: 
        print("Division by zero is not allowed!") elif operator == "%": 
    if second != 0:
        print('The modulus is {:.2f}'.format(first % second)) 
    else: 
        print("Division by zero is not allowed!") 
elif operator == "**":
    print('The exponentiation is {:.2f}'.format(first ** second))
else:
    print("Math Error") 
'''