text="programming"
result=""
seen =set()
for char in text:
    if char not in seen:
        seen.add(char)
        result+=char
print(result)