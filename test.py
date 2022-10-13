def spin_words(sentence):
    splited_string = sentence.split(' ')
    empty_string = []
    for i in splited_string:
        if len(i) >= 5:
            empty_string.append(i[::-1])
        else:
            empty_string.append(i)
            
    return " ".join(empty_string)

print(spin_words('Hey fellow warriors'))