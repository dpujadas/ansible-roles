php
===

This role installs and configures php (cli, fpm and mod_apache).

Role Variables
--------------

* **php_cli:** Install php_cli or not (default: true)
* **php_fpm:** Install php_fpm or not (default: false)
* **php_mod:** Install mod_apache or not (default: false)
* **php_modules:** List of php modules to install (default: empty list)
* **php_cli_options:** List of ini directives for php cli (default: empty list)
* **php_mod_options:** List of ini directives for php mod_apache (default: empty list)
* **php_fpm_options:** List of ini directives for php fpm (default: empty list)
* **php_fpm_pool_options:** List of ini directives for fpm pools (defult:
    - name: 'www'
      option: 'user'
      value: 'www-data'
    - name: 'www'
      option: 'listen'
      value: '/var/run/php5-fpm.sock'
    - name: 'www'
      option: 'listen.owner'
      value: 'www-data'
    - name: 'www'
      option: 'pm'
      value: 'dynamic'
    - name: 'www'
      option: 'pm.max_children'
      value: '5'
    - name: 'www'
      option: 'pm.min_spare_servers'
      value: '1'
    - name: 'www'
      option: 'pm.max_spare_servers'
      value: '3'
    - name: 'www'
      option: 'chdir'
      value: '/'
    )

Dependencies
------------

* ansible-roles/apache (if php_mod==true)

Example Playbook
----------------

    - hosts: servers
      roles:
         - {
            role: php,
            php_fpm: true
        }

License
-------

BSD
