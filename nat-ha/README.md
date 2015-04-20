nat-ha
======

This role provides [High Availability for Amazon VPC NAT Instances](http://aws.amazon.com/articles/2781451301784570).

Requirements
------------

This role requires:
* curl
* AWS CLI installed and properly configured with a user that has, at least, the following privileges:
    * ec2:DescribeInstances
    * ec2:CreateRoute
    * ec2:ReplaceRoute
    * ec2:StartInstances
    * ec2:StopInstances

Role Variables
--------------

* **nat_ha_aws_bin:** AWS CLI binary (default: '/usr/local/bin/aws')
* **nat_ha_script_path:** Path to create daemon script (default: '/usr/local/bin')
* **nat_ha_num_pings:** The number of times the health check will ping NAT instance. NAT instance will only be considered unhealthy if all pings fail (default: '5')
* **nat_ha_ping_timeout:** The number of seconds to wait for each ping response before determining that the ping has failed (default: '1')
* **nat_ha_wait_between_pings:** The number of seconds to wait between health checks (default: '30')
* **nat_ha_wait_for_instance_stop:** The number of seconds to wait for NAT instance to stop before attempting to stop it again (if it hasn't stopped already) (default: '60')
* **nat_ha_wait_for_instance_start:** The number of seconds to wait for NAT Node #2 to restart before resuming health checks again (default:'300')
* **nat_ha_nat_id:** AWS Instace ID to check.
* **nat_ha_nat_rt_id:**  The ID of the route table routing Internet-bound traffic through the NAT instance that this script will be monitoring.
* **nat_ha_my_rt_id:** The ID of the route table routing Internet-bound traffic through the current instance.

Example Playbook
----------------

    - hosts: servers
      roles:
         - {
            role: nat-ha,
            nat_ha_nat_id: '{{ nat_instance_id }}',
            nat_ha_nat_rt_id: '{{ nat_rt_id }}',
            nat_ha_my_rt_id: '{{ my_rt_id }}'
          }

License
-------

BSD
