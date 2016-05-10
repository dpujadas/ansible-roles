cloudwatch-put
==============

Send some linux metrics to AWS CloudWatch. Based on [aws-mon-linux](https://github.com/moomindani/aws-mon-linux)

Requirements
------------

Awscli must be properly configured with, at least, grants for cloudwatch:PutMetricData and ec2:DescribeInstances.

Role Variables
--------------

- `cloudwatch_put_path`: Path to install the script (default: '/opt')
- `cloudwatch_put_set_cron`: Set a cron to send metrics every minute (default: False)
- `cloudwatch_put_aws_bin`: Path to aws bin (default: '/usr/local/bin/aws')
- `cloudwatch_put_opts`: Options passed to script. See script doc for all available options (default: '')

Example Playbook
----------------

    - hosts: servers
      roles:
        - { 
            role: cloudwatch-put,
            cloudwatch_put_set_cron: True,
            cloudwatch_put_opts: '--load-ave1'
        }

License
-------

BSD
