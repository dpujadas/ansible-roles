redis-server
============

This role installs and configures a redis server using [chris-lea repo](https://launchpad.net/~chris-lea/+ppa-packages) for latest packages.

Role Variables
--------------

* **redis_server_port:** Port where redis will accept connections (default: '6379')
* **redis_server_slaveof:** To make this instance a copy of another Redis server (default: '')

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: redis-server }

License
-------

BSD
