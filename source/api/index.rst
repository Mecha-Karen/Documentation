.. meta::
    :title: Documentation - Mecha Karen
    :type: website
    :url: https://docs.mechakaren.xyz/api
    :description: API Documentation
    :theme-color: #f54646

API
===

Our API is the backbone for many of our great creations including our dashboard, database and discord bot.
Inorder to access our API you will need an ``Access Token``.

.. _HowToGetToken:

How do I get a Access Token?
----------------------------
Firstly, you need to sign up to our API. If you have already, you can simply login.

Once you have logged in, you will see a screen like:

.. figure:: images/preview.png
    :width: 400px
    :align: center
    :alt: Dashboard Preview

Click the ``Create Token`` button and it will create you a new token! You can modify your token by clicking:

.. figure:: images/edit.png
    :align: center
    :alt: Edit Token

Same way for deleting a token, you can simply press the red icon.

And thats it you have created your very own token, which you can use for accessing our api!

To copy the value of your token you can click the `Click to show` text from the dashboard or go to the edit page and copy from info as show below:

.. figure:: images/copy.png
    :align: center
    :alt: Copy access token value


Making Requests
---------------
Inorder to make requests you will need an access token, which can be created from `here <https://api.mechakaren.xyz>`_.
For steps and guidance check out :ref:`HowToGetToken`.

You can 2 requests per second, if you exceed that limit, you will be hit with a ratelimit. If you continue to make requests your IP will be blacklisted from accessing our websites.
For larger applications you will need to send us an email at ``admin@mechakaren.xyz`` and we will approve your request. In the future we plan to expand to a larger ratelimit.

Each request will require your API Token to be included either in the url with they key `authorization` or your headers (Authorzation).

Example Request
^^^^^^^^^^^^^^^

.. code-block:: py
    :caption: Endpoint used in this example was the math endpoint

    import requests

    authorization = 'My-API-Token'
    to_calculate = '1 plus 1'
    base_url = 'https://api.mechakaren.xyz/v1/math'

    r = requests.get(base_url, params={'authorization': authorization}, json={'equation': to_calculate})
    json = r.json()
    print(r['Results']['Input'], r['Results']['Output'])
