# Zabbix OS end of life tracking

This template can be used on any Zabbix agent running on any RHEL system. This template gives insight in the end of life date for every system both for extended update support (EUS) and non EUS systems.

This template requires at least Zabbix version 7.0.

The template collects:
* OS Release
* OS Version
* Checks if "EUS" is present in the redhat repo file

There are four triggers present. Two for non EUS systems, one doing informational triggers at 360 days and the other doing a warning at 180 days. The same triggers are made for the EUS systems.