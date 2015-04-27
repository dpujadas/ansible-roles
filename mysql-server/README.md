mysql-server
============

This role installs and configures a mysql server.

Role Variables
--------------

* **mysql_server_bind_address:** Network address mysql will listen (default: '0.0.0.0')
* **mysql_server_version:** Mysql version to install (default: '5.6')
* **mysql_server_root_password:** Root password

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: mysql-server, mysql_server_root_password: SuperSecretPass }

License
-------

BSD
