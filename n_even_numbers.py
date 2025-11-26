count = int(input("How many even numbers you want to print? "))
counter = 0
print(f"The first {count} even numbers are {counter}", end="")
while (counter < 2 * count - 2):
    counter = counter + 2
    print(f", {counter}", end="")
print(".")
