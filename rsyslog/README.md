rsyslog
=======

This role installs and configures [rsyslog](http://www.rsyslog.com/).

Role Variables
--------------

* **rsyslog_confs:** List os custom configs (template / order / name) to enable (default: empty list)

Example Playbook
----------------

    - hosts: servers
      vars:
        custom_logs:
          - template: '/templates/custom-log.j2'
            order: '30'
            name: 'customlog'
      roles:
        - { 
          role: rsyslog,
          rsyslog_confs: '{{ custom_logs }}'
        }

License
-------

BSD
