duplicity
=========

This role installs [duplicity](http://duplicity.nongnu.org/) and its wrapper [duply](http://duply.net/) and manages duply profiles using S3 as backend.

Role Variables
--------------

* **duplicity_user:** User that will run backups (default: 'root')
* **duplicity_profiles:** List of duply profiles (key / value) to manage. Each element must have the following structure:
  * **source:** Directory to backup (Ex: '/var/www')
  * **max_age:** Max time to keep files before purge (Ex: '6M')
  * **max_fullbkp_age:** Max time from last full backup (Ex: '2W')
  * **cron:** Special time for cronjob (Ex: 'daily')
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
            max_fullbkp_age: '1W'
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
