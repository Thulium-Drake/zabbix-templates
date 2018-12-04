# Zabbix Mailflow monitoring

This template can be used on any Zabbix agent running on a Linux system. The
template aims to give insight in the performance of the incoming mailflow.

This template requires at least Zabbix version 4.0.

The template collects:
* Average delays for each relay
* Amount of messages that went missing

Based on the collected information, the following triggers are configured:

* Incoming messages not delivered (with either extreme delay or lost in transit)

For more information see:
[zabbix_mailflow](ZABBIX_MAILFLOW.md)
