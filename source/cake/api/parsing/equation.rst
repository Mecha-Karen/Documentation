.. meta::
    :title: Documentation - Mecha Karen
    :type: website
    :url: https://docs.mechakaren.xyz/
    :description: Cake - Equation [Object]
    :theme-color: #f54646

.. currentmodule:: cake

***************
Equation Object
***************
This class must not be directly used in an ``if`` statement, when creating one from an ``Expression`` object.

.. code-block:: py

    >>> if (Expr == ...):
            ...

    # This is wrong!
    # It will ALWAYS be true
    # Instead try something like

    >>> if (Expr == ...).solve(*args, **kwargs) == ...:
            ...

    # This is saying, that if the solved equation is equal to something
    # Instead of saying ``if Equation:``


.. autoclass:: cake.Equation
    :members: