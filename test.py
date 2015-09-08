from deco import log,log2file

@log
def sum_n(n):
    return n*(n+1)/2

@log
def sum_n2(n):
    return n*(n+1)*(2*n+1)/6

@log
def isPrime(n):
    import math
    if n > 1:
        for i in range(2, int(math.sqrt(n))):
            if (n % i) == 0:
                return False
    return True

sum_n(10)
sum_n2(10)
isPrime(30)

