# Seil Tekinaeva
# 03/17/2026
# Problem 3: Using a while loop, ask the user to enter numbers,
# append them to a list, and stop when the sum is greater than 100

numbers = []
total = 0
while total <=100:
     num = int(input("Enter a number: "))
     numbers.append(num)
     total += num

print("List of numbers:", numbers)
print("Sum:", total)
