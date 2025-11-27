count = int(input("Up to which number you want to print the N power N series? "))
counter = 1
result = 1
power = 1
print(f"The N power N series up to {count} is {counter}", end="")
while (result <= count):
    counter = counter + 1
    result = result * counter
    power = power + 1
    print(", ", result, end="")
print(".")
