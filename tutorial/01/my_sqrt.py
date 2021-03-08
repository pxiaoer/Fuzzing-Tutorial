import fuzzingbook.fuzzingbook_utils 

from fuzzingbook.Timer import Timer

import random

EPSILON = 1e-8


def my_sqrt_fixed(x):
    assert 0 <= x 

    if x == 0:
        return 0
    
    return my_sqrt(x)


def my_sqrt(x):
    approx = None
    guess = x / 2

    while approx != guess:
        approx = guess
        guess = (approx + x / approx) / 2

    return approx



def my_sqrt_with_log(x):
    approx = None
    guess = x / 2

    while approx != guess:
        print("approx=", approx)
        approx = guess
        guess = (approx + x / approx) / 2

    return approx


def assertEquals(x, y, epsilon=1e-8):
    assert abs(x - y) < epsilon


def my_sqrt_checked(x):
    root = mysql_sqrt(x)
    assertEquals(root * root, x)
    return root



def main():
    print(my_sqrt(2),my_sqrt(4))
    print(my_sqrt_with_log(9))


    result = my_sqrt(4)
    expected_result = 2.0 
    if result == expected_result:
        print("Test passed")
    else:
        print("Test failed")


    assert my_sqrt(4) == 2
    assert abs(my_sqrt(4)-2) < EPSILON

    assertEquals(my_sqrt(9),3)
    assertEquals(my_sqrt(42.11)* my_sqrt(42.11),42.11)

    with Timer() as timer:
        for n in range(1, 1000):
            assertEquals(my_sqrt(n) * my_sqrt(n), n)

    print(timer.elapsed_time())

    with Timer() as timer:
        for i in range(1, 10000):
            x = 1 + random.random() * 1000000
            assertEquals(my_sqrt(x) * my_sqrt(x), x)

    print(timer.elapsed_time())


if __name__ == "__main__":
    main()