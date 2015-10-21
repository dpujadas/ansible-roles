blackfire
=========

This role installs and configures [Blackfire](https://blackfire.io/).

Role Variables
--------------

* **blackfire_collector:** Collector URL (default: 'https://blackfire.io')
* **blackfire_log_level:** Blackfire log level (default: '1')
* **blackfire_socket:** Socket to listen (default: 'unix:///var/run/blackfire/agent.sock')
* **blackfire_server_id:** Server id used to authenticate (Ex: '359b31dc-721c-4dba-b661-e7995f50bbef')
* **blackfire_server_token:** Server token used to authenticate (Ex: '89b52a06b635184b89e1d960d5fdf4213c80142dd35934d7bad7526c9f177e2e')

Example Playbook
----------------

    - hosts: servers
      roles:
        - { 
            role: blackfire,
            blackfire_server_id: '359b31dc-721c-4dba-b661-e7995f50bbef',
            blackfire_server_token: '89b52a06b635184b89e1d960d5fdf4213c80142dd35934d7bad7526c9f177e2e'
        }

License
-------

BSD
