#! /usr/bin/env python3

"""
Generates an SSH config file from the host information file located at
`~/notes/hosts.txt`. The hosts file was manually curated, using both the CIMS
website and inspection of each host's resources. If more hosts are added to the
hosts file, then this script should be run again.
"""

import os
from os import path
import argparse
import re

config_header = \
"""\
# XXX: This config file was automatically generated using
# ~/scripts/make_ssh_config.py. To make changes, edit the script and regenerate
# this file; don't edit this file manually.

Host *
	ServerAliveCountMax 4
	ServerAliveInterval 15
"""

host_template = \
"""\
Host {0}
	HostName {0}
	Port 22
	User ar2922
	IdentityFile ~/security/aditya.cims
"""

hosts_info_path = "/home/ar2922/notes/hosts.txt"

def open_if_exists(parser, arg):
	if path.exists(arg):
		parser.error("The file {0} already exists.".format(arg))
	else:
		return open(arg, 'w', encoding='utf-8')

parser = argparse.ArgumentParser(description="Generates SSH config from host information.")
parser.add_argument('--output', type=lambda x: open_if_exists(parser, x),
	help="Path to the output file.", required=True)
args = parser.parse_args()

hosts = []
host_pat = re.compile(r'^([a-z]+\d*)')

for line in open(hosts_info_path).readlines():
	match = host_pat.match(line)
	if match:
		hosts.append(match.groups()[0])

args.output.write(config_header)
args.output.write('\n')

for i, host in enumerate(hosts):
	args.output.write(host_template.format(host))
	if i != len(hosts) - 1:
		args.output.write('\n')
