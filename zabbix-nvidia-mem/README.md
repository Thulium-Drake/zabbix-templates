# Zabbix Nvidia GPU Memory usage monitoring

This template can be used on any Zabbix agent running on a Linux system. The
template aims to give insight in the utilization of the GPU memory of a Nvidia
card in the system.

This template requires at least Zabbix version 4.4.

The template collects:
* Memory usage of all the Nvidia GPU's in the system

Based on the collected information, the following trigger is made:

* GPU memory low

For more information see:
[zabbix_nvidia-mem](ZABBIX_NVIDIA_MEM.md)
