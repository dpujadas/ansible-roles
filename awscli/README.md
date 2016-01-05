awscli
======

This role installs awscli using pip, enables auto completion for awscli commands and, optionally, sets up awscli's config file.

Role Variables
--------------

* **awscli_setup_config:** Set up config file or not (default: True)
* **awscli_user:** User to configure (default: ubuntu)
* **awscli_group:** User's group (default: ubuntu)
* **awscli_aws_access_key_id:** ACCESS_KEY_ID with privileges to perform required actions
* **awscli_aws_secret_access_key:** SECRET_ACCESS_KEY with privileges to perform required actions
* **awscli_region:** Default AWS region for awscli commands

Example Playbook
----------------

    - hosts: servers
      roles:
        - {
            role: awscli,
            awscli_aws_access_key_id: 'your_access_key_id',
            awscli_aws_secret_access_key: 'your_secret_access_key',
            awscli_region: 'us-east-1'
        }

License
-------

BSD