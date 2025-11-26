count = int(input("How many odd numbers you want to print? "))
counter = 1
print("The first", count, "odd numbers are", counter, end="")
while (counter < 2 * count - 2):
    counter = counter + 2
    print(", ", counter, sep="", end="")
print(".")
