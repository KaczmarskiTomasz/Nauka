def sumEvenNumsFromList(lists):
    return sum([
            num
            for num in lists
            if num > 0
              ])
     
numbers = [1, -2, 3, 0, -4, 5]

print(sumEvenNumsFromList(numbers))
