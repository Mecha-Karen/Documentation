.. meta::
    :title: Documentation - Mecha Karen
    :type: website
    :url: https://docs.mechakaren.xyz/api
    :description: API Reference [Math Endpoint]
    :theme-color: #f54646

********
Patterns
********
All patterns and flags accepted in the math endpoint equation parser.

Parser
======
Our parser selects elements using regex and splitting method. For example ``1 + 1`` is translated to

.. code-block:: python

    # Example block of code how our parser reads your equation

    def solve(unsolved: str) -> typing.Union[str, int]
        block_split = reader.split(unsolved)
        # value: `[1, '+', 1]`
        as_obj = parsing.map_to_obj(block_split)
        # value: `[Integer(1), Operator('+'), Integer(1)]`

        return parsing.solve(as_obj, err=True)

    unsolved = '1 + 1'
    print(solve(unsolved))
    # printed value: 2

Its best to keep a space between each element to prevent any errors whilst parsing.

Language Parsing
----------------
As of now we only allow to usage of certain keywords in the ``ENGLISH`` language. These keywords are listed below and must always be seperated by a space!


Operators
=========
* "+" - Addition
* "-" - Subtraction
* "*" - Multiplication
* "**" - To the power of
* "/" - Division
* "//" - Division without remainder

Unary Operators
===============
* "squared" - Times a number by its self, ``x * x``
* "cubed" - Times a number by itself 3 times, ``x * x * x``

These are just shortcut methods you can also do ``x ** 2`` for squaring, and so on.

Constants
=========
Premade mathematical values which you can use.

* Pi - The value for pi, we use ``3.141693``
* E - The value for Euler's number, we use ``2.718281``

Functions
=========
Mathmatical functions which are widely used and provide a simple way of working out problems.

* sqrt - Square root
* log - Logarithm

Using Functions and Constants
=============================
Using functions and constants is a method which doesnt require any long curly brackets, back slashes etc.

Constants
---------
Simply just include the name of the constant in **lowercases**. For example ``Pi`` would be ``pi``.
This is not compulsory it just makes the likelihood of errors much lower!

Example
^^^^^^^
.. code-block:: text

    pi * (4 squared)

Functions
---------
To use functions, you provide the name of the function and either, wrap the number in brackets or provide the number next to the function - with a space.

Example
^^^^^^^

.. code-block:: text

    sqrt 4
    sqrt(4)

Never, ever do:

.. code-block:: text

    sqrt4

Scales
======
Instead of writing large numbers that have millions of zeros you can use inbuilt scales which are listed below:

.. code-block:: text

    hundred -> 1 * (10 ^ 2)
    thousand -> 1 * (10 ^ 3)
    million -> 1 * (10 ^ 6)
    billion -> 1 * (10 ^ 9)
    trillion -> 1 * (10 ^ 12)
