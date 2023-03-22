

value = int(input("Enter number to sum"))
result = 0
numToSum = range(1,value + 1)

for num in numToSum:
    result += num

print(result)
    
value1 = int(input("Enter number to sum"))

result1 = sum(range(1,value1 + 1))

print(result1)
