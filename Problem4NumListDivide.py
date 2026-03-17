# Seil Tekinaeva
# 03/17/2026
# Problem 4: Create a while loop from 0 to 50
# If the counter is divisible by 10, append it to the list tens

tens = []
counter = 0

while counter <= 50:
    if counter % 10 == 0:
        tens.append(counter)
    counter += 1

print("The numbers divisible by 10 are:", tens)
