# NAME

zabbix_mailflow - manage mailflow information for zabbix.

# SYNOPSIS

`zabbix_mailflow [option]`

# DESCRIPTION

This command support the use of the included template in zabbix.

# INSTALLATION

In order for the command to be useful to zabbix, a number of installation steps
need to be done.

## AGENT CONFIGURATION

### ZABBIX_MAILFLOW INSTALLATION

The command needs to be installed on one or more zabbix agents. The default location
referenced in all files in this repository is:

`/usr/local/bin/zabbix_mailflow`

In order for this command to work, the following software needs to be available:

* jo
* awk
* ssh
* fetchmail

This command also requires 'zabbix_mailflow_getheader.awk' to be installed in the
default location:

`/etc/zabbix/zabbix_mailflow_getheader.awk`

### ZABBIX_MAILFLOW CONFIGURATION

There is one configuration file for this command.

#### MAILFLOW CONFIGURATION

The configuration file contains all the required variables to setup the mailflow monitoring:

* Relays in the mailflow
* Email address to use
* Amount of relays to monitor

The configuration file is located at:

`/etc/zabbix/zabbix-mailflow.conf`

Please follow the instructions in this file.

#### RUNNING

This command has 2 modes that need some setup:

* Sending out monitor emails
* Processing incoming monitor emails

##### SENDING MONITOR MAILS

It is best to run the command from cron. The user running the command needs enough
privileges to read the configuration file and an SSH key to a remote host.

In order to send a monitor mail the command needs to be run with the send_mail option:

`/usr/local/bin/zabbix_mailflow send_mail`

The command will not produce output, but will send a message to the configured recipient.

A useful crontab entry would be:

`* * * * * /usr/local/bin/zabbix_mailflow send_mail`

##### PROCESSING INCOMING MONITOR MAILS

It is recommended to use Fetchmail to process the incoming monitor emails. In order to do so
place the following configuration in ~zabbix/.fetchmailrc

```
set logfile /var/lib/zabbix/fetchmail.log
set no bouncemail

poll mail.example.com protocol imap username "zabbix" password "z@bb1x1saw3$som3" mda "/usr/local/bin/zabbix_mailflow process_mail"
```

The command will automatically retrieve any messages when the Zabbix agent retrieves statistics.

### CONFIGURING ZABBIX AGENT

Now that the information is being gathered, the zabbix agent needs to be made aware
of how the information can be retrieved. A configuration file is available in the
repository and should be installed at:

`/etc/zabbix/zabbix_agentd.d/zabbix_agent-mailflow.conf`

After the configuration has been added, reload the agent

`systemctl restart zabbix-agent`

## SERVER CONFIGURATION

The final step should be taken server side. In order to monitor the data a new
template needs to be imported.

* Open the zabbix webinterface
* Go to Configuration -> Templates
* Choose Import
* Choose browse and select the `template-mailflow.xml` file in the file browser.
* Make any require changes to rules
* Select Import

The template is now available. In order to configure it for a host with a zabbix
agent that has been configuratie with the command follow the steps below.

* Open the zabbix webinterface
* Go to Configuration -> Hosts
* Select the name of the host to configure
* Go to templates
* Choose Template Mailflow at the Link new templates box
* Choose Add
* Choose Update

Zabbix should now start collecting data.

# FILES

`/usr/local/bin/zabbix_mailflow` Command
`/etc/zabbix/zabbix-mailflow.conf` Mailflow configuration
`/etc/zabbix/zabbix_mailflow_getheader.awk` AWK-script
`/etc/zabbix/zabbix-agentd.d/zabbix_agent-mailflow.conf` Agent configuration file

# EXAMPLES

Check the output for discovery of mail relays:

`/usr/local/bin/zabbix_mailflow mailflow.discover`

# AUTHOR

Written by Jeffrey van Pelt

# REPORTING BUGS

Preferably by opening an issue on the github page.

# COPYRIGHT

Copyright  ©  2014  Free Software Foundation, Inc.  License GPLv3+: GNU
GPL version 3 or later <http://gnu.org/licenses/gpl.html>.
This is free software: you are free  to  change  and  redistribute  it.
There is NO WARRANTY, to the extent permitted by law.
