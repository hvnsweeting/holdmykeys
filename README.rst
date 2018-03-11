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

Example
-------

On my Raspberry Pi

.. code-block:: bash

  pi@raspberrypi:~ $ . env3/bin/activate
  (env3) pi@raspberrypi:~ $ pip install holdmykeys
  Collecting holdmykeys
    Downloading https://www.piwheels.org/simple/holdmykeys/holdmykeys-0.1.0-py2.py3-none-any.whl
  Requirement already satisfied: Click>=6.0 in ./env3/lib/python3.5/site-packages (from holdmykeys)
  Installing collected packages: holdmykeys
  Successfully installed holdmykeys-0.1.0
  (env3) pi@raspberrypi:~ $ holdmykeys hvnsweeting
  Ensuring all keys in authorized_keys
  Adding this tool to run every hour in crontab
  no crontab for pi
  (env3) pi@raspberrypi:~ $ crontab -l
  0 */1 * * * /home/pi/env3/bin/python3 holdmykeys --silent hvnsweeting
  (env3) pi@raspberrypi:~ $ cat ~/.ssh/authorized_keys
  ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDpojmsipUaM5dmQPq3lUkDRPT1DkGi9A2+yy0dVZCj7pfdOEnbZGmB68+onhMOZf7kd4I8s3vaczGzVFor7Zv38iD36$6gddwmw/xaQLwhsojj6QfmBQaUsr/y2AZvHoISnx1EsEf2kKI6aWG77jhzxwOMgMIwo7K3hEGfPomIdiSgsHnS6UgbzDSYiLqeSbIBXqOfXybDU6jgQW7EeiVQgcXLqaU$uONVnjGLsF4S5IaHs7M7bqcklLKTwHBZu3Vr21FlNp/PJ6nH4qwd0KH3gwkR3AZaRHHkYeUUItgrQEU+6jNgcK5vxtakD6cRuy6WrKEzve4n56sxrZrzibQN

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
