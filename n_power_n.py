count = int(input("Enter a number to compute the power of itself: "))
termcount = 2
print(f"{count} to the power {count} is 1")
counter = 1
product = 1
while (counter <= termcount):
    product = product * termcount
    counter = counter + 1
while (product <= count):
    print(f", {product})
print(".")
