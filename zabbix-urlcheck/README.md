# Zabbix URL monitoring

This template can be used on any Zabbix agent running on a Linux system. The
template aims to give insight in availability of configured URLs.

This template requires at least Zabbix version 5.0.

The template collects:
* Return code of the configured URL

Based on the collected information, the following trigger is made:

* URL connection failed

For more information see:
[zabbix_urlcheck](ZABBIX_URLCHECK.md)
