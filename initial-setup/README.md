initial-setup
=============

This role performs several tasks usually performed after installing a new server.

Role Variables
--------------

* **initial_setup_full_upgrade:** Perform a full server upgrade (default: false)
* **initial_setup_timezone:** Server's timezone (default: '')
* **initial_setup_management_user:** Management user (default: 'ubuntu')
* **initial_setup_management_public_key:** Management user's public key (default: empty)
* **initial_setup_management_from:** List of comma-separated management allowed origins (default: 'localhost,10.0.*')
* **initial_setup_create_dns_record:** Create Route53 DNS record or not (default: false)
* **initial_setup_localdomain:** Internal domain name used in FQDN, mandatory if initial_setup_create_dns_record is true (Ex: 'example.lan', default: 'localdomain')
* **initial_setup_route53_ttl:** DNS record TTL (default: '300')
* **initial_setup_aws_access_key:** ACCESS_KEY_ID with privileges to create Route53 records, mandatory if initial_setup_create_dns_record is true (default: '')
* **initial_setup_aws_secret_key:** SECRET_ACCESS_KEY with privileges to create Route53 records, mandatory if initial_setup_create_dns_record is true (default: '')
* **initial_setup_locales:** List of locales to install (default: empty list)
* **initial_setup_create_swap:** Create swapfile or not (default: false)
* **initial_setup_swap_size:** Swap file size, in Mb (default: 1024)
* **initial_setup_umask:** When defined, sets system's default umask using [octal notation](https://en.wikipedia.org/wiki/Umask#Setting_the_mask_using_octal_notation) (Ex: '0002')
* **initial_setup_host_entries:** List of entries to add to /etc/hosts file (default: empty list)
* **initial_setup_localhosts:** List of alternative names to localhost (default: empty list)

Example Playbook
----------------

    - hosts: servers
      vars:
        host_entries:
          '10.0.0.1':
            - host1.localdomain
            - host2.localdomain
          '10.0.0.2':
            - host3.localdomain
      roles:
         - {
            role: initial-setup,
            initial_setup_full_upgrade: true,
            initial_setup_host_entries: host_entries
        }

License
-------

BSD
