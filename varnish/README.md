varnish
=======

This role installs [varnish](https://www.varnish-cache.org/).

Role Variables
--------------

* **varnish_default_vcl:** Path to default.vcl template (default: empty)
* **varnish_listen_address:** Default address to bind to (default: '')
* **varnish_listen_port:** Default port to bind to (default: '6081')
* **varnish_admin_listen_address:** Telnet admin interface listen address (default: '127.0.0.1')
* **varnish_admin_listen_port:** Telnet admin interface listen port (default: '6082')

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
