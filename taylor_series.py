import utils 

def for_sin(arg):
    if arg == 0:
            return 0
    elif arg == utils.pi:
        return 0
    elif arg == 2 * utils.pi:
        return 0
    elif arg == (3 * utils.pi) / 2:
        return 0
    elif arg == utils.pi / 2:
        return 1
    else:
        ans = -(
            (arg - utils.pi)
            - (1 / utils.factorial(3)) * (arg - utils.pi) ** 3
            + (1 / utils.factorial(5)) * (arg - utils.pi) ** 5
            - (1 / utils.factorial(7)) * (arg - utils.pi) ** 7
            + (1 / utils.factorial(9)) * (arg - utils.pi) ** 9
            - (1 / utils.factorial(11)) * (arg - utils.pi) ** 11
            + (1 / utils.factorial(13)) * (arg - utils.pi) ** 13
            - (1 / utils.factorial(15)) * (arg - utils.pi) ** 15
            + (1 / utils.factorial(17)) * (arg - utils.pi) ** 17
            - (1 / utils.factorial(19)) * (arg - utils.pi) ** 19
            + (1 / utils.factorial(21)) * (arg - utils.pi) ** 21
            - (1 / utils.factorial(23)) * (arg - utils.pi) ** 23
            + (1 / utils.factorial(25)) * (arg - utils.pi) ** 25
            - (1 / utils.factorial(27)) * (arg - utils.pi) ** 27
            + (1 / utils.factorial(29)) * (arg - utils.pi) ** 29
            - (1 / utils.factorial(31)) * (arg - utils.pi) ** 31
        )
        return ans

def for_cos(arg):
    if arg == 0:
            return 0
    elif arg == 2 * utils.pi:
        return 1
    elif arg == utils.pi / 2:
        return 0
    elif arg == (3 * utils.pi) / 2:
        return 0
    elif arg == utils.pi:
        return -1
    else:
        ans = -(
            1
            - (arg - utils.pi) ** 2 / utils.factorial(2)
            + (arg - utils.pi) ** 4 / utils.factorial(4)
            - (arg - utils.pi) ** 6 / utils.factorial(6)
            + (arg - utils.pi) ** 8 / utils.factorial(8)
            - (arg - utils.pi) ** 10 / utils.factorial(10)
            + (arg - utils.pi) ** 12 / utils.factorial(12)
            - (arg - utils.pi) ** 14 / utils.factorial(14)
            + (arg - utils.pi) ** 16 / utils.factorial(16)
            - (arg - utils.pi) ** 18 / utils.factorial(18)
            + (arg - utils.pi) ** 20 / utils.factorial(20)
            - (arg - utils.pi) ** 22 / utils.factorial(22)
            + (arg - utils.pi) ** 24 / utils.factorial(24)
            - (arg - utils.pi) ** 26 / utils.factorial(26)
            + (arg - utils.pi) ** 28 / utils.factorial(28)
            - (arg - utils.pi) ** 30 / utils.factorial(30)
            + (arg - utils.pi) ** 32 / utils.factorial(32)
        )
        return ans