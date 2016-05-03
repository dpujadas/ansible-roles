letsencrypt
===========

This role:
* installs and configures [letsencrypt.sh](https://github.com/lukas2511/letsencrypt.sh)
* provides some hooks (currently only for AWS and dns-01 challenge)

Requirements
------------

* python-pip
* git

Role Variables
--------------

* **letsencrypt_dir:** Directory to checkout letsencrypt.sh repo (default: '/opt/letsencrypt')
* **letsencrypt_version:** Letsencrypt.sh version/branch (default: 'master')
* **letsencrypt_staging:** Use letsencrypt.org staging server (default: false)
* **letsencrypt_challenge_type:** Which challenge type to use (currently only http-01 or dns-01) (default: 'dns-01')
* **letsencrypt_hook:** Name of hook script (default: 'hook-aws-{{ letsencrypt_challenge_type }}.py')
* **letsencrypt_email:** Email to regiser with letsencrypt.org
* **letsencrypt_key:** Content for private_key.pem file (default: '')
* **letsencrypt_set_cron:** Setup daily cron job or not (default: false)

Example Playbook
----------------

    - hosts: servers
      roles:
        - { 
          role: letsencrypt,
          letsencrypt_email: 'admin@example.com'
        }

License
-------

BSD

Hooks
-----

### hook-aws-dns-01.py
Resolves dns-01 challenges using AWS Route53 and uploads the generated certificate using AWS IAM. Required authorizations:
* route53:ListHostedZones
* route53:ChangeResourceRecordSets
* route53:GetChange
* iam:UploadServerCertificate

Based on [letsencrypt-aws](letsencrypt-aws)