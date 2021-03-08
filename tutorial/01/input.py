from  my_sqrt import my_sqrt,my_sqrt_fixed

import fuzzingbook.fuzzingbook_utils 
from fuzzingbook.ExpectError import ExpectTimeout,ExpectError

def sqrt_program(arg):
    try:
        x = float(arg)
    except ValueError:
        print("Illegal Input")
    else:
        if x < 0:
            print("Illegal number")
        else:
            #print("the root of",x, "is",my_sqrt(x))
            print("the root of",x, "is",my_sqrt_fixed(x))





sqrt_program(4)
sqrt_program("9")
sqrt_program("-1")
sqrt_program("-xxxx")
sqrt_program(0)



#while ExpectTimeout(1):
#    sqrt_program("-1")

#while ExpectError(1):
#    sqrt_program("xxxx")

#while ExpectError(1):
#    sqrt_program(0)

