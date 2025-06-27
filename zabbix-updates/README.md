# Zabbix OS update tracking

This template can be used on any Zabbix agent running on any Linux system. This template gives insight in the updates the system still needs to install from the repo. It currently supports the APT and DNF package managers

This template requires at least Zabbix version 7.0.

The template collects:
* OS Upgradable Packages
* OS Upgrade Count

There is one trigger present, this will notify you when a system needs updates.
