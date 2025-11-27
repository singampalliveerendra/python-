count = int(input("Up to which number you want to print the N power N series? "))
counter = 2
result = 1
print(f"The N power N series up to {count} is 1", end="")
while (result <= count):
    result = 1
    counter1 = 1
    while (counter1 <= counter):
        result = result * counter
        counter1 = counter1 + 1
    if (result <= count):
        print(f", {result}", end="")
    counter = counter + 1
print(".")

