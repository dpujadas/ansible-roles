deployment
==========

This role creates a PHP deployment environment (creates app_root path, installs git and composer, ...)

Role Variables
--------------

* **deployment_root:** Directory where code will be deployed, usually '/var/www'
* **deployment_user:** User that will perform deploys (default: 'www-data')
* **deployment_group:** Group that will perform deploys (default: 'www-data')
* **deployment_pass:** Password for deployment user (default: '*', which means no password)
* **deployment_home:** Home dir for deployment user (default: 'omit')
* **deployment_root_type:** Indicates the type of node where code will be deployed. Possible values: 'file', 'nfs' (default: 'file')
* **deployment_extra_packages:** List of extra packages needed for deployment, appended to deployment_packages list (default: empty list)
* **deployment_authorized_keys:** If set, will be added to deployment_user's authorized_keys.
* **deployment_extra_dirs:** List of directories needed for deployment process which must belog to deployment_user (defaul: empty list)
* **deployment_type_php:** Indicates if the deployment environment uses PHP in order to include php-related stuff (default: false).
* **deployment_github_token:** If set, will be used by composer to download code from Github.
* **deployment_use_php_fpm:** Indicates if server is using php-fpm (default: false)

Example Playbook
----------------

    - hosts: servers
      roles:
        - { 
            role: deployment,
            deployment_root: '/var/www',
            deployment_root_type: 'nfs'
        }

License
-------

BSD
