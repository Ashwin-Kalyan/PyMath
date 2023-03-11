import utils
import taylor_series

# add support for degrees and hyperbolic inverse funcs
# rewrite if statements as match case

def sin(x, mode):
    match mode:
        case "RAD":
            if x >= 0 and x <= 2 * utils.pi:
                return taylor_series.for_sin(x)
            elif x > 2 * utils.pi:
                while True:
                    utils.i += 1
                    y = x - (2 * utils.pi * utils.i)
                    if y <= 0:
                        utils.i -= 1
                        y = x - (2 * utils.pi * utils.i)
                        break 
                return taylor_series.for_sin(y)
            while True:
                utils.i += 1
                z = x + (2 * utils.pi * utils.i)
                if z >= 2 * utils.pi:
                    utils.i -= 1
                    z = x + (2 * utils.pi * utils.i)
                    break
            return taylor_series.for_sin(z)
        case "DEG":
            pass
        case _:
            return "Argument 'mode' only accpets 'DEG' and 'RAD'"


def cos(x):
    if x >= 0 and x <= 2 * utils.pi:
       return taylor_series.for_cos(x)
    elif x > 2 * utils.pi:
        while True:
            utils.i += 1
            y = x - (2 * utils.pi * utils.i)
            if y <= 0:
                utils.i -= 1
                y = x - (2 * utils.pi * utils.i)
                break
        return taylor_series.for_cos(x)
    else:
        utils.i = 0
        while True:
            utils.i += 1
            z = x + (2 * utils.pi * utils.i)
            if z >= 2 * utils.pi:
                utils.i -= 1
                z = x + (2 * utils.pi * utils.i)
                break
        return taylor_series.for_cos(x)


def tan(x):
    if cos(x) == 0:
        return "undefined"
    else:
        return sin(x) / cos(x)


def csc(x):
    if sin(x) == 0:
        return "undefined"
    else:
        return 1 / sin(x)


def sec(x):
    if cos(x) == 0:
        return "undefined"
    else:
        return 1 / cos(x)


def cot(x):
    if sin(x) == 0:
        return "undefined"
    else:
        return cos(x) / sin(x)


def asin(x):
    if utils.absolute_valueabsolute_value(x) < 1:
        ans = (
            x
            + (1 / 2) * (x**3 / 3)
            + (utils.factorial_odd_only(3) / utils.factorial_even_only(4)) * (x**5 / 5)
            + (utils.factorial_odd_only(5) / utils.factorial_even_only(6)) * (x**7 / 7)
            + (utils.factorial_odd_only(7) / utils.factorial_even_only(8)) * (x**9 / 9)
            + (utils.factorial_odd_only(9) / utils.factorial_even_only(10))
            * (x**11 / 11)
            + (utils.factorial_odd_only(11) / utils.factorial_even_only(12))
            * (x**13 / 13)
            + (utils.factorial_odd_only(13) / utils.factorial_even_only(14))
            * (x**15 / 15)
            + (utils.factorial_odd_only(15) / utils.factorial_even_only(16))
            * (x**17 / 17)
            + (utils.factorial_odd_only(17) / utils.factorial_even_only(18))
            * (x**19 / 19)
            + (utils.factorial_odd_only(19) / utils.factorial_even_only(20))
            * (x**21 / 21)
            + (utils.factorial_odd_only(21) / utils.factorial_even_only(22))
            * (x**23 / 23)
            + (utils.factorial_odd_only(23) / utils.factorial_even_only(24))
            * (x**25 / 25)
            + (utils.factorial_odd_only(25) / utils.factorial_even_only(26))
            * (x**27 / 27)
            + (utils.factorial_odd_only(27) / utils.factorial_even_only(28))
            * (x**29 / 29)
            + (utils.factorial_odd_only(29) / utils.factorial_even_only(30))
            * (x**31 / 31)
        )
        return ans
    return "undefined"


def acos(x):
    if utils.absolute_value(x) < 1:
        ans = (utils.pi / 2) - asin(x)
        return ans
    return "undefined"


def atan(x):
    if utils.absolute_value(x) < 1:
        ans = (
            x
            - x**3 / 3
            + x**5 / 5
            - x**7 / 7
            + x**9 / 9
            - x**11 / 11
            + x**13 / 13
            - x**15 / 15
            + x**17 / 17
            - x**19 / 19
            + x**21 / 21
            - x**23 / 23
            + x**25 / 25
            - x**27 / 27
            + x**29 / 29
            - x**31 / 31
        )
        return ans
    elif x >= 1:
        ans = (
            (utils.pi / 2)
            - 1 / x
            + 1 / 3 * x**2
            - 1 / 5 * x**2
            + 1 / 7 * x**2
            - 1 / 9 * x**2
            + 1 / 11 * x**2
            - 1 / 13 * x**2
            + 1 / 15 * x**2
            - 1 / 17 * x**2
            + 1 / 19 * x**2
            - 1 / 19 * x**2
            + 1 / 21 * x**2
            - 1 / 23 * x**2
            + 1 / 25 * x**2
            - 1 / 27 * x**2
            + 1 / 29 * x**2
            - 1 / 31 * x**2
        )
        return ans
    elif x <= -1:
        ans = -(
            (utils.pi / 2)
            - 1 / x
            + 1 / 3 * x**2
            - 1 / 5 * x**2
            + 1 / 7 * x**2
            - 1 / 9 * x**2
            + 1 / 11 * x**2
            - 1 / 13 * x**2
            + 1 / 15 * x**2
            - 1 / 17 * x**2
            + 1 / 19 * x**2
            - 1 / 19 * x**2
            + 1 / 21 * x**2
            - 1 / 23 * x**2
            + 1 / 25 * x**2
            - 1 / 27 * x**2
            + 1 / 29 * x**2
            - 1 / 31 * x**2
        )


