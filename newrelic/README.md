newrelic
========

This role installs NewRelic daemon and agents (currently only php).

Role Variables
--------------

* **newrelic_agent_type:** NewRelic agent to install (Ex: 'php')
* **newrelic_license_key:** NewRelic license key (Ex: 'aowlrefn9cwoe8h')
* **newrelic_php_notify:** Handler that will be notified when php agent config file changes (Ex: 'restart php-fpm')
* **newrelic_options:** List of ini directives (section / option / value) for daemon config file (default: empty list)
* **newrelic_php_options:** List of ini directives (section / option / value) for php agent config file (default: empty list)

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
