sentence="apple mango banana apple orange mango apple"
words=sentence.split()
frequency={}
for word in words:
    if word in frequency:
        frequency[word]+=1
    else:
        frequency[word]=1
most=max(frequency,key=frequency.get)
print("Most frequent word:", most)