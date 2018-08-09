# Zabbix FlexLM license usage

This template can be used on any Zabbix agent running on a Linux system. The
template aims to give insight in the usage of FlexLM licenses.

This template requires at least Zabbix version 3.4.

The template collects (using discovery):
* The amount of licenses issued per feature
* The amount of licenses used per feature

Based on the collected information, the following graph is plotted:

* License usage per feature

For more information see:
[zabbix_flexlm](ZABBIX_FLEXLM.md)
