import itertools
import unittest

from . import generators as gener


def test_classic_ten_first_even():
    assert gener.classic_ten_first_even() == list(range(0, 20, 2))


def test_ten_first_even():
    assert gener.ten_first_even() == list(range(0, 20, 2))


def test_classing_even_gen():
    assert gener.classic_even_gen(0, 2) == [0, 2]


class TestOverflow(unittest.TestCase):
    def test_overflow_list(self):
        with self.assertRaises(Exception):
            gener.overflow_list()

    def test_overflow_gen(self):
        gen = gener.overflow_gen()
        self.assertEqual(next(gen), 0)
        self.assertEqual(next(gen), 1)


def test_gen_ifilter():
    gen = gener.gen_even_filter()
    assert gener.construct_result(gen) == [0, 2]


def test_gen_iterator():
    iterator = gener.GenIterator(1)
    assert gener.construct_result(iterator) == [2, 4]


def test_gen_even():
    gen = gener.gen_even(0)
    assert gener.construct_result(gen) == [0, 2]


def test_yield_from():
    gen = gener.gen_even_yield_from(0)
    assert gener.construct_result(gen) == [0, 2]


def test_grep():
    res = gener.Result()
    grepper = gener.grep_with_result('line', res)
    next(grepper)
    grepper.send('very long line')
    assert res.found is True
    grepper.send('not there')
    assert res.found is False


def test_is_prime():
    assert gener.is_prime(2)
    assert gener.is_prime(3)
    assert not gener.is_prime(4)
    assert not gener.is_prime(49)


def test_sieve():
    gen = gener.sieve_gen()
    assert list(itertools.islice(gen, 0, 3)) == [2, 3, 5]


def test_exclude_multiples():
    lis = [3, 4, 5, 6]
    assert list(gener.exclude_multiples(2, lis)) == [3, 5]


# Local Variables:
# compile-command: "cd .. && make"
# End:
