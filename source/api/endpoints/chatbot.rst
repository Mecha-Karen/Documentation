.. meta::
   :title: Documentation - Mecha Karen
   :type: website
   :url: https://docs.mechakaren.xyz/api
   :description: API Reference [Chatbot Endpoint]
   :theme-color: #f54646


****************
Chatbot Endpoint
****************
Speak to self learning AI, new training data provided is implemented after it deemed safe meaning it doesn't contain any of the following:

* NSFW Content
* Links to other places
* Offensive comments

    * Racial Slurs
    * Homophobic Phrases
    * etc.

Request Method
==============
This endpoint only accepts a ``GET`` request.

URL Patterns
============
The base URL for the chatbot endpoint is ``https://api.mechakaren.xyz/.../chatbot``

` ``...`` represents the API version`.

Instead of adding the ``message`` in the request body you can use a url parameter like:
``https://api.mechakaren.xyz/.../chatbot?message=...``

Request Body Format
===================
You can provide your message in your request body to prevent URL decode errors from ruining your message.

JSON
----

.. code-block:: json

    {
        "message": "MyMessage"
    }

Key, Value
----------

.. code-block:: text

    message=MyMessage

Response
========
This endpoint returns a ``JSONResponse`` on all requests, even invalid. The URL is embedded in an array. Checkout the example response.

Example Response
----------------

.. code-block:: json

    {
        "Bearer": "Token-Owner-Email",
        "response": {
            "tags": [],
            "callback": "%message%",
            "answer": "ChatBot-Message"
        }
    }