filesystem
==========

This role allows formatting and mounting devices.

Role Variables
--------------

* **filesystem_fs:** List of devices. Each element must have the following structure:
  * **device:** Device name (Ex: '/dev/xvdf')
  * **type:** Filesystem type (Ex: 'ext4')
  * **mountpoint:** Mount point for device (Ex: '/mnt/www')
  * **opts:** Mount opts for device (default: 'defaults,nobootwait')

Example Playbook
----------------

    - hosts: servers
      vars:
        filesystems:
          - device: '/dev/xvdf'
            type: 'ext4',
            mountpoint: '/mnt/www',
            opts: 'defaults'
      roles:
        - {
          role: filesystem,
          filesystem_fs: '{{ filesystems }}'
        }

License
-------

BSD
