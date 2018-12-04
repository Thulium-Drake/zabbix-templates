# NAME

zabbix_catialic - retrieve catialic license usage information for zabbix.

# SYNOPSIS

`zabbix_catialic [option]`

# DESCRIPTION

This command supports the use of the included template in zabbix.

# INSTALLATION

In order for the command to be useful to zabbix, a number of installation steps
need to be done.

## AGENT CONFIGURATION

### ZABBIX_CATIALIC INSTALLATION

The command need to be installed on one or more zabbix agents. The default location
referenced in all files in this repository is:

`/usr/local/bin/zabbix_catialic`

In order for this command to work, the following software needs to be available:

* jo
* sed
* curl
* awk

The script requires the output of `zabbix-catialic.awk` for processing. The default location
for this script is:

`/etc/zabbix/zabbix-catialic.awk`

### ZABBIX_CATIALIC CONFIGURATION

There is one configuration file for this command.

#### CATIALIC CONFIGURATION

The configuration file is located at:

`/etc/zabbix/zabbix-catialic.conf`

This file contains one variable named LICENSE_URL which will specify for the awkscript where the output
can be obtained.

The output will be obtained by the following script:

`/usr/local/bin/zabbix_catialic getdata`

#### RUNNING

It is best to run the command from cron. The user running the command needs enough
privileges to read the configuration file.

In order to create statistics the command needs to be run with the getdata option:

`/usr/local/bin/zabbix_catialic getdata`

The output of the command will be stored in:

`/tmp/zabbix-catialic`

A useful crontab entry would be:

`* * * * * /usr/local/bin/zabbix_catialic getdata`

### CONFIGURING ZABBIX AGENT

Now that the information is being gathered, the zabbix agent needs to be made aware
of how the information can be retrieved. A configuration file is available in the
repository and should be installed at:

`/etc/zabbix/zabbix_agentd.d/zabbix_agent-catialic.conf`

After the configuration has been added, reload the agent

`systemctl restart zabbix-agent`

## SERVER CONFIGURATION

The final step should be taken server side. In order to monitor the data a new
template needs to be imported.

* Open the zabbix webinterface
* Go to Configuration -> Templates
* Choose Import
* Choose browse and select the `template-catialic.xml` file in the file browser.
* Make any require changes to rules
* Select Import

The template is now available. In order to configure it for a host with a zabbix
agent that has been configuratie with the command follow the steps below.

* Open the zabbix webinterface
* Go to Configuration -> Hosts
* Select the name of the host to configure
* Go to templates
* Choose Template App CATIA at the Link new templates box
* Choose Add
* Choose Update

Zabbix should now start collecting data.

# FILES

`/usr/local/bin/zabbix_catialic` Command
`/etc/zabbix/zabbix-catialic.conf` CATIA configuration
`/etc/zabbix/zabbix-agentd.d/zabbix_agent-catialic.conf` Agent configuration file
`etc/zabbix/zabbix-catialic.awk` AWK-script

# EXAMPLES

Check the output for discovery of licenses:

`/usr/local/bin/zabbix_catialic catialic.discover`

# AUTHOR

Written by Floor van der Sluis

# REPORTING BUGS

Preferably by opening an issue on the github page.

# COPYRIGHT

Copyright  ©  2014  Free Software Foundation, Inc.  License GPLv3+: GNU
GPL version 3 or later <http://gnu.org/licenses/gpl.html>.
This is free software: you are free  to  change  and  redistribute  it.
There is NO WARRANTY, to the extent permitted by law.
