import base

global pi
pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
global e
e = 2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274

# add support for degrees and hyperbolic inverse funcs
# rewrite if statements as match case


def sin(x):
    if x >= 0 and x <= 2 * pi:
        if x == 0:
            return 0
        elif x == pi:
            return 0
        elif x == 2 * pi:
            return 0
        elif x == (3 * pi) / 2:
            return 0
        elif x == pi / 2:
            return 1
        else:
            ans = -(
                (x - pi)
                - (1 / base.factorial(3)) * (x - pi) ** 3
                + (1 / base.factorial(5)) * (x - pi) ** 5
                - (1 / base.factorial(7)) * (x - pi) ** 7
                + (1 / base.factorial(9)) * (x - pi) ** 9
                - (1 / base.factorial(11)) * (x - pi) ** 11
                + (1 / base.factorial(13)) * (x - pi) ** 13
                - (1 / base.factorial(15)) * (x - pi) ** 15
                + (1 / base.factorial(17)) * (x - pi) ** 17
                - (1 / base.factorial(19)) * (x - pi) ** 19
                + (1 / base.factorial(21)) * (x - pi) ** 21
                - (1 / base.factorial(23)) * (x - pi) ** 23
                + (1 / base.factorial(25)) * (x - pi) ** 25
                - (1 / base.factorial(27)) * (x - pi) ** 27
                + (1 / base.factorial(29)) * (x - pi) ** 29
                - (1 / base.factorial(31)) * (x - pi) ** 31
            )
            return ans
    elif x > 2 * pi:
        i = 0
        while True:
            i += 1
            y = x - (2 * pi * i)
            if y <= 0:
                i -= 1
                y = x - (2 * pi * i)
                break
        if y == 0:
            return 0
        elif y == 2 * pi:
            return 1
        elif y == pi / 2:
            return 0
        elif y == (3 * pi) / 2:
            return 0
        elif y == pi:
            return -1
        else:
            ans2 = -(
                (y - pi)
                - (1 / base.factorial(3)) * (y - pi) ** 3
                + (1 / base.factorial(5)) * (y - pi) ** 5
                - (1 / base.factorial(7)) * (y - pi) ** 7
                + (1 / base.factorial(9)) * (y - pi) ** 9
                - (1 / base.factorial(11)) * (y - pi) ** 11
                + (1 / base.factorial(13)) * (y - pi) ** 13
                - (1 / base.factorial(15)) * (y - pi) ** 15
                + (1 / base.factorial(17)) * (y - pi) ** 17
                - (1 / base.factorial(19)) * (y - pi) ** 19
                + (1 / base.factorial(21)) * (y - pi) ** 21
                - (1 / base.factorial(23)) * (y - pi) ** 23
                + (1 / base.factorial(25)) * (y - pi) ** 25
                - (1 / base.factorial(27)) * (y - pi) ** 27
                + (1 / base.factorial(29)) * (y - pi) ** 29
                - (1 / base.factorial(31)) * (y - pi) ** 31
            )
            return ans2
    else:
        i = 0
        while True:
            i += 1
            z = x + (2 * pi * i)
            if z >= 2 * pi:
                i -= 1
                z = x + (2 * pi * i)
                break
        if z == 0:
            return 0
        elif z == 2 * pi:
            return 1
        elif z == pi / 2:
            return 0
        elif z == (3 * pi) / 2:
            return 0
        elif z == pi:
            return -1
        else:
            ans3 = -(
                (z - pi)
                - (1 / base.factorial(3)) * (z - pi) ** 3
                + (1 / base.factorial(5)) * (z - pi) ** 5
                - (1 / base.factorial(7)) * (z - pi) ** 7
                + (1 / base.factorial(9)) * (z - pi) ** 9
                - (1 / base.factorial(11)) * (z - pi) ** 11
                + (1 / base.factorial(13)) * (z - pi) ** 13
                - (1 / base.factorial(15)) * (z - pi) ** 15
                + (1 / base.factorial(17)) * (z - pi) ** 17
                - (1 / base.factorial(19)) * (z - pi) ** 19
                + (1 / base.factorial(21)) * (z - pi) ** 21
                - (1 / base.factorial(23)) * (z - pi) ** 23
                + (1 / base.factorial(25)) * (z - pi) ** 25
                - (1 / base.factorial(27)) * (z - pi) ** 27
                + (1 / base.factorial(29)) * (z - pi) ** 29
                - (1 / base.factorial(31)) * (z - pi) ** 31
            )
            return ans3


