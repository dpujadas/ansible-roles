ssmtp
=====

This role installs and configures ssmtp package, prepared to use with AWS SES.

Role Variables
--------------

* **ssmtp_root:** Default: postmaster
* **ssmtp_hostname:** Full qualified name of the host
* **ssmtp_server:** The host to send mail to
* **ssmtp_port:** The port to send mail to
* **ssmtp_user:** The user name to use for SMTP AUTH
* **ssmtp_pass:** The password to use for SMTP AUTH
* **ssmtp_rewrite_domain:** If set, the domain from which mail seems to come
* **ssmtp_from_line_override:** Specifies whether the From header of an email, if any, may override the default domain (default: Yes)
* **ssmtp_use_tls:** Specifies whether ssmtp uses TLS to talk to the SMTP server (default: Yes)
* **ssmtp_use_starttls:** Specifies whether ssmtp uses STARTTLS to talk to the SMTP server (default: No)

Example Playbook
----------------

    - hosts: servers
      roles:
        - { 
            role: ssmtp,
            ssmtp_hostname: '{{ inventory_hostname }}',
            ssmtp_server: '{{ aws_ses_server_name }}',
            ssmtp_port: '465',
            ssmtp_user: '{{ aws_ses_user }}',
            ssmtp_pass: '{{ aws_ses_pass }}' 
        }

License
-------

BSD
