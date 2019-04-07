Senior HCM
============
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
