mysql-dbs
=========

This role creates databases and manages user privileges.

Role Variables
--------------

* **mysql_dbs_host:** Host running the database (default: 'localhost')
* **mysql_dbs_user:** The username used to authenticate with (default: 'root')
* **mysql_dbs_password:** The password used to authenticate with (default: '')
* **mysql_dbs:** List of DBs (name / user / pass / host) to create (default: empty list)

Example Playbook
----------------

    - hosts: servers
      vars:
        dbs:
          - name: 'dbname'
            user: 'username'
            pass: 'SuperSecretPass'
            host: '%'
      roles:
         - { 
            role: mysql-dbs,
            mysql_dbs: '{{ dbs }}'
        }

License
-------

BSD

