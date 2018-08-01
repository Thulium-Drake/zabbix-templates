# Zabbix SSL Certificate expiration

This template can be used on any Zabbix agent running on a Linux system. The
template aims to give insight in the configured SSL certificates.

This template requires at least Zabbix version 3.4.

The template collects:
* Certificate fingerprint
* Remaining certificate validity

Based on the collected information, the following triggers are configured:

* Certificate expires in [30/15/5] days, with increasing priority
* Certificate has expired
* Fingerprint has changed

For more information see:
[zabbix_sslcert](ZABBIX_SSLCERT.md)
