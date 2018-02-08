# utils.py
# Math library
# Author: Sébastien Combéfis
# Version: February 8, 2018
import math
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

def roots(a, b, c):


    d = b ** 2 - 4 * a * c  # discriminant

    if d < 0:
        return none
    elif d == 0:
        x = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
        return x
    else:
        x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
        x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
        return (x1,x2)
    pass

def integrate(function, lower, upper):
    """Approximates the integral of a fonction between two bounds
    
    Pre: 'function' is a valid Python expression with x as a variable,
         'lower' <= 'upper',
         'function' continuous and integrable between 'lower‘ and 'upper'.
    Post: Returns an approximation of the integral from 'lower' to 'upper'
          of the specified 'function'.
    """
    pass

if __name__ == '__main__':
    print(fact(5))
    print(roots(1, 0, 1))
    print(integrate('x ** 2 - 1', -1, 1))
