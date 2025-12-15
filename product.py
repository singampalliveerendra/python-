#print("To multiply three numbers.")
#num1 = int(input("Enter the first number: "))
#num2 = int(input("Enter the second number: "))
#num3 = int(input("Enter the third number: "))
#product = num1*num2*num3
#print("The product of ", num1, ", ", num2, " and ", num3, " is ", product, sep="", end=".\n")

import sys
if len(sys.argv) != 4:
    print("Usage: python3 product.py num1 num2 num3")
    sys.exit(1)
print("To multiply three numbers.")
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
num3 = int(sys.argv[3])
product = num1*num2*num3
print("The product of ", num1, ", ", num2, " and ", num3, " is ", product, sep="", end=".\n")



