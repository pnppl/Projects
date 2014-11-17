# find pi to Nth digit; N must be 20 or less; defaults to N = 5
# technically doesn't 'generate' pi but it produces the desired output elegantly

import math, sys

def piN(n=5):
    if n > 20:
        out = 'error, too large'
    else:
        out = '{0:.{1}f}'.format(math.pi, n)
    print(out)
    
if __name__ == '__main__':
    if len(sys.argv) == 1:
        piN()
    else:
        piN(int(sys.argv[1]))
