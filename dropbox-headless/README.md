dropbox-headless
================

This role installs Dropbox on a headless device as a service.

Requirements
------------

You need a Dropbox account to link the device.
After first install, look at {{ dropbox_headless_logfile }} for info about how to link the device to your Dropbox account.

Role Variables
--------------

* **dropbox_headless_user:** The user to run dropbox service (Ex: dropbox)


Example Playbook
----------------


    - hosts: servers
      roles:
        - {
          role: dropbox-headless,
          dropbox_headless_user: 'dropbox'
        }

License
-------

BSD

