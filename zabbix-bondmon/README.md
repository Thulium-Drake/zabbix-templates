# Zabbix Linux bond monitoring

This template can be used on any Zabbix agent running on a Linux system. The
template aims to give insight in the availability of configured bond interfaces

This template requires at least Zabbix version 3.4.

The template collects:
* All slave interfaces to existing bonds

Based on the collected information, the following trigger is made:

* Slave interface is down

For more information see:
[zabbix_bondmon](ZABBIX_BONDMON.md)
