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


# Local Variables:
# compile-command: "cd .. && make"
# End:
