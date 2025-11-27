count = int(input("Enter a number to compute it's factorial: "))
counter = 1
fact = 1
while (counter <= count):
    fact = fact * counter
    counter = counter + 1
print(f"The factorial of {count} is ", end="")
print(fact, end=".\n")
