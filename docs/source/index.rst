Welcome to Thorlabs PM400's documentation!
==========================================

How to run::

    $ aqctl_artiq_thorlabs_pm400.py -d device

Then, send commands to it via the ``sipyco_rpctool`` utility::

    $ sipyco_rpctool 127.0.0.1 3285 call set_wavelength ${wavelength}

API
---

.. automodule:: artiq_thorlabs_pm400.driver
    :members:


ARTIQ Controller
----------------

.. argparse::
   :ref: artiq_thorlabs_pm400.aqctl_artiq_thorlabs_pm400.get_argparser
   :prog: aqctl_artiq_thorlabs_pm400


