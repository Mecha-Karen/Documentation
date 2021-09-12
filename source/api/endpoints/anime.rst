.. meta::
   :title: Documentation - Mecha Karen
   :type: website
   :url: https://docs.mechakaren.xyz/api
   :description: API Reference [Anime Endpoint]
   :theme-color: #f54646

**************
Anime Endpoint
**************
Recieve hundreds of anime gifs at your fingertips with many categories to choose from!

As a bonus for all API versions the library of gids will continue to grow and your welcome to add your own gifs by contacting one of our executives.

Categories
==========
* Angry
* Hug
* Idiot
* Kill
* Kiss
* Lick
* Pat
* Slap

Request Method
==============
This endpoint only accepts a ``GET`` request.

URL Patterns
============
The base URL for the anime endpoint is ``https://api.mechakaren.xyz/.../anime``.
 
` ``...`` represents the API version`.

To target a category you can either route it to the endpoint which will look like:
``https://api.mechakaren.xyz/.../anime/angry``

Or you can use the category parameter on the endpoint, which will look like:
``https://api.mechakaren.xyz/.../anime?category=angry``

Response
========
This endpoint returns a ``JSONResponse`` on all requests, even invalid. The URL is embedded in an array. Checkout the example response.

Example Response
----------------

.. code-block:: json

    {
        "Bearer": "Token-Owner-Email",
        "Category": "Chosen Category",
        "data": [
            "URL",
        ]
    }