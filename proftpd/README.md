proftpd
=======

This role installs and configures [proftpd](http://www.proftpd.org/) as a standalone server.

Role Variables
--------------

* **proftpd_server_name:** Name displayed to connecting users (default: 'Debian')
* **proftpd_jail_users:** Jail all users in their homes (default: False)
* **proftpd_require_valid_shell:** Users require a valid shell listed in /etc/shells to login (default: 'on')

Example Playbook
----------------

    - hosts: servers
      roles:
        - { 
          role: proftpd,
          proftpd_server_name: 'FTP Server',
          proftpd_jail_users: True
        }

License
-------

BSD
