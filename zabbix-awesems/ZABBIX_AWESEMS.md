# NAME

zabbix_awesems - retrieve total energy consumed by EV from Awesems API.

# SYNOPSIS

`zabbix_awesems [option]`

# DESCRIPTION

This command support the use of the included template in zabbix.

# INSTALLATION

In order for the command to be useful to zabbix, a number of installation steps
need to be done.

## AGENT CONFIGURATION

### ZABBIX_AWESEMS INSTALLATION

The command needs to be installed on one or more zabbix agents. The default location
referenced in all files in this repository is:

`/usr/local/bin/zabbix_awesems`

### ZABBIX_AWESEMS CONFIGURATION

There is one configuration file for this command.

#### AWESEMS CONFIGURATION

The credentials for retrieving information from the Awesems API have to be defined.

The configuration file is located at:

`/etc/zabbix/zabbix-awesems.conf`

The file should contain the following variables:

  AWS_IDP_URL - The URL for the AWS authentication endpoint
  AWESEMS_CONFIG_API - The URL which reports which GraphQL endpoint is used by the data API
  AWESEMS_EMAIL - The email the user uses to sign in on the Awesems Portal
  AWESEMS_PASSWORD - The password for the email defined above
  AWESEMS_CLIENT_ID - The application ID for the Awesems API within AWS

#### RUNNING

It is best to run the command from cron. The user running the command needs enough
privileges to read the configuration file.

In order to create statistics the command needs to be run with the getdata option:

`/usr/local/bin/zabbix_awesems getdata`

The output data of the command will be stored in:

`/tmp/zabbix-awesems`

A useful crontab entry would be:

`0 * * * * /usr/local/bin/zabbix_awesems getdata`

### CONFIGURING ZABBIX AGENT

Now that the information is being gathered, the zabbix agent needs to be made aware
of how the information can be retrieved. A configuration file is available in the
repository and should be installed at:

`/etc/zabbix/zabbix_agentd.d/zabbix_agent-awesems.conf`

After the configuration has been added, reload the agent

`systemctl restart zabbix-agent`

## SERVER CONFIGURATION

The final step should be taken server side. In order to monitor the data a new
template needs to be imported.

* Open the zabbix webinterface
* Go to Configuration -> Templates
* Choose Import
* Choose browse and select the `template-awesems.xml` file in the file browser.
* Make any require changes to rules
* Select Import

The template is now available. In order to configure it for a host with a zabbix
agent that has been configuratie with the command follow the steps below.

* Open the zabbix webinterface
* Go to Configuration -> Hosts
* Select the name of the host to configure
* Go to templates
* Choose Template Awesems EVCharger at the Link new templates box
* Choose Add
* Choose Update

Zabbix should now start collecting data.

# FILES

`/usr/local/bin/zabbix_awesems` Command
`/etc/zabbix/zabbix-awesems.conf` Awesems API configuration
`/etc/zabbix/zabbix-agentd.d/zabbix_agent-awesems.conf` Agent configuration file

# AUTHOR

Written by Jeffrey van Pelt

# REPORTING BUGS

Preferably by opening an issue on the github page.

# COPYRIGHT

Copyright  ©  2014  Free Software Foundation, Inc.  License GPLv3+: GNU
GPL version 3 or later <http://gnu.org/licenses/gpl.html>.
This is free software: you are free  to  change  and  redistribute  it.
There is NO WARRANTY, to the extent permitted by law.
