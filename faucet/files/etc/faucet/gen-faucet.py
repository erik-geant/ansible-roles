import os
from jinja2 import Template 


INPUT_FILENAME = os.path.join(os.path.dirname(__file__), "faucet.yml.tpl")

DEFAULT_VLAN = "office"

VLANS = {
    "Sysadmin": 2,
    "VoIP": 3,
    "Office": 4,
    "Guests": 7,
    "IPv6 only": 20,
    "TOMBS managment network": 983,
    "TOMBS VM network": 984,
}

SDNCA_FIRST_PORT = 3
SDNCA_LAST_PORT = 42
SDNCB_FIRST_PORT = 48
SDNCB_LAST_PORT = 48

SDNCA_PATCH_PORTS = {
    "1-12": { "port": 3 },
    "1-2": { "port": 5 },
    "1-11": { "port": 6 },
    "1-17": { "port": 7 },
    "1-18": { "port": 8 },
    "1-19": { "port": 9 },
    "1-22": { "port": 11 },
    "1-24": { "port": 12 },

    "2-2": { "port": 4 },
    "2-3": { "port": 10 },
    "2-4": { "port": 13 },
    "2-6": { "port": 14 },
    "2-7": { "port": 15,
        "vlan": "sysadmin", "info": "dick and max" },
    "2-9": { "port": 16,
        "vlan": "sysadmin", "info": "camera, ruud etc."},

    "3-5": { "port": 33, "vlan": "voip" },
    "3-11": { "port": 34, "vlan": "voip" },

    "4-11": { "port": 35, "vlan": "voip" },
    "6-9": { "port": 36, "vlan": "voip" },
}

SDNCB_PATCH_PORTS = {
    "2-17": { "port": 48, "info": "by erik's desk" }
}


def _vlan_label(s): return s.lower().replace(" ", "-")


def _gen_port_list(first_port_num, last_port_num, patch_map):
    ports = {}
    for i in range(first_port_num, last_port_num+1):
        name = "port1.0.%d" % i
        ports[name] = {
            "number": i,
            "description": name,
            "name": name,
            "vlan": DEFAULT_VLAN }

    for patch_name, port_info in patch_map.items():
        port_name = "port1.0.%d" % port_info["port"]
        assert port_name in ports.keys()
        ports[port_name]["vlan"] = port_info.get("vlan", DEFAULT_VLAN)
        description = patch_name
        if "info" in port_info: 
            description += " " + port_info["info"]
        ports[port_name]["description"] = description

    return sorted(ports.values(), key=lambda x: x["number"])

with open(INPUT_FILENAME) as f:
    template = Template(f.read())

vlan_list = [ {
    "label": _vlan_label(k),
    "name": k,
    "vid": v} for k,v in VLANS.items() ]
vlan_list = sorted(vlan_list, key=lambda x: x["vid"])


print template.render(
    vlans=vlan_list,
    tagged_vlan_vids=[x["label"] for x in vlan_list],
    sdnca_ports=_gen_port_list(SDNCA_FIRST_PORT, SDNCA_LAST_PORT, SDNCA_PATCH_PORTS),
    sdncb_ports=_gen_port_list(SDNCB_FIRST_PORT, SDNCB_LAST_PORT, SDNCB_PATCH_PORTS))

