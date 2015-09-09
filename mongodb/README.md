mongodb
=======

This role installs and configures [MongoDB](https://www.mongodb.org/)

Role Variables
--------------

* **mongodb_version:** Which version (2.6, 3.0, ...) to install (default: '2.6')
* **mongodb_subversion:** Which subversion (.2, .7, ...) to install (default: '.7')
* **mongodb_conf_bind_ip:** Mongo conf bind_ip (default: '127.0.0.1')
* **mongodb_conf_auth:** Mongo conf auth (Ex: 'true')
* **mongodb_users:** List of mongo users to create. Each element must have the following structure:
  * **database:** Database name (Ex: 'test')
  * **user:** User's name (Ex: 'test')
  * **pwd:** User's password (Ex: 'SecretPass')
  * **roles:** List of roles (Ex: ['readWrite'])

Example Playbook
----------------

    - hosts: servers
      vars:
        mongo_users:
          - database: 'test'
            user: 'test'
            pwd: 'SecretPass'
            roles:
              - 'readWrite'
      roles:
        - {
            role: mongodb,
            mongodb_conf_auth: 'true',
            mongodb_conf_bind_ip: '',
            mongodb_users: '{{ mongo_users }}'
        }

License
-------

BSD
