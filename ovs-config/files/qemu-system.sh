#!/bin/sh

VMNAME=xyzabc
VNCIDX=5
IMAGE_FILE=/images/$VMNAME.qcow2

cp /images/debian_wheezy_amd64_standard.qcow2 $IMAGE_FILE

qemu-system-x86_64  \
    -enable-kvm \
    -net nic \
    -net tap,ifname=$VMNAME \
    -hda $IMAGE_FILE \
    -m 512 \
    -vnc :$VNCIDX \
    -daemonize
