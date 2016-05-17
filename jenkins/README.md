jenkins
=======

This role installs and configures [Jenkins](https://jenkins-ci.org/).

Role Variables
--------------

- `jenkins_user`: User that will run jenkins (default: '$NAME')
- `jenkins_group`: Group that will run jenkins (default: '$NAME')
- `jenkins_home`: Jenkins' home dir (default: '/var/lib/$NAME')

Example Playbook
----------------

    - hosts: servers
      roles:
        - {
          role: jenkins
        }

License
-------

BSD
