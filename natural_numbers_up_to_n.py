count = int(input("Upto which number you want to print natural numbers? "))
counter = 1
print("The first", count, "natural numbers are ", end="")
while (counter < count):
    print(counter, end=", ")
    counter = counter +1
print(counter, end=".\n")
