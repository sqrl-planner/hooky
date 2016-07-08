Hooky
=====

Hooky is a Python Module have a list like object called List, and a dict like object called Dict.

The difference between UserList/UserDict and List/Dict is that List/Dict have four members which will call
when List/Dict is changed.


Demo
----

.. literalinclude:: demo.py
    :language: python
    :linenos:


API Reference
-------------

.. automodule:: hooky

.. autoclass:: Hook
    :members:  _before_add, _after_add, _before_del, _after_del

.. autoclass:: List

.. autoclass:: Dict

