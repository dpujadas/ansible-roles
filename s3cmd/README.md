s3cmd
=====

This role installs and configures [s3cmd](http://s3tools.org/s3cmd).

Role Variables
--------------

* **s3cmd_use_https:** Use https or not (default: 'True')
* **s3cmd_aws_access_key:** ACCESS_KEY_ID with privileges to create / delete / restore S3 objects (Ex: 'WDF45FR5GE5TGETER')
* **s3cmd_aws_secret_key:** SECRET_ACCESS_KEY with privileges to create / delete / restore S3 objects (Ex: 'SuperSecretAWSPass')
* **s3cmd_user:** User to configure (default: 'ubuntu')
* **s3cmd_group:** User's group (default: s3cmd_user)

Example Playbook
----------------

    - hosts: servers
      roles:
         - { 
            role: s3cmd,
            s3cmd_aws_access_key: '{{ aws_access_key }}',
            s3cmd_aws_secret_key: '{{ aws_secret_key }}',
            s3cmd_user: 'root'
        }

License
-------

BSD
