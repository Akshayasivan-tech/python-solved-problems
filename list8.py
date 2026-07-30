numbers=[1,2,3,4,5,6,7,8,9,10]
k = 5
for i in range(k):
    last=numbers.pop()
    numbers.insert(0,last)
    print(numbers)