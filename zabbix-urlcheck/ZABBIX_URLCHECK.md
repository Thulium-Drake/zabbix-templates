# NAME

zabbix_urlcheck - url connectivity checks for zabbix.

# SYNOPSIS

`zabbix_urlcheck [option]`

# DESCRIPTION

This command support the use of the included template in zabbix.

# INSTALLATION

In order for the command to be useful to zabbix, a number of installation steps
need to be done.

## AGENT CONFIGURATION

### ZABBIX_URLCHECK INSTALLATION

The command needs to be installed on one or more zabbix agents. The default location
referenced in all files in this repository is:

`/usr/local/bin/zabbix_urlcheck`

In order for this command to work, the following software needs to be available:

* curl
* awk
* jo
* sed

### ZABBIX_URLCHECK CONFIGURATION

There is one configuration file for this command.

#### URLCHECK CONFIGURATION

The certificates that the zabbix agent should monitor have to be defined.

The configuration file is located at:

`/etc/zabbix/zabbix-urlcheck.conf`

The file contains one line for each certificate:

hostname[,proxy proxy2]

#### RUNNING

It is best to run the command from cron. The user running the command needs enough
privileges to read the configuration file.

In order to create statistics the command needs to be run with the getdata option:

`/usr/local/bin/zabbix_urlcheck getdata`

The output data of the command will be stored in:

`/tmp/zabbix-urlcheck`

A useful crontab entry would be:

`* * * * * /usr/local/bin/zabbix_urlcheck getdata`

### CONFIGURING ZABBIX AGENT

Now that the information is being gathered, the zabbix agent needs to be made aware
of how the information can be retrieved. A configuration file is available in the
repository and should be installed at:

`/etc/zabbix/zabbix_agentd.d/zabbix_agent-urlcheck.conf`

After the configuration has been added, reload the agent

`systemctl restart zabbix-agent`

## SERVER CONFIGURATION

The final step should be taken server side. In order to monitor the data a new
template needs to be imported.

* Open the zabbix webinterface
* Go to Configuration -> Templates
* Choose Import
* Choose browse and select the `template-urlcheck.xml` file in the file browser.
* Make any require changes to rules
* Select Import

The template is now available. In order to configure it for a host with a zabbix
agent that has been configuratie with the command follow the steps below.

* Open the zabbix webinterface
* Go to Configuration -> Hosts
* Select the name of the host to configure
* Go to templates
* Choose Template URL Monitoring at the Link new templates box
* Choose Add
* Choose Update

Zabbix should now start collecting data.

# FILES

`/usr/local/bin/zabbix_urlcheck` Command
`/etc/zabbix/zabbix-urlcheck.conf` URLs to check
`/etc/zabbix/zabbix-agentd.d/zabbix_agent-urlcheck.conf` Agent configuration file

# EXAMPLES

Check the output for discovery of certificates:

`/usr/local/bin/zabbix_urlcheck urlcheck.discover`

# AUTHOR

Written by Jeffrey van Pelt

# REPORTING BUGS

Preferably by opening an issue on the github page.

# COPYRIGHT

Copyright  ©  2014  Free Software Foundation, Inc.  License GPLv3+: GNU
GPL version 3 or later <http://gnu.org/licenses/gpl.html>.
This is free software: you are free  to  change  and  redistribute  it.
There is NO WARRANTY, to the extent permitted by law.
