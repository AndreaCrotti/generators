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


.. literalinclude:: code/generators.py
    :pyobject: is_even

.. literalinclude:: code/generators.py
    :pyobject: next_even

.. literalinclude:: code/generators.py
    :pyobject: classic_even_gen

*Any problem with that??*


Composability
=============

How do I get the first 10 even numbers?

.. literalinclude:: code/generators.py
    :pyobject: classic_ten_first_even


*No code reuse!*

What if I could do this?

.. literalinclude:: code/generators.py
    :pyobject: ten_first_even

Generators
==========

Infinite list of even numbers:

.. code:: haskell

   even = [x | x <- [0..], x `mod` 2 == 0]



Teaser example
==============
 
Sieve of Erathostenes

.. code-block:: haskell

    primesTo m = eratos [2..m]  where
       eratos []     = []
       eratos (p:xs) = p : eratos (xs `minus` [p, p+p..m])


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

- *Generator*: A function which returns an iterator.
- *Iterator*: An object representing a stream of data.
- *Iterable*: An object capable of returning its members one at a time.

Possible drawbacks
==================

.. TODO: add an example where debugging with a generator is a lot harder

.. literalinclude:: code/generators.py
    :pyobject: overflow_list

.. TODO: show in real time that this fails

.. literalinclude:: code/generators.py
    :pyobject: overflow_gen

Resources
=========

.. _generator_expression: http://www.python.org/dev/peps/pep-0289/
.. _yield_from: http://www.python.org/dev/peps/pep-0380/
.. _python_glossary: http://docs.python.org/2/glossary.html
