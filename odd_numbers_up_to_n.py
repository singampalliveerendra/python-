number = (int(input("Up to which number you want to print odd numbers? ")))
counter = 1
print("The odd numbers up to", number, "are ", end="")
while (counter < number - 1):
    print(counter, end=", ")
    counter = counter + 2
print(counter, ".", sep="")

