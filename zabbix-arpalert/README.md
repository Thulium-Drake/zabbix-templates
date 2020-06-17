# Zabbix ARP alert

This template can be used on a Zabbix server running on a Linux system. The
template aims to detect duplicate IP addresses using ARPalert.

This template requires at least Zabbix version 5.0.

The template collects:
* MAC addresses of conflicting IPs

Based on the collected information, the following trigger is created:

* Duplicate IP detected - {MESSAGE}

Due to the nature of how Zabbix handles problems created by triggers, you will
receive multiple problems per detected duplicate IP. This template tries to limit
the amount of incoming problems with a configurable cooldown on re-sending the message.

For more information see:
[zabbix_arpalert](ZABBIX_ARPALERT.md)
