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
    at510-top:
        dp_id: 0x1aeb949202
        description: "SDNCA"
        hardware: "Allied-Telesis"
        interfaces:
            2:
                tagged_vlans: [{{ tagged_vlan_vids|join(',') }}]
                name: "port1.0.2"
                description: "lan trunk"{% for port in sdnca_ports %}
            {{ port["number"] }}:
                native_vlan: {{ port["vlan"] }}
                name: "{{ port["name"] }}"
                description: "{{ port["description"] }}"{% endfor %}

    at510-bottom:
        dp_id: 0x1aeb95277d
        description: "SDNCB"
        hardware: "Allied-Telesis"
        interfaces:
            2:
                tagged_vlans: [{{ tagged_vlan_vids|join(',') }}]
                name: "port1.0.2"
                description: "lan trunk"{% for port in sdncb_ports %}
            {{ port["number"] }}:
                native_vlan: {{ port["vlan"] }}
                name: "{{ port["name"] }}"
                description: "{{ port["description"] }}"{% endfor %}

