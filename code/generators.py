def next_even(num):
    return num if num % 2 == 0 else (num + 1)


class GenIterator:
    def __init__(self, start=0):
        self.even = next_even(start)

    def __iter__(self):
        return self

    def next(self):
        tmp = self.even
        self.even += 2
        return tmp


def gen_even(start=0):
    even = next_even(start)
    while True:
        yield even
        even += 2


def test_gen_iterator():
    iterator = GenIterator(1)
    res = []
    for i in range(2):
        res.append(next(iterator))

    assert res == [2, 4], res


def test_gen_even():
    res = []
    g = gen_even(0)
    for i in range(2):
        res.append(g.next())

    assert res == [0, 2]

# Local Variables:
# compile-command: "cd .. && make"
# End:
