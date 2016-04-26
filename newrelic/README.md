newrelic
========

This role installs NewRelic daemon, sysmond (optionally) and agents (currently only php).

Role Variables
--------------

* **newrelic_license_key:** NewRelic license key (Ex: 'aowlrefn9cwoe8h')
* **newrelic_agent_type:** NewRelic agent to install. When set, role installs newrelic_daemon, too. (Ex: 'php')
* **newrelic_options:** List of ini directives (section / option / value) for daemon config file (default: empty list)
* **newrelic_enabled:** Enable newrelic daemon at boot or not (default: 'yes')
* **newrelic_state:** Newrelic daemon state (default: 'started')
* **newrelic_php_notify:** List of handlers that will be notified when php agent config file changes (default: empty list)
* **newrelic_php_options:** List of ini directives (section / option / value) for php agent config file (default: empty list)
* **newrelic_sysmond_install:** Install newrelic_sysmond or not (default: false)
* **newrelic_sysmond_loglevel:** Sysmond's log level (default: 'info')
* **newrelic_sysmond_logfile:** Sysmond's log file (default: '/var/log/newrelic/nrsysmond.log')

Example Playbook
----------------

    - hosts: servers
      roles:
        - {
            role: newrelic,
            newrelic_agent_type: 'php',
            newrelic_license_key: 'NewrelicLicenseKey }}',
            newrelic_php_notify: 'restart php-fpm'
        }

License
-------

BSD
