def is_isogram(string):
    new_str = string.lower()  # Making it case-insensitive
    counter = []  # A list with the number of each letter
    for c in new_str:
        counter.append(new_str.count(c))
    # If sum of counter is greater than len(string), some value(s) of counter might be different from 1.
    return True if (sum(counter) == len(string)) else False


print(is_isogram("Dermatoglyphics"))
