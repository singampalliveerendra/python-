count = int(input("Up to which number you want to print natural numbers? "))
counter = 1
print("The first", count, "natural numbers are ", counter, end="")
for counter in range(counter + 1, count + 1, 1):
    print(f", {counter}", end = "")
print(".")
