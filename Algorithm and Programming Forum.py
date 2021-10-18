#1) Ask the user to enter a numerator and denominator. Use input validation to ensure that both the numerator and denominator are positive. (Note: 0 is not considered positive.)
#2) Calculate the greatest common divisor (gcd) using the gcd function from the math module. The function can be used as:
# math.gcd(a,b) where a and b are the numerator and denominator respectively. Don’t forget to include the math module!

#For number 3 - 7 (You may or may not follow this, this is just a "guide" to help you solve the problem. Do not restrict yourself to follow this, be creative and solve the problem as you see fit.

#3) Create an (outer) if else statement that determines whether the fraction is proper or improper. If the fraction is proper, display the fraction and state that it is proper; otherwise, it is improper.
#4) Create a nested if else statement - within the if clause of part 3 - to check if the proper fraction can be reduced. If it can’t, display a message indicating that the proper fraction can’t be reduced; otherwise, reduce the fraction and display the reduced form.
#5) In the else clause of part 3, create another nested if else statement to check if the improper fraction can be reduced. Once again, if it can’t, display a message indicating that the improper fraction can’t be reduced; otherwise, reduce the fraction and display the reduced form.
#6) The improper fraction must be converted to a mixed number, regardless of whether the it can be reduced. Use integer division and the modulus to calculate the mixed number. (This calculation is necessary in both the nested if and else clauses in part 5.)
#7) Finally, if the fractional portion of the mixed number is 0, only display the whole number (i.e. do not display a fraction as 0 / b). Use another nested if else statement to display the mixed number appropriately. (This nested if else statement should also be in both the if and else clauses in part 5, after calculating the mixed number.)

import math

numerator = eval(input("Enter a numerator:"))
while numerator < 1:
    print("Numerator must be greater than 0")
    numerator = eval(input("Please re-enter the numerator, value must be greater than 0:"))
else:
    denominator = eval(input("Enter a denominator:"))
    while denominator < 1:
        print("Denominator must be greater than 0")
        denominator = eval(input("Please re-enter the denominator, value must be greater than 0:"))

gcd= math.gcd(numerator,denominator)

if numerator < denominator:
    print(numerator, "/",denominator,"is a proper fraction")
    if gcd == 1:
        print ("This proper fraction cannot be reduced any further")
    else:
        print("This proper fraction can be reduced:", numerator/gcd, "/", denominator/gcd)
        if numerator > denominator:
          print(numerator, "/" , denominator, "is an improper fraction")
          if gcd == 1:
              print("This improper fraction cannot be reduced any further")
          else:
              print("(numerator)/(denominator) is an improper fraction")
whole_number = numerator // denominator
Remainder= numerator % denominator
if gcd == 0:
    print("The whole number is", numerator//denominator)
else:
    print("The mixed number is", numerator// denominator, "and",numerator// denominator - numerator//denominator * denominator// gcd )






