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

ports = {}
for i in range(FIRST_SDN_PORT, LAST_SDN_PORT+1):
    name = "port1.0.%d" % i
    ports[name] = {
        "number": i,
        "description": name,
        "name": name,
        "vlan": "office" }

panels = {
    "1": {
        "12": { "port": "port1.0.3" },
        "15": { "port": "port1.0.4", "vlan": "voip" },
        "2": { "port": "port1.0.5" },
        "11": { "port": "port1.0.6" },
        "17": { "port": "port1.0.7" },
        "18": { "port": "port1.0.8" },
        "19": { "port": "port1.0.9" },
        "20": { "port": "port1.0.10", "vlan": "voip" },
        "22": { "port": "port1.0.11" },
        "24": { "port": "port1.0.12" },
    },
    "2": {
        "1": { "port": "port1.0.13" },
    },
}

for pan_num in panels:
    for slot_num in panels[pan_num]:
        ppc = panels[pan_num][slot_num]
        assert ppc["port"] in ports.keys()
        ports[ppc["port"]]["vlan"] = ppc.get("vlan", "office")
        ports[ppc["port"]]["description"] = "%s-%s" % (pan_num, slot_num)


port_list = sorted(ports.values(), key=lambda x: x["number"])

with open(INPUT_FILENAME) as f:
    template = Template(f.read())

print template.render(
    vlans=vlan_list,
    tagged_vlan_vids=[x["label"] for x in vlan_list],
    ports=port_list)

