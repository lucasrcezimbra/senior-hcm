Senior HCM
============

.. image:: https://badge.fury.io/py/senior-hcm.svg
    :target: https://badge.fury.io/py/senior-hcm
    :alt: PyPI
.. image:: https://travis-ci.org/Lrcezimbra/senior-hcm.svg?branch=master
    :target: https://travis-ci.org/Lrcezimbra/senior-hcm
    :alt: Travis CI Build
.. image:: https://coveralls.io/repos/github/Lrcezimbra/senior-hcm/badge.svg?branch=master
    :target: https://coveralls.io/github/Lrcezimbra/senior-hcm?branch=master
    :alt: Coverage
.. image:: https://pyup.io/repos/github/Lrcezimbra/senior-hcm/shield.svg
    :target: https://pyup.io/repos/github/Lrcezimbra/senior-hcm/
    :alt: Updates
.. image:: https://pyup.io/repos/github/Lrcezimbra/senior-hcm/python-3-shield.svg
    :target: https://pyup.io/repos/github/Lrcezimbra/senior-hcm/
    :alt: Python 3
     
Client to access `Senior HCM`_ API 

.. _Senior HCM: https://hcm.senior.com.br/

Installation
~~~~~~~~~~~~~
``pip install senior-hcm``


How to Use
~~~~~~~~~~~~~
.. code-block:: python

    from senior_hcm import SeniorHcm

    # Login
    senior = SeniorHcm('example@mail.com', 'password')

    # Recent payrolls
    senior.get_recent_payrolls()
    
    # Last payroll
    senior.get_last_payroll()
    
    
Contributing
~~~~~~~~~~~~~
Contributions are welcome, feel free to open an Issue or Pull Request
