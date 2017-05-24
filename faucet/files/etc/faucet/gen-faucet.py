import os
from jinja2 import Template 

FIRST_SDN_PORT = 3
LAST_SDN_PORT = 42

VLANS = {
    "Sysadmin": 2,
    "VoIP": 3,
    "Office": 4,
    "Guests": 7,
    "IPv6 only": 20,
    "TOMBS managment network": 983,
    "TOMBS VM network": 984,
}

INPUT_FILENAME = os.path.join(os.path.dirname(__file__), "faucet.yml.tpl")

def _vlan_label(s): return s.lower().replace(" ", "-")

vlan_list = [ {
    "label": _vlan_label(k),
    "name": k,
    "vid": v} for k,v in VLANS.items() ]
vlan_list = sorted(vlan_list, key=lambda x: x["vid"])
port_list = [{
    "name": "port1.0.%d" % i,
    "number": i,
    "vlan": "office"} for i in range(FIRST_SDN_PORT, LAST_SDN_PORT+1)]


with open(INPUT_FILENAME) as f:
    template = Template(f.read())

print template.render(
    vlans=vlan_list,
    tagged_vlan_vids=[x["label"] for x in vlan_list],
    ports=port_list)

