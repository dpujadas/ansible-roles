ssh-key
=======

This role decrypts and installs an encrypted key.

Role Variables
--------------

* **ssh_key_user:** Key user (Ex: 'ubuntu')
* **ssh_key_group:** Key group (default '{{ ssh_key_user }}')
* **ssh_key_name:** Key name (default: 'id_rsa')
* **ssh_key_private_key:** Encrypted key (Ex: 'files/id_rsa')
* **ssh_key_force:** Perform key re-deployment (default: 'no')

Example Playbook
----------------

    - hosts: servers
      roles:
         - {
            role: ssh-key,
            ssh_key_user: 'ubuntu',
            ssh_key_private_key: 'files/id_rsa',
            ssh_key_password: 'SuperSecretPass'
         }

License
-------

BSD
