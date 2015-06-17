mongodb
=======

This role installs and configures [MongoDB](https://www.mongodb.org/)

Role Variables
--------------

* **mongodb_version:** Which version (2.6, 3.0, ...) to install (default: '2.6')
* **mongodb_subversion:** Which subversion (.2, .7, ...) to install (default: '.7')

Example Playbook
----------------

    - hosts: servers
      roles:
         - { 
            role: mongodb
        }

License
-------

BSD
