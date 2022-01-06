def play(left, right):
    """
        >>> play(30, 30)
        0
    """
    if left > 21:
        left = 0
    if right > 21:
        right = 0
    if right > left:
        return(right)
    elif right == left:
        return(0)
    else:
        return(left)

if __name__ == '__main__':
    import doctest
    doctest.testmod()