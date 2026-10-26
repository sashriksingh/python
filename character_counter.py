text = "Hello"
frequency = {}
for character in text : 
    if character in frequency:
        frequency[character] = frequency[character] + 1
    else:
        frequency[character] = 1
print(frequency)