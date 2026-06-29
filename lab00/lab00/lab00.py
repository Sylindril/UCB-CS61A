def twenty_twenty_four():
    """Come up with the most creative expression that evaluates to 2024
    using only numbers and the +, *, and - operators.

    >>> twenty_twenty_four()
    2024
    """
    return 2*7 + 3*(7*6*5*4*3*2*1 - 5*(6*5*4*3*2*1 + 5*4*3*2*1 + 4*3*2*1 + 3*2*1 + 2*1 + 1 + 1))

print(twenty_twenty_four())

