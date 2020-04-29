# Zabbix Tape performance monitoring

This template can be used on any Zabbix agent running on a Linux system. The
template aims to give insight in the performance of connected SCSI tape drives

This template requires at least Zabbix version 3.4.

The template collects:
* Bytes written to the device
* Bytes read from the device

Based on the collected information, the following graph is made:

* Throughput from and to the device

For more information see:
[zabbix_tapestats](ZABBIX_TAPESTATS.md)
