initial-setup
=============

This role performs several tasks usually performed after installing a new server.

Role Variables
--------------

* **initial_setup_full_upgrade:** Perform a full server upgrade (default: false)

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: initial-setup, initial_setup_full_upgrade: true }

License
-------

BSD
