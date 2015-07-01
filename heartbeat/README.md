heartbeat
=========

This role installs and configures [heartbeat](http://www.linux-ha.org/wiki/Heartbeat).

Role Variables
--------------

* **heartbeat_partner_ip:** Other server's IP address to send heart beats (Ex: '10.0.0.10')
* **heartbeat_auto_failback:** Determines whether a resource will automatically fail back to its 'primary' node (default: 'off')
* **heartbeat_nodes:** List of cluster nodes, first element is considered the 'primary' node (see example playbook)
* **heartbeat_authkey:** Hash for securing info (Ex: '1dbf31f3466409b08fa27f6a32dbed14')
* **heartbeat_resources:** List of resources managed by heartbeat (see example playbook)
* **heartbeat_custom_resources:** List of custom resources to install (default: empty list)

Dependencies
------------

*dpujadas/awscli (if ElasticIP custom resource is installed, in order to manage AWS credentials)

Example Playbook
----------------

    - hosts: servers
      vars:
        custom_resources:
          - ElasticIP
        nodes:
          - 'server1'
          - 'server2'
        resources:
          - 'ElasticIP::eipalloc-37317a51::10.0.0.17'
      roles:
        - { role: heartbeat,
            heartbeat_authkey: '2efj934nf9q34fq',
            heartbeat_custom_resources: '{{ custom_resources }}',
            heartbeat_partner_ip: '10.0.1.10',
            heartbeat_nodes: '{{ nodes }}',
            heartbeat_resources: '{{ resources }}'
        }


License
-------

BSD
