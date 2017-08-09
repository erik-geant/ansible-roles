#!/bin/sh

VMNAME=testvm1
VNCIDX=3
IMAGE_FILE=/images/$VMNAME.qcow2

cp /images/debian_wheezy_amd64_standard.qcow2 $IMAGE_FILE

#qemu-system-x86_64  \
#    -enable-kvm \
#    -net nic \
#    -net tap,ifname=$VMNAME \
#    -hda $IMAGE_FILE \
#    -m 512 \
#    -vnc :$VNCIDX \
#    -daemonize

qemu-system-x86_64  \
    -enable-kvm \
    -netdev tap,ifname=$VMNAME,id=eth \
    -device e1000,netdev=eth,mac=52:00:00:00:00:01 \
    -hda $IMAGE_FILE \
    -m 512 \
    -vnc :$VNCIDX \
    -daemonize 
