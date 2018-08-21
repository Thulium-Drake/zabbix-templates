# Zabbix disk I/O monitoring

This template can be used on any Zabbix agent running on a Linux system. The
template aims to give insight in the performance of connected disk devices.

This template requires at least Zabbix version 3.4.

The template collects:
* Bytes written to the device
* Bytes read from the device
* Reads completed
* Writes completed

Based on the collected information, the following graph is made:

* Throughput from and to the device
* IOPS from and to the device

For more information see:
[zabbix_diskstats](ZABBIX_DISKSTATS.md)
