nginx
=====

This role installs nginx [Pre-Built Packages](http://nginx.org/en/linux_packages.html), leaving the server without predefined sites.

Role Variables
--------------

* **nginx_version:** Package version to install, ex: mainline (default: '')
* **nginx_worker_processes:** Number of worker processes (default: '1')
* **nginx_worker_connections:** Maximum number of simultaneous connections that can be opened by a worker process (default: '1024')
* **nginx_user:** Defines user and group credentials used by worker processes (default: 'www-data')
* **nginx_sendfile:** Enables or disables the use of sendfile() (default: 'on')
* **nginx_tcp_nopush:** Enables or disables the use of the TCP_NOPUSH socket option on FreeBSD or the TCP_CORK socket option on Linux (default: 'on')
* **nginx_tcp_nodelay:** Enables or disables the use of the TCP_NODELAY option (default: 'on')
* **nginx_keepalive_timeout:** Sets a timeout during which a keep-alive client connection will stay open on the server side (default: '65')
* **nginx_types_hash_max_size:** Sets the maximum size of the types hash tables (default: '2048')
* **nginx_custom_directives:** List of custom directives (directive / value) to apply (default: empty list)
* **nginx_access_log:** Path to access log (default: 'off')
* **nginx_error_log:** Path to error log (default: '/var/log/nginx/error.log')

Example Playbook
----------------

    - hosts: servers
      roles:
        - { 
          role: nginx, 
          nginx_custom_directives: [
            { "directive": "client_max_body_size", "value": "20M" }
          ]
        }

License
-------

BSD