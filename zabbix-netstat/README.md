# Zabbix netstat monitoring

This template can be used on any Zabbix agent running on a Linux system. The
template aims to give insight in the performance of connected network interfaces.

This template requires at least Zabbix version 3.4.

The template collects:
* Transmit statistics
* Receive statistics

Based on the collected information, the following graphs are made:

* Transmit statistics
* Recieve statistics

And the following triggers are available:

* Rate of $i is not 0
** Errors
** Drops
** Fifo (Overflows)
** Framing
** Collisions
** Carrier losses

For more information see:
[zabbix_netstat](ZABBIX_NETSTAT.md)
