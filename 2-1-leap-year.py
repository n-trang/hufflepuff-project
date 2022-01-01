def is_leap_year(year):
    """
        >>> is_leap_year(2016)
        True
        >>> is_leap_year(2000)
        True
        >>> is_leap_year(2017)
        False
        >>> is_leap_year(1500)
        False
    """
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 4 == 0 and year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        return False
if __name__ == '__main__':
    import doctest
    doctest.testmod()