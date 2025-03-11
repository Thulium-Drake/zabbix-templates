#!/usr/bin/env python3
""" Import Zabbix templates and other exported files
This script reads its configuration from ~/.pyzabbix_conf.yml

=== 8< ===
zabbix:
   hostname: zabbix.example.com
   web_path: /zabbix
   sslverify: True
   username: Admin
   password: zabbix
=== 8< ===
"""

default_conf = {
    'hostname': None,
    'web_path': None,
    'sslverify': None,
    'username': None,
    'password': None,
    'api_token': None
    }
conf = {}

import os
import sys
import yaml
import logging
import glob
from argparse import ArgumentParser

try:
    from pyzabbix import ZabbixAPI, ZabbixAPIException
except ImportError:
    print ('ERROR: pyzabbix module not found! Exiting!')
    sys.exit(1)

try:
    c = os.path.expanduser('~') + '/.pyzabbix_conf.yml'
    with open(c, 'r') as conf_file:
        load_conf = yaml.safe_load(conf_file)
        conf = default_conf | load_conf['zabbix']
except FileNotFoundError:
    print ('ERROR: ' + c + ' not found! Exiting!')
    sys.exit(1)

# Parse commandline arguments
alltemplates = False
parser = ArgumentParser()
parser.add_argument("-t", help="Import the given template (or directory)", dest="import_path")
parser.add_argument("-v", help="Show the transactions made with the Zabbix API", action="store_true", dest="verbose")
args = parser.parse_args()

# debug if verbose
if args.verbose:
    stream = logging.StreamHandler(sys.stdout)
    stream.setLevel(logging.DEBUG)
    log = logging.getLogger('pyzabbix')
    log.addHandler(stream)
    log.setLevel(logging.DEBUG)

# Exit if the import_path is empty
if not args.import_path:
    print('No input given, please check help')
    sys.exit(1)

# Setup API connection
zapi = ZabbixAPI("https://"+conf['hostname']+conf['web_path']+"/api_jsonrpc.php")
zapi.session.verify = conf['sslverify']
zapi.timeout = 60.1

if (conf['username'] is None) and (conf['api_token'] is None):
    print('ERROR: No credentials found, please define username/password or api_token')

if conf['password'] is not None:
    zapi.login (conf['username'], conf['password'])

if conf['api_token'] is not None:
    zapi.login(api_token=conf['api_token'])

# Import rules
rules = {
    'discoveryRules': {
        'createMissing': True,
        'updateExisting': True,
	'deleteMissing': True
    },
    'graphs': {
        'createMissing': True,
        'updateExisting': True,
	'deleteMissing': True
    },
    'hosts': {
        'createMissing': True,
        'updateExisting': True
    },
    'images': {
        'createMissing': True,
        'updateExisting': True
    },
    'items': {
        'createMissing': True,
        'updateExisting': True,
	'deleteMissing': True
    },
    'maps': {
        'createMissing': True,
        'updateExisting': True
    },
    'templateLinkage': {
        'createMissing': True,
    },
    'templates': {
        'createMissing': True,
        'updateExisting': True
    },
    'triggers': {
        'createMissing': True,
        'updateExisting': True,
	'deleteMissing': True
    },
    'valueMaps': {
        'createMissing': True,
        'updateExisting': True
    },
}

# Find all files in the directory and parse them for import
if os.path.isdir(args.import_path):
    files = glob.glob(args.import_path + '/*')
    for file in files:
        print('Processing ' + file)
        with open(file, 'r') as f:
            if file.endswith('yaml'):
                f_format = 'yaml'
            elif file.endswith('yml'):
                f_format = 'yaml'
            elif file.endswith('xml'):
                f_format = 'xml'
            else:
                print('Skipping, could not detect supported file type')
                continue

            template = f.read()
            try:
                zapi.configuration['import'](format=f_format, source=template, rules=rules)
                print('Import successful!')
            except ZabbixAPIException as e:
                print(e)
# Or just parse the file and import that instead
elif os.path.isfile(args.import_path):
    files = glob.glob(args.import_path)
    for file in files:
        with open(file, 'r') as f:
            if file.endswith('yaml'):
                f_format = 'yaml'
            elif file.endswith('yml'):
                f_format = 'yaml'
            elif file.endswith('xml'):
                f_format = 'xml'
            else:
                print('Skipping, could not detect supported file type')
                continue

            template = f.read()
            try:
                zapi.configuration['import'](format=f_format, source=template, rules=rules)
                print('Import successful!')
            except ZabbixAPIException as e:
                print(e)
# Unless the file isn't usable at all
else:
    sys.exit('ERROR: Not a valid file')
