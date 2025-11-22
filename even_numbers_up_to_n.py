number = (int(input("Up to which number you want to print even numbers? ")))
counter = 0
print("The even numbers up to", number, "are ", end="")
while (counter < number - 1):
    print(counter, end=", ")
    counter = counter + 2
print(counter, ".", sep="")
