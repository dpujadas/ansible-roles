wkhtmltopdf
===========

This role downloads and installs [wkhtmltopdf](http://wkhtmltopdf.org/).

Role Variables
--------------

* **wkhtmltopdf_url:** URL to download deb package (default: 'http://downloads.sourceforge.net/project/wkhtmltopdf/archive/0.12.2/wkhtmltox-0.12.2_linux-trusty-amd64.deb')

Example Playbook
----------------

    - hosts: servers
      roles:
        - { 
          role: wkhtmltopdf
        }

License
-------

BSD
