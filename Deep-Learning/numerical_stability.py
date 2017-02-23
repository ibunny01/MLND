# If the numerical value of the calculation is too large or too small, it is
# preferable to calculate the value as small as possible because the calculation
# of the computer causes an error.

# result = 1000000000
result = 1

for i in range(1,1000000):
    result += 0.000001

# result -= 1000000000
result -= 1


print(result)
