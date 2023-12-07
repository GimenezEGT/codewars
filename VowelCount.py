def get_count(sentence):
    vowels  = ['a','e','i','o','u']
    counter = 0
    for v in vowels:
        if v in sentence:
            counter += sentence.count(v)
    return counter

print(get_count('abracadrabra'))