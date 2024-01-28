# Updated speed_test.py

import timeit
import numpy

def main(iterations=1_000_000_000):
    print(f"Number of iterations: {iterations}")
    print('while loop\t\t', timeit.timeit(lambda: while_loop(iterations), number=1))
    print('for loop\t\t', timeit.timeit(lambda: for_loop(iterations), number=1))
    print('sum_range\t\t', timeit.timeit(lambda: sum_range(iterations), number=1))
    print('sum_numpy\t\t', timeit.timeit(lambda: sum_numpy(iterations), number=1))

def while_loop(n):
    c = 0
    i = 0
    while i < n:
        c += i
        i += 1
    return c

def for_loop(n):
    c = 0
    for i in range(n):
        c += i
    return c

def sum_range(n):
    return sum(range(n))

def sum_numpy(n):
    return numpy.sum(numpy.arange(n))


if __name__ == "__main__":
    main()

