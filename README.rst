===============================
ble-button
===============================


.. image:: https://img.shields.io/pypi/v/blebutton.svg
        :target: https://pypi.python.org/pypi/blebutton

.. image:: https://img.shields.io/travis/IlyaSukhanov/blebutton.svg
        :target: https://travis-ci.org/IlyaSukhanov/blebutton

.. image:: https://readthedocs.org/projects/blebutton/badge/?version=latest
        :target: https://blebutton.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/IlyaSukhanov/blebutton/shield.svg
     :target: https://pyup.io/repos/github/IlyaSukhanov/blebutton/
     :alt: Updates


BLE Driver for V.ALRT button.

This is an experimental, unofficial implementation of driver for V.ALRT button
device by VSN mobil. Its possible that it will also work with V.BTTN, but those
devices are harder to procure.

This project requires a patched version of pygatt. PRs with patches will be
opened against main project.


Features
--------

* Connect
* Trigger events when button is pressed
* Change button configuration (alarm modes, button press type)
* Beep alerts
* Version / Serial number readout
* Fall detection

Not implemented
---------------
* Battery level
* Gyro data
* Arbitrary LED setting (There has got to be a way to do this)
