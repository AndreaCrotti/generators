.. generators documentation master file, created by
   sphinx-quickstart2 on Sun Jan  5 15:25:23 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to generators's documentation!
======================================

Twitter: @andreacrotti

Slides: https://github.com/AndreaCrotti/generator

Working for http://www.wazoku.com/:

.. image:: img/wazoku.png
   :height: 70


Why you should care
===================

Teaser example
==============
 
Sieve of erathostenes

.. code-block:: haskell

    primesTo m = eratos [2..m]  where
       eratos []     = []
       eratos (p:xs) = p : eratos (xs `minus` [p, p+p..m])


Infinite list of even numbers:

.. code:: haskell

   even = [x | x <- [0..], x `mod` 2 == 0]

Using ifilter

.. code:: python
    
    is_even = lambda n: n % 2 == 0
    even_gen = itertools.ifilter(is_even, itertools.count(0))
    # print the first 10 elements
    for even in itertools.islice(even_gen, 0, 10):
        print(even)

With a custom generator:

.. literalinclude:: code/generators.py
    :pyobject: gen_even


With an iterator:

.. literalinclude:: code/generators.py
   :pyobject: GenIterator

.. TODO: add some information about yield from

Theory
======

Iterators, iterable, generators
===============================

Possible drawbacks
==================

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

