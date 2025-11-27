number=int(input("Up to which number you want to print the square series? "))
counter = 1
print (f"The square series up to {number} is ")
if (counter+1)*(counter+1)<=number:
    print(f"{counter*counter}, ")
    counter + counter + 1
print(f"{counter * counter}.")
