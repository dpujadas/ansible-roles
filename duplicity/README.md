duplicity
=========

This role installs [duplicity](http://duplicity.nongnu.org/) and its wrapper [duply](http://duply.net/) and manages duply profiles.

Role Variables
--------------

* **duplicity_user:** User that will run backups (default: 'root')
* **duplicity_profiles:** List of duply profiles (name / source / max_age / cron) to manage (default: empty list)
* **duplicity_gpg_pass:** GPG pass to encrypt backups (Ex: 'SecretPass')
* **duplicity_aws_bucket:** AWS bucket where backups will be uploaded (Ex: 'duplicity-bucket')
* **duplicity_aws_user:** ACCESS_KEY_ID with read/write privileges to the bucket
* **duplicity_aws_pass:** SECRET_ACCESS_KEY with read/write privileges to the bucket

Dependencies
------------

* dpujadas/initial-setup

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      vars:
        duply_profiles:
          www:
            source: '/var/www'
            max_age: '1M'
            cron: daily
      roles:
        - {
            role: duplicity,
            duplicity_profiles: '{{ duply_profiles }}',
            duplicity_gpg_pass: 'SecretPass',
            duplicity_aws_bucket: 'duplicity-bucket',
            duplicity_aws_user: '{{ aws_access_key_id }}',
            duplicity_aws_pass: '{{ aws_secret_access_key }}'
        }

License
-------

BSD
