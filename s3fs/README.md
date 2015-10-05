s3fs
====

This role installs [s3fs](https://github.com/s3fs-fuse/s3fs-fuse).

Role Variables
--------------

* **s3fs_version:** s3fs version to install (default: '1.79')

Example Playbook
----------------

    - hosts: servers
      roles:
        - { 
          role: s3fs
        }

License
-------

BSD
