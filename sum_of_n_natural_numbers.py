count = int(input("Up to which number you want to compute the sum of natural numbers? "))
counter = 0
sum = 0
print(f"The sum of first {count} natural numbers is ", end="")
while (counter < count):
    sum = sum + (count - counter)
    counter = counter + 1
print(f"{sum}.")
