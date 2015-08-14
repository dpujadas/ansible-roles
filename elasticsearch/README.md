elasticsearch
=============

This role installs and configures [elasticsearch](https://www.elastic.co/products/elasticsearch).

Role Variables
--------------

* **elasticsearch_node_name:** Node name (default: inventory_hostname)
* **elasticsearch_cluster_name:** ElasticSearch cluster name (Ex: 'UniqueClusterName')
* **elasticsearch_major_version:** ElasticSearch major version to install (default: '1.7')
* **elasticsearch_default_options:** List of ini directives (section / option / value) for elasticsearch defaults file (default: empty list)
* **elasticsearch_install_plugins:** List of plugins (name / path) to install (default: empty list)
* **elasticsearch_plugin_aws_access_key:** ACCESS_KEY_ID with privileges to perform EC2 discovery actions, mandatory when installing aws-cloud plugin
* **elasticsearch_plugin_aws_secret_key:** SECRET_ACCESS_KEY with privileges to perform EC2 discovery actions, mandatory when installing aws-cloud plugin
* **elasticsearch_plugin_aws_region:** AWS region, mandatory when installing aws-cloud plugin (Ex: us-east-1)
* **elasticsearch_plugin_aws_tags:** List of tags to filter EC2 discovery

Example Playbook
----------------

    - hosts: servers
      vars:
        elasticsearch_plugins:
          - name: 'cloud-aws'
            path: 'elasticsearch/elasticsearch-cloud-aws/2.7.0'
        plugin_aws_tags:
          - stage: 'prod'
      roles:
        - {
          role: elasticsearch,
          elasticsearch_cluster_name: 'UniqueClusterName',
          elasticsearch_install_plugins: '{{ elasticsearch_plugins }}',
          elasticsearch_plugin_aws_access_key: '{{ aws_access_key_id }}',
          elasticsearch_plugin_aws_secret_key: '{{ aws_secret_access_key }}',
          elasticsearch_plugin_aws_region: '{{ aws_region }}',
          elasticsearch_plugin_aws_tags: '{{ plugin_aws_tags }}'
        }

License
-------

BSD

