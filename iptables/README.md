iptables
========

This role installs iptables-persistent package and configures the server for masquerading.

Role Variables
--------------

* **iptables_masq_source:** Source address for masquerading (default: '10.0.0.0/16')
* **iptables_dnat_rules:** List of dnat rules (dport / to_destination) to apply (default: empty list).

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: iptables, iptables_dnat_rules: {"dport": 22022, "to_destination": "10.0.1.186:22"} }

License
-------

BSD
