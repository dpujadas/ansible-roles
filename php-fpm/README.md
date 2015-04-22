Role Name
=========

This role installs and configures php-fpm using [ondrej repo](https://launchpad.net/~ondrej/+archive/ubuntu/php5) for latest PHP packages.

Role Variables
--------------

* **php_fpm_modules:** List of modules to install (default: empty list)
* **php_fpm_options:** List of options (section / option / value) to set in php.ini (default: empty list)

Example Playbook
----------------

    - hosts: servers
      roles:
        - { 
          role: php-fpm, 
          php_fpm_options: [
            { "section": "PHP", "option": "post_max_size", "value": "20M" }
          ]
        }

License
-------

BSD
