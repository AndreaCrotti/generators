import itertools
import unittest
# TODO: try to use python future to see how the iteration works


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


def is_even(num):
    return num % 2 == 0


def next_even(num):
    return num if is_even(num) else (num + 1)


def gen_even_filter():
    return filter(is_even, itertools.count(0))


class GenIterator:
    def __init__(self, start=0):
        self.even = next_even(start)

    def __iter__(self):
        return self

    def __next__(self):
        tmp = self.even
        self.even += 2
        return tmp


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


def homemade_context_manager(gen):
    """Given a generator function do a try finally
    """
    next(gen)




# Local Variables:
# compile-command: "cd .. && make"
# End:
