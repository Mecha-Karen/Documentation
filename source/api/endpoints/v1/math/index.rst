.. meta::
   :title: Documentation - Mecha Karen
   :type: website
   :url: https://docs.mechakaren.xyz/
   :description: API Reference [Math Endpoint]
   :theme-color: #f54646

*************
Math Endpoint
*************
Complete basic mathematical queries, including some worded queries.

Related Pages
-------------
.. toctree::
    :maxdepth: 2

    patterns

Request Method
==============
This endpoint only accepts a ``GET`` request.

URL Patterns
============
The base URL for the chatbot endpoint is ``https://api.mechakaren.xyz/.../math``

` ``...`` represents the API version`.

Instead of adding the ``equation`` in the request body you can use a url parameter like:
``https://api.mechakaren.xyz/.../math?equation=...``

Warning
-------

Although this is a nice way of making simple requests, however URL decoding can lead to incorrect equations being parsed.
For example, ``+`` is a space, so doing ``1 + 1`` will be parsed to ``1   1``.

Request Body Format
===================

JSON
----

.. code-block:: json

    {
        "equation": "MyEquation"
    }

Key, Value
----------

.. code-block:: text

    equation=MyEquation

Hierachy
========
The order it searches your request for the provided equation.

.. code-block:: text

    URL Parameter
        JSON Request Body
            Key, Value Request Body

Response
========
This endpoint returns a ``JSONResponse`` on all requests, even invalid. The URL is embedded in an array. Checkout the example response.

Example Response
----------------

.. code-block:: json

    {
        "Bearer": "Token-Owner-Email",
        "Results": {
            "Input": "MyEquation",
            "Output": "Result of MyEquation"
        }
    }
