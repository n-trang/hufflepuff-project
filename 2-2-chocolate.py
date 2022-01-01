def chocolate(small, big, total):
    """
        >>> chocolate(1, 1, 6)
        1
        >>> chocolate(1, 1, 7)
        -1
        >>> chocolate(1, 1, 5)
        0
        >>> chocolate(5, 1, 4)
        4
        >>> chocolate(5, 1, 5)
        0
    """
# In JUnit, there's a way to automated those test case by making a template and only parse in the numbers needed. But I don't know how to do it with Python yet :(, so all the boundary test need to be added by hands.

# There are 4 partitions:
# 1. total amount is greater than the bars have. return -1
# 2. need only big bar.
# 3. need only small bar.
# 4. need big bar and small bar.


    big_bar = total // 5
    if big_bar < big:
        amount_left_after_big_bar = total - big_bar * 5
        if small < amount_left_after_big_bar:
            return -1
        else:
            small_bar = amount_left_after_big_bar
            return small_bar
    else:
        amount_left_after_big_bar = total - big * 5
        if small < amount_left_after_big_bar:
            return -1
        else:
            small_bar = amount_left_after_big_bar
            return small_bar

if __name__ == '__main__':
    import doctest
    doctest.testmod()