deployment
==========

This role creates a PHP deployment environment (creates app_root path, installs git and composer, ...)

Role Variables
--------------

* **deployment_root:** Directory where code will be deployed, usually /var/www
* **deployment_user:** User that will perform deploys (default: 'www-data')
* **deployment_group:** Group that will perform deploys (default: 'www-data')
* **deployment_github_token:** If set, will be used by composer to download code from Github.
* **deployment_use_php_fpm:** Indicates if server is using php-fpm (default: false)

Example Playbook
----------------

    - hosts: servers
      roles:
        - { 
            role: deployment,
            deployment_root: '/var/www'
        }

License
-------

BSD