def acsc(x):
    if utils.absolute_value(x) > 1:
        ans = asin(1 / x)
        return ans
    return "undefined"


def asec(x):
    if utils.absolute_value(x) > 1:
        ans = acos(1 / x)
        return ans
    return "undefined"


def acot(x):
    ans = (utils.pi / 2) - atan(x)
    return ans


def asinh(x):
    if utils.absolute_value(x) < 1:
        ans = (
            x
            - (1 / 2) * (x**3 / 3)
            + (utils.factorial_odd_only(3) / utils.factorial_even_only(4)) * (x**5 / 5)
            - (utils.factorial_odd_only(5) / utils.factorial_even_only(6)) * (x**7 / 7)
            + (utils.factorial_odd_only(7) / utils.factorial_even_only(8)) * (x**9 / 9)
            - (utils.factorial_odd_only(9) / utils.factorial_even_only(10))
            * (x**11 / 11)
            + (utils.factorial_odd_only(11) / utils.factorial_even_only(12))
            * (x**13 / 13)
            - (utils.factorial_odd_only(13) / utils.factorial_even_only(14))
            * (x**15 / 15)
            + (utils.factorial_odd_only(15) / utils.factorial_even_only(16))
            * (x**17 / 17)
            - (utils.factorial_odd_only(17) / utils.factorial_even_only(18))
            * (x**19 / 19)
            + (utils.factorial_odd_only(19) / utils.factorial_even_only(20))
            * (x**21 / 21)
            - (utils.factorial_odd_only(21) / utils.factorial_even_only(22))
            * (x**23 / 23)
            + (utils.factorial_odd_only(23) / utils.factorial_even_only(24))
            * (x**25 / 25)
            - (utils.factorial_odd_only(25) / utils.factorial_even_only(26))
            * (x**27 / 27)
            + (utils.factorial_odd_only(27) / utils.factorial_even_only(28))
            * (x**29 / 29)
            - (utils.factorial_odd_only(29) / utils.factorial_even_only(30))
            * (x**31 / 31)
            + (utils.factorial_odd_only(31) / utils.factorial_even_only(32))
            * (x**33 / 33)
        )
        return ans
    elif x >= 1:
        ans = (
            utils.ln(utils.absolute_value(2 * x))
            + 1 / 2**2 * x**2
            - 3 / utils.factorial_even_only(4) * 4**x**4
            + utils.factorial_odd_only(5) / utils.factorial_even_only(6) * 6 * x**6
            + 1 / 2**2 * x**2
            - 3 / utils.factorial_even_only(4) * 4**x**4
            + utils.factorial_odd_only(5) / utils.factorial_even_only(6) * 6 * x**6
            + 1 / 2**2 * x**2
            - 3 / utils.factorial_even_only(4) * 4**x**4
            + utils.factorial_odd_only(5) / utils.factorial_even_only(6) * 6 * x**6
        )
    elif x <= -1:
        pass


def acosh(x):
    pass


def atanh(x):
    if utils.absolute_value(x) < 1:
        ans = (
            x
            + x**3 / 3
            + x**5 / 5
            + x**7 / 7
            + x**9 / 9
            + x**11 / 11
            + x**13 / 13
            + x**15 / 15
            + x**17 / 17
            + x**19 / 19
            + x**21 / 21
            + x**23 / 23
            + x**25 / 25
            + x**27 / 27
            + x**29 / 29
            + x**31 / 31
        )
        return ans
    return "undefined"


def acsch(x):
    pass


def asech(x):
    pass


def acoth(x):
    if utils.absolute_value(x) > 1:
        ans = (
            1 / x
            + 1 / (3 * x**3)
            + 1 / (5 * x**5)
            + 1 / (7 * x**7)
            + 1 / (9 * x**9)
            + 1 / (11 * x**11)
            + 1 / (13 * x**13)
            + 1 / (15 * x**15)
            + 1 / (17 * x**17)
            + 1 / (19 * x**19)
            + 1 / (21 * x**21)
            + 1 / (23 * x**23)
            + 1 / (25 * x**25)
            + 1 / (27 * x**27)
            + 1 / (29 * x**29)
            + 1 / (31 * x**31)
            + 1 / (33 * x**33)
            + 1 / (35 * x**35)
            + 1 / (37 * x**37)
            + 1 / (39 * x**39)
            + 1 / (41 * x**41)
            + 1 / (43 * x**43)
            + 1 / (45 * x**45)
            + 1 / (47 * x**47)
            + 1 / (49 * x**49)
            + 1 / (51 * x**51)
            + 1 / (53 * x**53)
            + 1 / (55 * x**55)
            + 1 / (57 * x**57)
            + 1 / (59 * x**59)
            + 1 / (61 * x**61)
            + 1 / (63 * x**63)
            + 1 / (65 * x**65)
            + 1 / (67 * x**67)
            + 1 / (69 * x**69)
            + 1 / (71 * x**71)
        )
        return ans
    return "undefined"


def sinh(x):
    ans = (e**x - e**-x) / 2
    return ans


def cosh(x):
    ans = (e**x + e**-x) / 2
    return ans


def tanh(x):
    ans = sinh(x) / cosh(x)
    return ans


def csch(x):
    if x == 0:
        return "undefined"
    ans = 1 / sinh(x)
    return ans


def sech(x):
    ans = 1 / cosh(x)
    return ans


def coth(x):
    if x == 0:
        return "undefined"
    ans = 1 / tanh(x)
    return ans
