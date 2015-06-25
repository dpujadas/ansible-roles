ip-alias
========

This role adds a secondary ip address to a device.

Role Variables
--------------

* **ip_alias_address:** Secondary ip address (Ex: '10.0.0.17')
* **ip_alias_netmask:** Secondary address netmask (default: '24')
* **ip_alias_device:** Device to add the secondary address (default: 'eth0')

Example Playbook
----------------

    - hosts: servers
      roles:
        - { 
            role: ip-alias,
            ip_alias_address: '10.0.0.27'
        }

License
-------

BSD
