global pi
pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
global e
e = 2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274

# add support for degrees, inverse funcs, and hyperbolic inverse funcs
# rewrite if statements as match case


def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact


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
                - (1 / factorial(3)) * (x - pi) ** 3
                + (1 / factorial(5)) * (x - pi) ** 5
                - (1 / factorial(7)) * (x - pi) ** 7
                + (1 / factorial(9)) * (x - pi) ** 9
                - (1 / factorial(11)) * (x - pi) ** 11
                + (1 / factorial(13)) * (x - pi) ** 13
                - (1 / factorial(15)) * (x - pi) ** 15
                + (1 / factorial(17)) * (x - pi) ** 17
                - (1 / factorial(19)) * (x - pi) ** 19
                + (1 / factorial(21)) * (x - pi) ** 21
                - (1 / factorial(23)) * (x - pi) ** 23
                + (1 / factorial(25)) * (x - pi) ** 25
                - (1 / factorial(27)) * (x - pi) ** 27
                + (1 / factorial(29)) * (x - pi) ** 29
                - (1 / factorial(31)) * (x - pi) ** 31
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
                - (1 / factorial(3)) * (y - pi) ** 3
                + (1 / factorial(5)) * (y - pi) ** 5
                - (1 / factorial(7)) * (y - pi) ** 7
                + (1 / factorial(9)) * (y - pi) ** 9
                - (1 / factorial(11)) * (y - pi) ** 11
                + (1 / factorial(13)) * (y - pi) ** 13
                - (1 / factorial(15)) * (y - pi) ** 15
                + (1 / factorial(17)) * (y - pi) ** 17
                - (1 / factorial(19)) * (y - pi) ** 19
                + (1 / factorial(21)) * (y - pi) ** 21
                - (1 / factorial(23)) * (y - pi) ** 23
                + (1 / factorial(25)) * (y - pi) ** 25
                - (1 / factorial(27)) * (y - pi) ** 27
                + (1 / factorial(29)) * (y - pi) ** 29
                - (1 / factorial(31)) * (y - pi) ** 31
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
                - (1 / factorial(3)) * (z - pi) ** 3
                + (1 / factorial(5)) * (z - pi) ** 5
                - (1 / factorial(7)) * (z - pi) ** 7
                + (1 / factorial(9)) * (z - pi) ** 9
                - (1 / factorial(11)) * (z - pi) ** 11
                + (1 / factorial(13)) * (z - pi) ** 13
                - (1 / factorial(15)) * (z - pi) ** 15
                + (1 / factorial(17)) * (z - pi) ** 17
                - (1 / factorial(19)) * (z - pi) ** 19
                + (1 / factorial(21)) * (z - pi) ** 21
                - (1 / factorial(23)) * (z - pi) ** 23
                + (1 / factorial(25)) * (z - pi) ** 25
                - (1 / factorial(27)) * (z - pi) ** 27
                + (1 / factorial(29)) * (z - pi) ** 29
                - (1 / factorial(31)) * (z - pi) ** 31
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
                - (x - pi) ** 2 / factorial(2)
                + (x - pi) ** 4 / factorial(4)
                - (x - pi) ** 6 / factorial(6)
                + (x - pi) ** 8 / factorial(8)
                - (x - pi) ** 10 / factorial(10)
                + (x - pi) ** 12 / factorial(12)
                - (x - pi) ** 14 / factorial(14)
                + (x - pi) ** 16 / factorial(16)
                - (x - pi) ** 18 / factorial(18)
                + (x - pi) ** 20 / factorial(20)
                - (x - pi) ** 22 / factorial(22)
                + (x - pi) ** 24 / factorial(24)
                - (x - pi) ** 26 / factorial(26)
                + (x - pi) ** 28 / factorial(28)
                - (x - pi) ** 30 / factorial(30)
                + (x - pi) ** 32 / factorial(32)
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
                - (y - pi) ** 2 / factorial(2)
                + (y - pi) ** 4 / factorial(4)
                - (y - pi) ** 6 / factorial(6)
                + (y - pi) ** 8 / factorial(8)
                - (y - pi) ** 10 / factorial(10)
                + (y - pi) ** 12 / factorial(12)
                - (y - pi) ** 14 / factorial(14)
                + (y - pi) ** 16 / factorial(16)
                - (y - pi) ** 18 / factorial(18)
                + (y - pi) ** 20 / factorial(20)
                - (y - pi) ** 22 / factorial(22)
                + (y - pi) ** 24 / factorial(24)
                - (y - pi) ** 26 / factorial(26)
                + (y - pi) ** 28 / factorial(28)
                - (y - pi) ** 30 / factorial(30)
                + (y - pi) ** 32 / factorial(32)
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
                - (z - pi) ** 2 / factorial(2)
                + (z - pi) ** 4 / factorial(4)
                - (z - pi) ** 6 / factorial(6)
                + (z - pi) ** 8 / factorial(8)
                - (z - pi) ** 10 / factorial(10)
                + (z - pi) ** 12 / factorial(12)
                - (z - pi) ** 14 / factorial(14)
                + (z - pi) ** 16 / factorial(16)
                - (z - pi) ** 18 / factorial(18)
                + (z - pi) ** 20 / factorial(20)
                - (z - pi) ** 22 / factorial(22)
                + (z - pi) ** 24 / factorial(24)
                - (z - pi) ** 26 / factorial(26)
                + (z - pi) ** 28 / factorial(28)
                - (z - pi) ** 30 / factorial(30)
                + (z - pi) ** 32 / factorial(32)
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
    pass


def acos(x):
    pass


def atan(x):
    pass


def acsc(x):
    pass


def asec(x):
    pass


def acot(x):
    pass


def asinh(x):
    pass


def acosh(x):
    pass


def atanh(x):
    pass


def acsch(x):
    pass


def asech(x):
    pass


def acoth(x):
    pass


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
