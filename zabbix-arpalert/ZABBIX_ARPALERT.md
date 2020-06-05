# NAME

zabbix_arpalert - report arpalerts' notifications to zabbix.

# SYNOPSIS

`zabbix_arpalert [option]`

# DESCRIPTION

This command supports the use of the included template in zabbix.

# INSTALLATION

In order for the command to be useful to zabbix, a number of installation steps
need to be done.

## AGENT CONFIGURATION

### ZABBIX_ARPALERT INSTALLATION

The command needs to be installed on one or more zabbix agents. The default location
referenced in all files in this repository is:

`/usr/local/bin/zabbix_arpalert`

In order for this command to work, the following software needs to be available:

* arpalert
* zabbix_sender

### ZABBIX_ARPALERT CONFIGURATION

This command is meant to be used by arpalert as it's action script. In order to use
it, you need to configure the following in /etc/arpalert/arpalert.conf:

* interface = [comma separated list of interfaces arpalert should monitor]
* action on detect = /usr/local/bin/zabbix_arpalert

The command also requires the following configuration file:

`/etc/zabbix/zabbix-arpalert.conf`

It should contain the variable ZABBIXSRV with the full name of the zabbix server
used by zabbix_sender.

#### RUNNING

This command is not meant for local execution outside arpalert.

## SERVER CONFIGURATION

The final step should be taken server side. In order to monitor the data a new
template needs to be imported.

* Open the zabbix webinterface
* Go to Configuration -> Templates
* Choose Import
* Choose browse and select the `template-arpalert.xml` file in the file browser.
* Make any require changes to rules
* Select Import

The template is now available. In order to configure it for a host with a zabbix
agent that has been configuratie with the command follow the steps below.

* Open the zabbix webinterface
* Go to Configuration -> Hosts
* Select the name of the host to configure
* Go to templates
* Choose Template App Arpalert at the Link new templates box
* Choose Add
* Choose Update

Zabbix should now start collecting data.

# FILES

`/usr/local/bin/zabbix_arpalert` Command
`/etc/zabbix/zabbix-arpalert.conf` Command configuration file

# AUTHOR

Written by Jeffrey van Pelt

# REPORTING BUGS

Preferably by opening an issue on the github page.

# COPYRIGHT

Copyright  ©  2014  Free Software Foundation, Inc.  License GPLv3+: GNU
GPL version 3 or later <http://gnu.org/licenses/gpl.html>.
This is free software: you are free  to  change  and  redistribute  it.
There is NO WARRANTY, to the extent permitted by law.
