==========
holdmykeys
==========


.. image:: https://img.shields.io/pypi/v/holdmykeys.svg
        :target: https://pypi.python.org/pypi/holdmykeys

.. image:: https://img.shields.io/travis/hvnsweeting/holdmykeys.svg
        :target: https://travis-ci.org/hvnsweeting/holdmykeys

.. image:: https://readthedocs.org/projects/holdmykeys/badge/?version=latest
        :target: https://holdmykeys.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/hvnsweeting/holdmykeys/shield.svg
     :target: https://pyup.io/repos/github/hvnsweeting/holdmykeys/
     :alt: Updates



Auto manage one SSH public keys as authorized keys on hosts by one command.

You have ten servers, and 3 SSH keys, how to access to them all with one of
those keys? `holdmykeys` is a solution.

* Free software: MIT license

Usage
-----

Install::

  pip install holdmykeys

Run it to install as crontab job run hourly::

  holdmykeys hvnsweeting

That's it!

Features
--------

- One command
- Works in virtualenv

TODO
----

Support python2

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
