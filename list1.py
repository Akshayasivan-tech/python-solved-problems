numbers=[1, 2, 3, 4, 5]
largest = numbers[0]
for i in numbers:
    if i > largest:
        largest = i
        print("The largest number is:", largest)    