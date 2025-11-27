count = int(input("Up to which number you want to print the sum of even numbers? "))
counter = 2
sum = 0
while (counter <= count):
    sum = sum + counter
    counter = counter + 2
print(f"The sum of even numbers up to {count} is {sum}.")
