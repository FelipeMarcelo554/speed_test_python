import timeit
import numpy

def main():

  print('while loop\t\t', timeit.timeit(while_loop, number=1))
  print('for loop\t\t', timeit.timeit(for_loop, number=1))
  print('sum_range\t\t', timeit.timeit(sum_range, number=1))
  print('sum_numpy\t\t', timeit.timeit(sum_numpy, number=1))


def while_loop(n=1_000_000_000):
    c = 0
    i = 0
    while i < n:
        c += i
        i += 1
    return c

def for_loop(n=1_000_000_000):
    c = 0
    for i in range(n):
        c += i
    return c

def sum_range(n=1_000_000_000):
    return sum(range(n))

def sum_numpy(n=1_000_000_000):
    return numpy.sum(numpy.arange(n))



if __name__ == "__main__":
    main()


