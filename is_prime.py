import math

def is_prime(n, divisor=None):
    if not isinstance(n, int) or n <= 0:
        print(str(n)+" - не є натуральним")
        return None
    elif divisor is None:
        divisor=math.floor(math.isqrt(n))
    if divisor==1:
        print(str(n)+" - просте число")
        return True
    elif n%divisor==0:
        print(str(n)+" - складине число")
        return False
    else:
        return is_prime(n, divisor-1)

