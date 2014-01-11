.. generators documentation master file, created by
   sphinx-quickstart2 on Sun Jan  5 15:25:23 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to generators's documentation!
======================================

Contents:

.. toctree::
   :maxdepth: 2

Teaser example
==============
 
Sieve of erathostenes

::

    primesTo m = eratos [2..m]  where
       eratos []     = []
       eratos (p:xs) = p : eratos (xs `minus` [p, p+p..m])

Theory
======

Iterators, iterable, generators
===============================

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

