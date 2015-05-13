nodejs
======

This role installs NodeJS and npm packages.

Role Variables
--------------

* **nodejs_modules:** List of nodejs modules to install via apt (default: empty list)
* **nodejs_npm_packages:** List of packages to install via npm (default: empty list)

Example Playbook
----------------

    - hosts: servers
      vars:
        npm_packages:
          - node-sass
      roles:
         - {
            role: nodejs,
            nodejs_npm_packages: '{{ npm_packages }}'
         }

License
-------

BSD
