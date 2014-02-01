import itertools
import unittest
from math import sqrt, ceil
# TODO: try to use python future to see how the iteration works


def count_up_to(start=0, end=3):
    num = start
    while num <= end:
        yield num
        num += 1


def classic_even_gen(start=0, end=100):
    assert start <= end, "Invalid range"
    return [num for num in range(start, end + 1) if is_even(num)]


def classic_ten_first_even():
    even = 0
    res = []
    while len(res) < 10:
        res.append(even)
        even += 2

    return res


def ten_first_even():
    return list(itertools.islice(gen_even(), 10))


def ten_first_even_yield():
    gen = gen_even()
    count = 0
    while count < 10:
        yield next(gen)
        count += 1


def is_even(num):
    return num % 2 == 0


def next_even(num):
    return num if is_even(num) else (num + 1)


def gen_even_filter():
    return filter(is_even, itertools.count(0))


class SimpleIterable:
    def __iter__(self):
        return iter([42])


class GenIterator:
    def __init__(self, start=0):
        self.even = next_even(start)

    def __iter__(self):
        return self

    def __next__(self):
        tmp = self.even
        self.even += 2
        return tmp


class GenIteratorGetItem:
    def __init__(self):
        self.idx = 0

    def __getitem__(self, item):
        if self.idx == 10:
            raise IndexError

        idx = self.idx
        self.idx += 1
        return idx


def gen_even(start=0):
    even = next_even(start)
    while True:
        yield even
        even += 2


def gen_even_yield_from(start=0):
    yield from gen_even(start)


def simple_coroutines():
    pass


def construct_result(gen):
    res = []
    for i in range(2):
        res.append(next(gen))

    return res


def overflow_list():
    """Creates a list in memory with 100 elements
    """
    res = []
    for n in range(101):
        if n == 100:
            raise Exception("Overflow Overflow!")
        res.append(n)

    return res


def overflow_gen():
    """Generator that would fail at the 100th element
    """
    n = 0
    while n < 101:
        if n == 100:
            raise Exception("Overflow Overflow!")
        yield n
        n += 1

# coroutine examples


def grep(pattern):
    print("Looking for pattern {}".format(pattern))
    while True:
        line = (yield)
        if pattern in line:
            print("Found pattern {}".format(line))
        else:
            print("Pattern {} not found".format(line))


class Result:
    def __init__(self):
        self.found = False


def grep_with_result(pattern, result):
    print("Looking for pattern {}".format(pattern))
    while True:
        line = (yield)
        if pattern in line:
            print("Found pattern {}".format(line))
            result.found = True
        else:
            print("Pattern {} not found".format(line))
            result.found = False


def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr

    return start


def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    else:
        max_div = ceil(sqrt(number)) + 1
        for div in range(2, max_div):
            if number % div == 0:
                return False

        return True


def gen_primes_count():
    return filter(is_prime, itertools.count(2))


def gen_primes():
    num = 2
    while True:
        if is_prime(num):
            yield num
            num += 1


def sieve_gen():
    return sieve(itertools.count(2))


def sieve(ints):
    while True:
        prime = next(ints)
        yield prime
        ints = exclude_multiples(prime, ints)


def exclude_multiples(n, ints):
    for i in ints:
        if (i % n) != 0:
            yield i

# Local Variables:
# compile-command: "cd .. && make"
# End:
