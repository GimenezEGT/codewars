def duplicate_encode(word):
    c = 0
    word = word.lower()
    word_list = list(word)
    new_word = ''
    for i, letter in enumerate(word_list):
        # print(letter, ": ", word.count(letter))
        c = word.count(letter)
        #print(letter)
        if c == 1:
            word_list[i] = word_list[i].replace(letter, "(")
        if c > 1:
            word_list[i] = word_list[i].replace(letter, ")")
    new_word = ''.join(word_list)
    print(new_word)
    return new_word


test = duplicate_encode("pjJdYEQf)@l!alhyv!CQG!qMbQco!LeCUlodqp(")
