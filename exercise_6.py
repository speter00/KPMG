def cookie_calculator(money: float, price: int, wrap: int, first_call=True) -> int:
    """
    Calculates the number of cookies you can buy. For each cookie, you also get a wrap.

    :param money: the money you can spend
    :param price: the cost of 1 cookie
    :param wrap: you get an extra cookie from this many wraps
    :param first_call: helper parameter to indicate whether this is the first call of the function
    (so it wasn't called by itself), should be ignored when calling the function
    :return: the number of cookies you can buy
    """
    # base case: you can't buy any cookies
    if money < price:
        return 0

    # Note: wraps can be interpreted as getting extra money, below is the formula
    # This extra money doesn't stack with our actual money however

    bonus_money = (1 / wrap) * price  # each purchase grants this much extra money, effectively
    money_gained = (money // price) * bonus_money  # the bonus "money" you get if you buy as many cookies as you can

    # the recursion: we calculate how many cookies we can buy now, with our current money...
    # then we start calculating again, to see how many cookies we can buy with our "bonus money" (wraps)...
    # by this point, we used up all our actual money, and are only using our bonus money...
    # we repeat this until we can no longer buy any cookies, then sum the result

    # if this was the first call we only call again with the "bonus money" (wraps), we ignore any leftover actual money
    if first_call:
        return int(money // price + cookie_calculator(money_gained, price, wrap, False))
    # otherwise we can use "leftover money"
    # (for example we bought a cookie costing 3 wraps with 4 wraps; we have 1 remaining)
    else:
        return int(money // price + cookie_calculator((money % price) + money_gained, price, wrap, False))
