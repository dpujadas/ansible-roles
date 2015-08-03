elasticsearch
=============

This role installs and configures [elasticsearch](https://www.elastic.co/products/elasticsearch).

Role Variables
--------------

* **elasticsearch_major_version:** ElasticSearch major version to install (default: '1.7')
* **elasticsearch_default_options:** List of ini directives (section / option / value) for elasticsearch defaults file (default: empty list)
* **elasticsearch_cluster_name:** ElasticSearch cluster name (Ex: 'UniqueClusterName')

Example Playbook
----------------

    - hosts: servers
      roles:
        - {
          role: elasticsearch,
          elasticsearch_cluster_name: 'UniqueClusterName'
        }

License
-------

BSD

