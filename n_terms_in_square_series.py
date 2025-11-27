count = int(input("How many terms you want to print in the square series? "))
counter = 1
print(f"The first {count} terms in the square series are {counter}", end="")
while (counter < count):
    counter = counter + 1
    print(",", counter*counter, end="")
print(".")
