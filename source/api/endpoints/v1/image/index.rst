.. meta::
   :title: Documentation - Mecha Karen
   :type: website
   :url: https://docs.mechakaren.xyz/api
   :description: API Reference [Image Endpoint]
   :theme-color: #f54646

**************
Image Endpoint
**************
Edit images using various filters, effects and equations. The max image size as of now is ``1.5mb``.

We plan to add features to return frames of gif/video without physically saving it as a file.

Endpoints
=========
Currently being written up, Coming Soon™️

Accepted Image Types
====================
* PNG
* GIF
* JPG
* JPEG
* ICO

Request Method
==============
This endpoint only accepts a ``GET`` request.

URL Patterns
============
The base URL for the chatbot endpoint is ``https://api.mechakaren.xyz/.../image``

` ``...`` represents the API version`.

For selecting filters you can use the ``endpoint`` URL parameter. However, each endpoint has there own route, which would look like:
``https://api.mechakaren.xyz/.../image/endpoint-here``

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

File
----
If you wish to use a file as your image when making a request, send it as a ``multipart/form-data`` request.

Example Request
^^^^^^^^^^^^^^^

.. code-block:: python
    :caption: Example written in python using the ``requests`` library

    import requests

    imagePath = './my-image.png'
    url = 'https://api.mechakaren.xyz/.../image/invert'
    apiToken = ''
    
    with open(imagePath, 'rb') as f:
        files = {'myFile': f}
        r = requests.get(
                url, 
                headers={'Authorization': apiToken}, 
                files=files,
                stream=True
            )
    raw = r.raw
    raw.seek(0)

    with open('output.png', 'wb') as f:
        f.write(raw.read())


Hierachy
========
The order it searches your request for the provided equation.

.. code-block:: text

    File
        URL Parameter
            JSON Request Body
                Key, Value Request Body
