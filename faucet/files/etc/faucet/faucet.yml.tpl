version: 2
vlans:{% for vlan in vlans %}
    {{ vlan["label"] }}:
        name: "{{ vlan["name"] }}"
        vid: {{ vlan["vid"] }}
        unicast_flood: True{% endfor %}
acls:
    101:
        - rule:
            dl_src: "ae:ad:61:7d:02:2f"
            actions:
                allow: 1
        - rule:
            actions:
                allow: 0
dps:
    windscale-faucet-1:
        dp_id: 0x1aeb949202
        description: "SDNCA"
        hardware: "Allied-Telesis"
        interfaces:
            2:
                tagged_vlans: [{{ tagged_vlan_vids|join(',') }}]
                name: "port1.0.2"
                description: "sdnca"{% for port in ports %}
            {{ port["number"] }}:
                native_vlan: {{ port["vlan"] }}
                name: "{{ port["name"] }}"
                description: "{{ port["name"] }}"{% endfor %}

