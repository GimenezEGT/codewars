def duplicate_count(text):
    string = text.lower()
    uniqueLetters = ''.join(set(string))
    counter2 = 0
    for letter in uniqueLetters:
        counter =  string.count(letter)
        if counter > 1:
            counter2 += 1
    return counter2


print(duplicate_count("abcdeaB"))