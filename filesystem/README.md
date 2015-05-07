filesystem
==========

This role allows formatting and mounting devices.

Role Variables
--------------

* **filesystem_device:** Device name (Ex: '/dev/xvdf')
* **filesystem_type:** Filesystem type (Ex: 'ext4')
* **filesystem_mountpoint:** Mount point for device (Ex: '/mnt/www')

Example Playbook
----------------

    - hosts: servers
      roles:
         - {
            role: filesystem,
            filesystem_device: '/dev/xvdf',
            filesystem_type: 'ext4',
            filesystem_mountpoint: '/mnt/www'
         }

License
-------

BSD
