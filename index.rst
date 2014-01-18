========================================
 How to step to the infinite and beyond
========================================

Twitter: @andreacrotti

Slides: https://github.com/AndreaCrotti/generator

Working for http://www.wazoku.com/:

.. image:: img/wazoku.png
   :height: 70


Even numbers
============

Generate *even* numbers:

.. literalinclude:: code/generators.py
    :pyobject: is_even

.. literalinclude:: code/generators.py
    :pyobject: classic_even_gen

*Any problem with that??*


First n even numbers?
=====================

How do I get the first 10 even numbers?

.. literalinclude:: code/generators.py
    :pyobject: classic_ten_first_even


Which becomes more generally:

.. literalinclude:: code/generators.py
    :pyobject: classic_first_n_even

Composability
=============

.. the generation function contains all the logic

What if I could do this?
*I want to reuse the generation function*

.. literalinclude:: code/generators.py
    :pyobject: ten_first_even_yield

.. literalinclude:: code/generators.py
    :pyobject: ten_first_even

Teaser
======

Infinite list of even numbers:

.. code-block:: haskell

   even = [x | x <- [0..], x `mod` 2 == 0]

Awesome, but in Python?

.. code-block:: python

    (x for x in itertools.count(0) if x % 2 == 0)

Definitions
===========

.. now it's time to give some definitions (in a top down matter)
   before we jump in showing some code.
.. The awesome oneliner I've just shown is a generator expression,
   which is syntactic sugar to yield new generator objects.

.. A generator is a function that returns an iterator, an iterator
.. is an object representing a stream of data, basically something
   that can be looped over with a for loop.

.. And an Iterable at least is any object capable of returning its
   members one at a time.

- *Generator expression*: A generator expression yields a new generator object.
- *Generator*: A function which returns an iterator.
- *Iterator*: An object representing a stream of data.
- *Iterable*: An object capable of returning its members one at a time.

Even numbers
============

With a custom generator:

.. code-block:: python

    (x for x in itertools.count(0) if x % 2 == 0)


.. literalinclude:: code/generators.py
    :pyobject: gen_even


With an iterator:

.. literalinclude:: code/generators.py
   :pyobject: GenIterator

.. TODO: add some information about yield from

Generator vs Iterable
=====================

- Generators are simpler to write
- Generators keep track of the context for you

- Iterables can have more methods defined
- Iterables can have more complex logic

General suggestion: pick a generator unless you need something specific.

Lazyness drawbacks
==================
.. Using generators is the way Python uses to do lazy evaluation.
.. While lazy evaluation is great there can be some cases where it can bite you.
.. This example is artificial but it's also something that can easily happen.

.. TODO: add an example where debugging with a generator is a lot harder

.. literalinclude:: code/generators.py
    :pyobject: overflow_list

.. TODO: show in real time that this fails

.. literalinclude:: code/generators.py
    :pyobject: overflow_gen


Sieve of Erathostenes
=====================
 
Sieve of Erathostenes

.. code-block:: haskell

    primesTo m = eratos [2..m]  where
       eratos []     = []
       eratos (p:xs) = p : eratos (xs `minus` [p, p+p..m])


Generators as lightweight threads
=================================

Example from the monocle_ documentation:

::

    @monocle.o
    def request():
        resp = yield HttpClient.query('http://127.0.0.1:8088/')
        print(resp.code, resp.body)

Resources
=========

.. _generator_expression: http://www.python.org/dev/peps/pep-0289/
.. _yield_from: http://www.python.org/dev/peps/pep-0380/
.. _python_glossary: http://docs.python.org/2/glossary.html
.. only for python2 for now apparently
.. _monocle: https://github.com/saucelabs/monocle