def cos(x):
    if x >= 0 and x <= 2 * pi:
        if x == 0:
            return 0
        elif x == 2 * pi:
            return 1
        elif x == pi / 2:
            return 0
        elif x == (3 * pi) / 2:
            return 0
        elif x == pi:
            return -1
        else:
            ans = -(
                1
                - (x - pi) ** 2 / base.factorial(2)
                + (x - pi) ** 4 / base.factorial(4)
                - (x - pi) ** 6 / base.factorial(6)
                + (x - pi) ** 8 / base.factorial(8)
                - (x - pi) ** 10 / base.factorial(10)
                + (x - pi) ** 12 / base.factorial(12)
                - (x - pi) ** 14 / base.factorial(14)
                + (x - pi) ** 16 / base.factorial(16)
                - (x - pi) ** 18 / base.factorial(18)
                + (x - pi) ** 20 / base.factorial(20)
                - (x - pi) ** 22 / base.factorial(22)
                + (x - pi) ** 24 / base.factorial(24)
                - (x - pi) ** 26 / base.factorial(26)
                + (x - pi) ** 28 / base.factorial(28)
                - (x - pi) ** 30 / base.factorial(30)
                + (x - pi) ** 32 / base.factorial(32)
            )
            return ans
    elif x > 2 * pi:
        i = 0
        while True:
            i += 1
            y = x - (2 * pi * i)
            if y <= 0:
                i -= 1
                y = x - (2 * pi * i)
                break
        if y == 0:
            return 0
        elif y == 2 * pi:
            return 1
        elif y == pi / 2:
            return 0
        elif y == (3 * pi) / 2:
            return 0
        elif y == pi:
            return -1
        else:
            ans2 = -(
                1
                - (y - pi) ** 2 / base.factorial(2)
                + (y - pi) ** 4 / base.factorial(4)
                - (y - pi) ** 6 / base.factorial(6)
                + (y - pi) ** 8 / base.factorial(8)
                - (y - pi) ** 10 / base.factorial(10)
                + (y - pi) ** 12 / base.factorial(12)
                - (y - pi) ** 14 / base.factorial(14)
                + (y - pi) ** 16 / base.factorial(16)
                - (y - pi) ** 18 / base.factorial(18)
                + (y - pi) ** 20 / base.factorial(20)
                - (y - pi) ** 22 / base.factorial(22)
                + (y - pi) ** 24 / base.factorial(24)
                - (y - pi) ** 26 / base.factorial(26)
                + (y - pi) ** 28 / base.factorial(28)
                - (y - pi) ** 30 / base.factorial(30)
                + (y - pi) ** 32 / base.factorial(32)
            )
            return ans2
    else:
        i = 0
        while True:
            i += 1
            z = x + (2 * pi * i)
            if z >= 2 * pi:
                i -= 1
                z = x + (2 * pi * i)
                break
        if z == 0:
            return 0
        elif z == 2 * pi:
            return 1
        elif z == pi / 2:
            return 0
        elif z == (3 * pi) / 2:
            return 0
        elif z == pi:
            return -1
        else:
            ans3 = -(
                1
                - (z - pi) ** 2 / base.factorial(2)
                + (z - pi) ** 4 / base.factorial(4)
                - (z - pi) ** 6 / base.factorial(6)
                + (z - pi) ** 8 / base.factorial(8)
                - (z - pi) ** 10 / base.factorial(10)
                + (z - pi) ** 12 / base.factorial(12)
                - (z - pi) ** 14 / base.factorial(14)
                + (z - pi) ** 16 / base.factorial(16)
                - (z - pi) ** 18 / base.factorial(18)
                + (z - pi) ** 20 / base.factorial(20)
                - (z - pi) ** 22 / base.factorial(22)
                + (z - pi) ** 24 / base.factorial(24)
                - (z - pi) ** 26 / base.factorial(26)
                + (z - pi) ** 28 / base.factorial(28)
                - (z - pi) ** 30 / base.factorial(30)
                + (z - pi) ** 32 / base.factorial(32)
            )
            return ans3


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
    if base.absolute_valueabsolute_value(x) < 1:
        ans = (
            x
            + (1 / 2) * (x**3 / 3)
            + (base.factorial_odd_only(3) / base.factorial_even_only(4)) * (x**5 / 5)
            + (base.factorial_odd_only(5) / base.factorial_even_only(6)) * (x**7 / 7)
            + (base.factorial_odd_only(7) / base.factorial_even_only(8)) * (x**9 / 9)
            + (base.factorial_odd_only(9) / base.factorial_even_only(10))
            * (x**11 / 11)
            + (base.factorial_odd_only(11) / base.factorial_even_only(12))
            * (x**13 / 13)
            + (base.factorial_odd_only(13) / base.factorial_even_only(14))
            * (x**15 / 15)
            + (base.factorial_odd_only(15) / base.factorial_even_only(16))
            * (x**17 / 17)
            + (base.factorial_odd_only(17) / base.factorial_even_only(18))
            * (x**19 / 19)
            + (base.factorial_odd_only(19) / base.factorial_even_only(20))
            * (x**21 / 21)
            + (base.factorial_odd_only(21) / base.factorial_even_only(22))
            * (x**23 / 23)
            + (base.factorial_odd_only(23) / base.factorial_even_only(24))
            * (x**25 / 25)
            + (base.factorial_odd_only(25) / base.factorial_even_only(26))
            * (x**27 / 27)
            + (base.factorial_odd_only(27) / base.factorial_even_only(28))
            * (x**29 / 29)
            + (base.factorial_odd_only(29) / base.factorial_even_only(30))
            * (x**31 / 31)
        )
        return ans
    return "undefined"


def acos(x):
    if base.absolute_value(x) < 1:
        ans = (pi / 2) - asin(x)
        return ans
    return "undefined"


def atan(x):
    if base.absolute_value(x) < 1:
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
            (pi / 2)
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
            (pi / 2)
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
    if base.absolute_value(x) > 1:
        ans = asin(1 / x)
        return ans
    return "undefined"


def asec(x):
    if base.absolute_value(x) > 1:
        ans = acos(1 / x)
        return ans
    return "undefined"


def acot(x):
    ans = (pi / 2) - atan(x)
    return ans


def asinh(x):
    if base.absolute_value(x) < 1:
        ans = (
            x
            - (1 / 2) * (x**3 / 3)
            + (base.factorial_odd_only(3) / base.factorial_even_only(4)) * (x**5 / 5)
            - (base.factorial_odd_only(5) / base.factorial_even_only(6)) * (x**7 / 7)
            + (base.factorial_odd_only(7) / base.factorial_even_only(8)) * (x**9 / 9)
            - (base.factorial_odd_only(9) / base.factorial_even_only(10))
            * (x**11 / 11)
            + (base.factorial_odd_only(11) / base.factorial_even_only(12))
            * (x**13 / 13)
            - (base.factorial_odd_only(13) / base.factorial_even_only(14))
            * (x**15 / 15)
            + (base.factorial_odd_only(15) / base.factorial_even_only(16))
            * (x**17 / 17)
            - (base.factorial_odd_only(17) / base.factorial_even_only(18))
            * (x**19 / 19)
            + (base.factorial_odd_only(19) / base.factorial_even_only(20))
            * (x**21 / 21)
            - (base.factorial_odd_only(21) / base.factorial_even_only(22))
            * (x**23 / 23)
            + (base.factorial_odd_only(23) / base.factorial_even_only(24))
            * (x**25 / 25)
            - (base.factorial_odd_only(25) / base.factorial_even_only(26))
            * (x**27 / 27)
            + (base.factorial_odd_only(27) / base.factorial_even_only(28))
            * (x**29 / 29)
            - (base.factorial_odd_only(29) / base.factorial_even_only(30))
            * (x**31 / 31)
            + (base.factorial_odd_only(31) / base.factorial_even_only(32))
            * (x**33 / 33)
        )
        return ans
    elif x >= 1:
        ans = (
            base.ln(base.absolute_value(2 * x))
            + 1 / 2**2 * x**2
            - 3 / base.factorial_even_only(4) * 4**x**4
            + base.factorial_odd_only(5) / base.factorial_even_only(6) * 6 * x**6
            + 1 / 2**2 * x**2
            - 3 / base.factorial_even_only(4) * 4**x**4
            + base.factorial_odd_only(5) / base.factorial_even_only(6) * 6 * x**6
            + 1 / 2**2 * x**2
            - 3 / base.factorial_even_only(4) * 4**x**4
            + base.factorial_odd_only(5) / base.factorial_even_only(6) * 6 * x**6
        )
    elif x <= -1:
        pass


def acosh(x):
    pass


def atanh(x):
    if base.absolute_value(x) < 1:
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
    if base.absolute_value(x) > 1:
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
