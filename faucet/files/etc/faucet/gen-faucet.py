import os
from jinja2 import Template 

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

vlan_list = [ {"name": k, "vid": v} for k,v in VLANS.items() ]
vlan_list = sorted(vlan_list, key=lambda x: x["vid"])
port_list = [{"name": "port1.0.%d" % i, "number": i} for i in range(3,51)]


with open(INPUT_FILENAME) as f:
    template = Template(f.read())

print template.render(
    vlans=vlan_list,
    tagged_vlan_vids=[x["vid"] for x in vlan_list],
    ports=port_list)

