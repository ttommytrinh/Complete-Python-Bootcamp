#GRABBED THE CODE FOR CALCULATING PI TO 1000 DIGITS ONLINE, MADE PI_DIGITS FUNCTION ON OWN
import decimal

def pi():
    decimal.getcontext().prec += 2
    three = decimal.Decimal(3)
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n + na, na + 8
        d, da = d + da, da + 32
        t = (t * n) / d
        s += t
    decimal.getcontext().prec -= 2
    return +s

decimal.getcontext().prec = 1000
pi = pi()

pi_str = str(pi)
pi_list = [x for x in pi_str]

def pi_digits(number):

    new_pi_list = pi_list[:number+1]
    new_pi = "".join(new_pi_list)
    return(new_pi)
