global pi
pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
global e
e = 2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274
global i
i = 0

def find_coterminal(ang, mode, direc):
    match mode:
        case "DEG":
            match direc:
                case "+":
                    pass
                case "-":
                    pass
        case "RAD":
            match direc:
                case "+":
                    pass
                case "-":
                    pass
    



def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact


def sqrt(num):
    num ** (1 / 2)
    return num


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
        else:
            return True


def is_odd(num):
    if num % 2 == 0:
        return False
    return True


def is_even(num):
    if num % 2 == 0:
        return True
    return False


def factorial_odd_only(num):
    fact = 1
    if is_odd(num) == False:
        return
    for i in range(1, num):
        if is_odd(i) == True:
            fact = fact * i
    fact = fact * num
    return fact


def factorial_even_only(num):
    fact = 1
    if is_even(num) == False:
        return
    for i in range(1, num):
        if is_even(i) == True:
            fact = fact * i
    fact = fact * num
    return fact


def absolute_value(num):
    if num >= 0:
        return num
    elif num < 0:
        return num * -1
    else:
        return


def ln(x):
    if x > 0:
        n = 10000000
        ans = n * ((x ** (1 / n)) - 1)
        return ans
    return "undefined"
