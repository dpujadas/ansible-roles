mms-agent
=========

This role installs and configures [MMS Automation Agent](https://docs.mms.mongodb.com/tutorial/nav/automation-agent/).

Role Variables
--------------

* **mms_agent_user:** MMS user (default: 'mongodb')
* **mms_agent_group:** MMS group`(default: mms_agent_user)
* **mms_agent_data_dir:** Mongodb data dir (default: '/data')
* **mms_agent_group_id:** MMS Group ID, can be found at https://mms.mongodb.com/settings
* **mms_agent_api_key:** MMS api key, can be found at https://mms.mongodb.com/settings

Example Playbook
----------------

    - hosts: servers
      roles:
         - {
            role: mms-agent,
            mms_agent_group_id: '{{ mms_group_id }}',
            mms_agent_api_key: '{{ mms_api_key }}'
         }

License
-------

BSD
