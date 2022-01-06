import string

def count_word(word):
    '''
        >>> count_word("cats")
        1
        >>> count_word("grr")
        1
        >>> count_word("cat")
        0
        >>> count_word("cats!grr")
        2
        >>> count_word("grr!cats")
        2

    '''
    counter = 0
    # check "r" and "s" in the midle of the word.
    word_set = enumerate(word)
    for set in word_set:
        index = set[0]
        char = set[1]
        if char not in string.ascii_letters:
            if word[index-1] == "s" or word[index-1] == "r":
                counter += 1
    # check "r" and "s" at the end of the word.
    if word[-1] == "s":
        counter += 1
    if word[-1] == "r":
        counter += 1

    return counter

if __name__ == '__main__':
    import doctest
    doctest.testmod()



