.. TODO_test documentation master file, created by
   sphinx-quickstart on Tue Sep 17 12:50:50 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. _default_content:

Example of reStructuredText file
=====================================

https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst

1.   Änderungsdokumentation
---------------------------

+----------------+---------+-------------+--------------------+
|  Version       |    MCR  | Firma (Name)|Beschreibung        |
+================+=========+=============+====================+
| Carlos Rosich  |   9101  |   Mirkwood  |  Creation          |
+----------------+---------+-------------+--------------------+
| body row 2     |           Cells may span column            |
+----------------+---------+-------------+--------------------+

2.  Basic text styles
----------------------
- Italic :      ``*your_text*``    -> *your_text*
- Bold text :   ``**your_text**``  -> **your_text**
- Special characters like ``'*', '.. ' or '|'`` should be scaped using ````<char>````

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse turpis dolor,
consequat sed eros non, bibendum sodales ante. Aliquam vestibulum finibus tortor
quis aliquam. Maecenas lacinia lectus eu dolor *sodales venenatis*. Vestibulum iaculis
sem purus, **finibus cursus neque ullamcorper** quis. Phasellus suscipit nunc sit amet
ornare bibendum. Vivamus iaculis dictum euismod. Cras vitae mollis nulla.


  " *Sed bibendum ligula nisi, pellentesque egestas tortor aliquam sed.
  Cras ac nibh ex. Aliquam erat volutpat. Nunc sed eleifend magna, at euismod
  nisi. Morbi vitae consequat magna, sit amet luctus lorem.* "

Vivamus et magna non diam ultrices condimentum. Donec sed congue magna. Mauris
viverra enim eget diam placerat, eget facilisis est pharetra. Curabitur eget
neque a arcu suscipit scelerisque. Nullam nisl elit, rhoncus nec ornare a,
consequat et dui. Proin finibus viverra tellus nec venenatis.

Vivamus vitae
velit ut nibh placerat interdum at a mi. Donec vitae nunc rhoncus, luctus velit
vitae, malesuada risus. Morbi tempus diam enim, ac mattis diam facilisis non.
Cras laoreet metus non leo lacinia, venenatis sagittis felis ultricies. Cras
viverra nibh ac faucibus semper. Curabitur condimentum quis erat sit amet
convallis.



3.  Checkboxes
--------------

This are several items that can be checked :
  .. checkbox:: Item 1
    :checked: no
  .. checkbox:: Item 2

  .. checkbox:: Item 3
    :checked: no

.. todo:: Add a ``.. checkbox::``  parameter to the Sphinx checkbox directive allowing to indicate if the checkbox should be displayed as checked by default or not.

4.  images
----------
.. todo:: Add images section to the *Default* doku

4. Things TODO
--------------
The custom directive ``.. todolist::`` displays a list of all TODO elements on a project

.. todolist::
