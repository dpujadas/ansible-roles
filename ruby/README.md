ruby
====

This role installs ruby and a list of gems.

Role Variables
--------------

* **ruby_gems:** List of gems to install (default: empty list)

Example Playbook
----------------

    - hosts: servers
      vars:
        gems:
          - sass
      roles:
        - { 
          role: ruby,
          ruby_gems: '{{ gems }}'
        }

License
-------

BSD
