count = int(input("Enter a number to compute the power of itself: "))
counter = 1
result = 1
print(f"{count} to the power of {count} is ", end="")
while (counter <= count):
    result = result * count
    counter = counter + 1
print(result, end=".\n")

