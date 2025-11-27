number = int(input("Which multiplication table you want to print? "))
count = 10
counter = 0
print(f"The multiplication table of {number} is:")
while (counter < count):
    counter = counter + 1
    print(f"{number:2d} x {counter:2d} = {number * counter:3d}")
