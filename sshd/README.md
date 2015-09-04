sshd
====

This role manages ssh service.

Role Variables
--------------

* **sshd_password_authentication:** Allow (yes/no) password authentication (default: 'no')
* **sshd_chrooted_users:** List os users (name / home) to chroot (default: empty list)

Example Playbook
----------------

    - hosts: servers
      vars:
        users:
          - name: 'chrooteduser'
            home: '/home/chrooteduser'
      roles:
        - { 
          role: sshd,
          sshd_password_authentication: 'yes',
          sshd_chrooted_users: '{{ users }}'
        }

License
-------

BSD
