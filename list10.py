numbers=[1,2,3,4,5,6,7,8,9,10]
freq = {}
for i in numbers:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
        print(freq)