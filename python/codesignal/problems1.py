def convert_to_base_16(n:str, x:int) -> str:
    ''' 
    accepts string representing a number with base x
    convert n from base x to base 16 
    '''
    # step 1 create a dictionary that holds numerical values of the string
    # n:str
    letters = 'abcdefghijklmnopqrstuvwxyz'
    if n == '0':
        return '0'
    elif x == 16:
        return n
    else:
        v1 = dict()
        for i in range(10):
            v1[str(i)]= i
        v2 = {n: value+10 for value, n in enumerate(letters)}
        num_values = {**v1, **v2}

        # step 2: convert from base x to base 10
        # to convert 234(base 5) to number with base 10:
        # 2*(5^2) + 3*(5^1) + 4*(5^0) = 2*25 + 3*5 + 4 = 69
        power = len(n) - 1
        number = 0
        for i in (range(power + 1)):
            number += num_values[n[i]]*(x**power)
            power -= 1

        # step 3: convert from base 10 to base x
        # 69 base 10 to base 16
        # 69 // 5 = 13, 69 % 5 = 4, bit# = 0 (last position)
        # 13 // 5 = 2, 13 % 5 = 3, bit# = 1
        # 2 // 5 = 0, 2 % 5 = 2, bit# = 2
        list_of_remainders = []
        str_values = {v: k for k, v in num_values.items()}
        while number != 0:
            remainder = number % 16
            number = number // 16
            list_of_remainders.append(str_values[remainder])
        list_of_remainders.reverse()
        return ''.join(list_of_remainders)
  

# 1 line solution
import numpy
def convert_to_base_16(n:str, x:int) -> str:
    return '0' if n == '0' else numpy.base_repr(int(n, x), 16).lower()

''' other solutions '''
# return format(int(n, x), 'x')
# return hex(int(n, x))[2:]
# return "%x" % int(n, x)
# return "{0:x}".format(int(n,x))

''' 
"{0:b}".format(100) # bin: 1100100
"{0:x}".format(100) # hex: 64
"{0:o}".format(100) # oct: 144
''' 

def mex(s: list, upperBound: int) -> int:
    '''
    minimum excludant: for the given set `s` 
    it finds the minimum non-negative integer that is not present in `s`.
    function finds mex if it is smallest than upperBound or returns upperBound instead
    '''
    found = -1
    for i in range(upperBound):
        if not i in s:
            found = i
            break
    else:
        found = upperBound

    return found