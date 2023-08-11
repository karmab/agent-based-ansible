#!/usr/bin/env python3

from redfish import Redfish
import sys
import yaml
import socket

inventory = sys.argv[1] if len(sys.argv) > 1 else 'inventory'
nodes = int(sys.argv[2]) if len(sys.argv) > 2 else 3
with open(inventory) as f:
    data = yaml.safe_load(f)['all']['vars']

iso_url = data.get('iso_url')
if not iso_url:
    ipaddr = socket.gethostbyname(socket.gethostname())
    iso_url = f"http://{ipaddr}/agent.x86_64.iso"

hosts = data['hosts']
for index, host in enumerate(hosts):
    if index >= nodes:
        break
    bmc_url = host.get('bmc_url')
    bmc_user = host.get('bmc_user')
    bmc_password = host.get('bmc_password')
    if bmc_url is not None:
        red = Redfish(bmc_url, bmc_user, bmc_password)
        red.set_iso(iso_url)
