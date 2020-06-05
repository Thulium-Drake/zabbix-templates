# Zabbix ARP alert trapper

This template can be used on any Zabbix agent running on a Linux system. The
template aims to detect duplicate IPs with arpalert.

This template requires at least Zabbix version 5.0.

The template collects:
* Alerts as sent by arpalert, currently only the following types:
  * Type 9: MAC change

Please note that this can generate false positives if you have certain bonding
configurations. Please add the known bonding MAC addresses to /etc/arpalert/maclist.allow.

Based on the collected information, the following trigger is made:

* Duplicate IP detected

For more information see:
[zabbix_arpalert](ZABBIX_ARPALERT.md)
