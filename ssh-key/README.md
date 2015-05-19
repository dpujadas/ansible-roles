ssh-key
=======

This role decrypts and installs an encrypted key.

Requirements
------------

Key must be encrypted using openssl as described in [this article](https://www.calazan.com/how-to-deploy-encrypted-copies-of-your-ssl-keys-and-other-files-with-ansible-and-openssl/)

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
