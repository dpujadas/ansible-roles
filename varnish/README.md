varnish
=======

This role installs [varnish](https://www.varnish-cache.org/).

Role Variables
--------------

* **varnish_default_vcl:** Path to default.vcl template (default: empty)

Example Playbook
----------------

    - hosts: servers
      roles:
         - { 
            role: varnish
         }

License
-------

BSD
