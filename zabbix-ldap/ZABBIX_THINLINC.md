# NAME

zabbix_ldap - retrieve ldap information for zabbix.

# SYNOPSIS

`zabbix_ldap [option]`

# DESCRIPTION

This command supports the use of the included template in zabbix.

# INSTALLATION

In order for the command to be useful to zabbix, a number of installation steps
need to be done.

## AGENT CONFIGURATION

### ZABBIX_LDAP INSTALLATION

The command need to be installed on one or more zabbix agents. The default location
referenced in all files in this repository is:

`/usr/local/bin/zabbix_ldap`

In order for this command to work, the following software needs to be available:

* awk
* ldapwhoami (ldap-utils)

### ZABBIX_LDAP CONFIGURATION

There is one configuration file for this command

#### LDAP CONFIGURATION

The script requires credentials and a (list of) server(s) to check.

The configuration file is located at:

`/etc/zabbix/zabbix-ldap.conf`

The file contains three variables named LDAP_HOSTS, BIND_DN and BIND_PW which will specify how
the required data can be obtained.

In the sample file in this repository are a some examples for a few situations.

#### RUNNING

It is best to run the command from cron. The user running the command needs enough
privileges to run the ldapwhoami command.

In order to create statistics the command need to be run with the getdata option:

`/usr/local/bin/zabbix_ldap getdata`

The output of the command will be stored in:

`/tmp/zabbix-ldap`

A useful crontab entry would be:

`* * * * * /usr/local/bin/zabbix_ldap getdata`

### CONFIGURING ZABBIX AGENT

Now that the information is being gathered, the zabbix agent needs to be made aware
of how the information can be retrieved. A configuration file is available in the
repository and should be installed at:

`/etc/zabbix/zabbix_agentd.d/zabbix_agent-ldap.conf`

After the configuration has been added, reload the agent

`systemctl restart zabbix-agent`

## SERVER CONFIGURATION

The final step should be taken server side. In order to monitor the data a new
template needs to be imported.

* Open the zabbix webinterface
* Go to Configuration -> Templates
* Choose Import
* Choose browse and select the `template-ldap.xml` file in the file browser.
* Make any require changes to rules
* Select Import

The template is now available. In order to configure it for a host with a zabbix
agent that has been configuratie with the command follow the steps below.

* Open the zabbix webinterface
* Go to Configuration -> Hosts
* Select the name of the host to configure
* Go to templates
* Choose Template App LDAP at the Link new templates box
* Choose Add
* Choose Update

Zabbix should now start collecting data.

# FILES

`/usr/local/bin/zabbix_ldap` Command
`/etc/zabbix/zabbix-ldap.conf` LDAP configuration
`/etc/zabbix/zabbix-agentd.d/zabbix_agent-ldap.conf` Agent configuration file

# AUTHOR

Written by Jeffrey van Pelt

# REPORTING BUGS

Preferably by opening an issue on the github page.

# COPYRIGHT

Copyright  ©  2014  Free Software Foundation, Inc.  License GPLv3+: GNU
GPL version 3 or later <http://gnu.org/licenses/gpl.html>.
This is free software: you are free  to  change  and  redistribute  it.
There is NO WARRANTY, to the extent permitted by law.
