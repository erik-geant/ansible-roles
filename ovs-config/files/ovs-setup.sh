ETHIFC=enp3s0

ip tuntap add mode tap vport1
ip tuntap add mode tap vport2
ifconfig vport1 up
ifconfig vport2 up

ovs-vsctl --may-exist add-br mybridge
ovs-vsctl --may-exist add-port mybridge $ETHIFC -- \
          --may-exist add-port mybridge vport1 -- \
          --may-exist add-port mybridge vport2
ip address flush $ETHIFC 
dhclient mybridge

