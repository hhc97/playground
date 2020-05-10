from math import factorial as fact
from math import e
from decimal import Decimal, getcontext
getcontext().prec = 55


def choose(n, r):
    """returns {n}C{r}"""
    return fact(n) // (fact(r) * fact(n - r))


def binom_eq(n, p, num):
    """returns P(n = num)"""
    return (Decimal(choose(n, num))
            * (Decimal(p) ** Decimal(num))
            * ((Decimal(1) - Decimal(p)) ** (Decimal(n) - Decimal(num))))


def binom_less_than(n, p, num):
    """returns P(n <= num)"""
    return sum(binom_eq(n, p, i) for i in range(0, num + 1))


def binom_more_than(n, p, num):
    """returns P(n >= num)"""
    return sum(binom_eq(n, p, i) for i in range(num, n + 1))


def pois_eq(lamb, k):
    """returns P(x = k)"""
    return ((Decimal(lamb) ** Decimal(k))
            * (Decimal(e) ** Decimal(-lamb))) / Decimal(fact(k))


def pois_less_than(lamb, k):
    """returns P(x <= k)"""
    return sum(pois_eq(lamb, i) for i in range(0, k + 1))


def pois_more_than(lamb, k):
    """returns P(x >= k)"""
    return 1 - pois_less_than(lamb, k - 1)


# ===== BINOMIAL =====
n, p, num = 40, 0.38, 30
# ===== POISSON ======
lamb, k = 100, 100

print(f'Binomial distribution ~ Bin({n}, {p})')
print(f'P(x  = {num}): {binom_eq(n, p, num)}')
print(f'P(x <= {num}): {binom_less_than(n, p, num)}')
print(f'P(x >= {num}): {binom_more_than(n, p, num)}')

print(f'\nPoisson distribution ~ Pois({lamb})')
print(f'P(k  = {k}): {pois_eq(lamb, k)}')
print(f'P(k <= {k}): {pois_less_than(lamb, k)}')
print(f'P(k >= {k}): {pois_more_than(lamb, k)}')
