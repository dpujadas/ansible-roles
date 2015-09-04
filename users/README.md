users
=====

This role manages users, groups, home dirs, ...

Role Variables
--------------

* **users_list:** List of users. Each element must have the following structure:
  * **name:** User name (Ex: 'ubuntu')
  * **group:** User group (default: '{{ name }}')
  * **state:** User state (default: 'present')
  * **password:** User's password, set '\*' or '!' for nologin (Ex: '\*')
  * **shell:** User's shell (default: omit)
  * **home:** User's home dir (default: omit)
  * **createhome:** Create home dir or not (default: omit)
  * **chrooted:** Chroot user or not (default: undefined)

Example Playbook
----------------

    - hosts: servers
      vars
        users:
          - name: 'testuser'
            state: 'present'
            home: '/mnt/test'
            createhome: 'yes'
      roles:
        - { 
          role: users,
          users_list: {{ users }}
        }

License
-------

BSD
