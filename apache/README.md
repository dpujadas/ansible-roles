apache
======

This role installs and manages (config, sites, ...) an apache server.

Role Variables
--------------

* **apache_user:** User owner of the apache process (default: 'www-data')
* **apache_group:** Group owner of the apache process (default: apache_user)
* **apache_packages:** List of packages to install (default: apache2, apache2-mpm-prefork, apache2-utils)
* **apache_mods_enabled:** List of apache modules to install (default: empty list)
* **apache_sites:** List of sites (server_name / template) to enable (default: empty list)
* **apache_auth_users:** List of users (user / pass) to allow in htpasswd file (default: empty list)
* **apache_doc_root:** Directory where apps will be installed (Ex: '/var/www')

Example Playbook
----------------

    - hosts: servers
      roles:
         - { 
            role: apache,
            apache_doc_root: '/var/www'
         }

License
-------

BSD
