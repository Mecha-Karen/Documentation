.. meta::
   :title: Documentation - Mecha Karen
   :type: website
   :url: https://docs.mechakaren.xyz/api
   :description: API Reference [Image Endpoint]
   :theme-color: #f54646

*********
Endpoints
*********
All the filters, effects for the image endpoint, with a description of what they do.

Quick Links
===========

* `Invert <#invertfilter>`_
* `Equalize <#equalizefilter>`_
* `Grayscale <#grayscalefilter>`_
* `Mirror <#mirrorfilter>`_
* `Posterize <#posterizefilter>`_

.. _InvertFilter:

Invert
======
Negate (invert) the image.

URL Parameters
--------------
* authorization - Token used for authorizing requests [Optional]
* url - The URL of the image to invert [Optional]
* as_type - The type of image to return [Not Implemented]
* input_type - The image extension [Optional] [Default="Auto"]


.. _EqualizeFilter:

Equalize
========
Equalize the histogram of the image. This function creates a consistent distribution of grayscale values in the output image by applying a non-linear mapping to the input image.

URL Parameters
--------------
* authorization - Token used for authorizing requests [Optional]
* url - The URL of the image to invert [Optional]
* as_type - The type of image to return [Not Implemented]
* input_type - The image extension [Optional] [Default="Auto"]

.. _GrayscaleFilter:
.. _GreyscaleFilter:

Grayscale
=========
Convert the image to grayscale.

URL Parameters
--------------
* authorization - Token used for authorizing requests [Optional]
* url - The URL of the image to invert [Optional]
* as_type - The type of image to return [Not Implemented]
* input_type - The image extension [Optional] [Default="Auto"]

Aliases
-------
Greyscale

.. _MirrorFilter:

Mirror
======
Horizontally flip the image (left to right).

URL Parameters
--------------
* authorization - Token used for authorizing requests [Optional]
* url - The URL of the image to invert [Optional]
* as_type - The type of image to return [Not Implemented]
* input_type - The image extension [Optional] [Default="Auto"]

.. _PosterizeFilter:

Posterize
=========
Reduce the number of bits for each color channel.

URL Parameters
--------------
* authorization - Token used for authorizing requests [Optional]
* url - The URL of the image to invert [Optional]
* as_type - The type of image to return [Not Implemented]
* input_type - The image extension [Optional] [Default="Auto"]
* bits - For each channel, the amount of bits to keep (1-8) [Optional] [Default=1]


