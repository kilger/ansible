ROLE SYSTEMD\_JOURNALD
======================

[![GitHub](https://img.shields.io/github/license/adfinis-sygroup/ansible-role-systemd_journald.svg?style=flat-square)](https://github.com/adfinis-sygroup/ansible-role-systemd_journald/blob/master/LICENSE)
[![Travis (.org)](https://img.shields.io/travis/adfinis-sygroup/ansible-role-systemd_journald.svg?style=flat-square)](https://travis-ci.org/adfinis-sygroup/ansible-role-systemd_journald)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-adfinis--sygroup.systemd_journald-660198.svg?style=flat-square)](https://galaxy.ansible.com/adfinis-sygroup/systemd_journald)

This Ansible role configures some aspects of systemd-journald, via
`/etc/systemd/journald.conf`.


Requirements
------------

Systemd 243 or higher, or

* On CentOS 7, `systemd-219-73.el_8.5` or higher.


Role Variables
--------------

The following default variables can be set:

```yaml
# Storage control (journald.conf(5), `Storage=` option)
# If empty, use journald default (`auto`):
systemd_journald_storage:
```


Dependencies
------------

*(none)*


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

```yaml
- hosts: servers
  roles:
    - adfinis-sygroup.systemd_journald
```


License
-------

[GPL-3.0](https://github.com/adfinis-sygroup/ansible-role-systemd_journald/blob/master/LICENSE)


Author Information
------------------

The `systemd_journald` role was written by:

* Adfinis AG | [Website](https://adfinis.com/) | [Twitter](https://twitter.com/adfinissygroup) | [GitHub](https://github.com/adfinis-sygroup)
