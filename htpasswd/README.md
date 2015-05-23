htpasswd
========

This role creates an htpasswd file with provided user/pass items.

Role Variables
--------------

* **htpasswd_file:** Full path for htpasswd file (Ex: '/etc/apache2/.htpasswd')
* **htpasswd_users:** List of user / pass (default: empty list)
* **htpasswd_user:** File's owner (default: 'root')
* **htpasswd_group:** File's group (default: htpasswd_user)
* **htpasswd_mode:** File's permissions (default: '0640')

Example Playbook
----------------

    - hosts: servers
      vars:
        auth_users:
          - user: 'test'
            pass: 'TestPasswd'
      roles:
        - {
          role: htpasswd,
          htpasswd_file: '/etc/nginx/.htpasswd',
          htpasswd_group: 'www-data',
          htpasswd_users: '{{ auth_users }}'
        }

License
-------

BSD
