# NAME

zabbix_sensors - retrieve sensors in the system via lm-sensors

# SYNOPSIS

`zabbix_nvidia_mem`

# DESCRIPTION

This command support the use of the included template in zabbix.

# INSTALLATION

In order for the command to be useful to zabbix, a number of installation steps
need to be done.

## AGENT CONFIGURATION

### ZABBIX_SENSORS INSTALLATION

The command needs to be installed on one or more zabbix agents. The default location
referenced in all files in this repository is:

`/usr/local/bin/zabbix_sensors`

In order for this command to work, the following software needs to be available:

* cut
* grep
* lm-sensors
* tr

### ZABBIX_SENSORS CONFIGURATION

There is no configuration required for this command. The command will detect which
sensors are available with 'sensors' and gather statistics for all of them

### CONFIGURING ZABBIX AGENT

Now that the information is being gathered, the zabbix agent needs to be made aware
of how the information can be retrieved. A configuration file is available in the
repository and should be installed at:

`/etc/zabbix/zabbix_agentd.d/zabbix_agent-sensors.conf`

After the configuration has been added, reload the agent

`systemctl restart zabbix-agent`

## SERVER CONFIGURATION

The final step should be taken server side. In order to monitor the data a new
template needs to be imported.

* Open the zabbix webinterface
* Go to Configuration -> Templates
* Choose Import
* Choose browse and select the `template-sensors.yml` file in the file browser.
* Make any require changes to rules
* Select Import

The template is now available. In order to configure it for a host with a zabbix
agent that has been configuratie with the command follow the steps below.

* Open the zabbix webinterface
* Go to Configuration -> Hosts
* Select the name of the host to configure
* Go to templates
* Choose System Sensors by Zabbix agent (active) at the Link new templates box
* Choose Add
* Choose Update

Zabbix should now start collecting data.

# FILES

`/usr/local/bin/zabbix_sensors` Command
`/etc/zabbix/zabbix-agentd.d/zabbix_agent-sensors.conf` Agent configuration file

# EXAMPLES

Check the output for discovery of sensors:

`/usr/local/bin/zabbix_sensors`

# AUTHORS

Documentation written by Jeffrey van Pelt
Original template written by Ivan Bayan, edited by Jeffrey van Pelt
Script written by Ivan Bayan

# REPORTING BUGS

Preferably by opening an issue on the github page.

# COPYRIGHT

Copyright  ©  2014  Free Software Foundation, Inc.  License GPLv3+: GNU
GPL version 3 or later <http://gnu.org/licenses/gpl.html>.
This is free software: you are free  to  change  and  redistribute  it.
There is NO WARRANTY, to the extent permitted by law.
