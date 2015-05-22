decrypt-file
============

This role decrypts and installs encrypted files.

Requirements
------------

Files must be encrypted using openssl as described in [this article](https://www.calazan.com/how-to-deploy-encrypted-copies-of-your-ssl-keys-and-other-files-with-ansible-and-openssl/)

Role Variables
--------------

* **decrypt_file_password:** Password used to encrypt/decrypt (Ex: 'SecretPassword')
* **decrypt_file_files:** List of files to decrypt. Each element must have the following structure:
  * **content:** Path to encrypted file (Ex: 'files/id_rsa')
  * **dest:** Full path for decrypted file (Ex: '~www-data/.ssh/id_rsa')
  * **owner:** Decrypted file's owner (Ex: 'www-data')
  * **group:** Decrypted file's group (default: owner)
  * **file_mode:** Decrypted file's mode (default: '0600')
  * **dir_mode:** Decrypted file path's mode (default: '0700')

Example Playbook
----------------

    - hosts: servers
      vars:
        app_user: 'www-data'
        encrypted_files:
          - content: 'files/id_rsa'
            dest: '~{{ app_user }}/.ssh/id_rsa'
            owner: '{{ app_user }}'
      roles:
         - {
            role: decrypt-file,
            decrypt_file_files: '{{ encrypted_files }}',
            decrypt_file_password: 'SuperSecretPass'
         }

License
-------

BSD
