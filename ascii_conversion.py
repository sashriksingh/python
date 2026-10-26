sentence = input("Enter a Sentence : ")
for character in sentence:
    number = ord(character)
    if(number>90):
        number = number - 26
        character = chr(number)
    if(number < 90):
        number = number + 3
        character = chr(number)
    print(character)