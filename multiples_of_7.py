count = int(input("How many multiples of 7 you want to print? "))
counter = 1
print(f"The first {count} multiples of 7 are {7*counter}", end="")
while (counter < count):
    counter = counter + 1
    print(",", 7 * counter, end="")
print(".")

