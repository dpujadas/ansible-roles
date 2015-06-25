nginx
=====

This role installs and configures nginx, using community packages or openresty source code.

Role Variables
--------------

* **nginx_source:** Which source to use: [community](http://nginx.org) or [openresty](http://openresty.org/) (default: 'community')
* **nginx_version:** Package community version to install, ex: mainline (default: '')
* **nginx_worker_processes:** Number of worker processes (default: '1')
* **nginx_worker_connections:** Maximum number of simultaneous connections that can be opened by a worker process (default: '1024')
* **nginx_user:** Defines user credentials used by worker processes (default: 'www-data')
* **nginx_group:** Defines group credentials used by worker processes (default: nginx_user)
* **nginx_sendfile:** Enables or disables the use of sendfile() (default: 'on')
* **nginx_tcp_nopush:** Enables or disables the use of the TCP_NOPUSH socket option on FreeBSD or the TCP_CORK socket option on Linux (default: 'on')
* **nginx_tcp_nodelay:** Enables or disables the use of the TCP_NODELAY option (default: 'on')
* **nginx_keepalive_timeout:** Sets a timeout during which a keep-alive client connection will stay open on the server side (default: '65')
* **nginx_types_hash_max_size:** Sets the maximum size of the types hash tables (default: '2048')
* **nginx_custom_directives:** List of custom directives (directive: value) to apply (default: empty)
* **nginx_access_log:** Path to access log (default: 'off')
* **nginx_error_log:** Path to error log (default: '/var/log/nginx/error.log')
* **nginx_doc_root:** Directory where apps will be installed (Ex: '/var/www')
* **nginx_sites:** List of sites (server_name / template / filename) to enable. Filename field is optional (server_name is used if not defined) but usefull in case load order is important (default: empty list)
* **nginx_confs:** List of available confs (conf_name / template), .conf filenames are automatically included (default: empty list)

Example Playbook
----------------

    - hosts: servers
      vars:
        custom_directives:
          client_max_body_size: '20M'
          ssl_session_timeout: '10m'
        sites:
          - template: 'path-to-template-1.j2'
            server_name: 'www.site.com'
          - template: 'path-to-template-2.j2'
            server_name: 'all.site.com'
            filename: 'z-all.site.com' # We need this site to be the last
      roles:
        - { 
          role: nginx,
          nginx_doc_root: '/var/www',
          nginx_custom_directives: {{ custom_directives }},
          nginx_sites: '{{ sites }}'
        }

License
-------

BSD
