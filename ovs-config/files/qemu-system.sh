#!/bin/sh

#/etc/qemu-ifup xyzaaa
#qemu-system-x86_64 -enable-kvm -net nic -net tap,ifname=xyzaaa -hda /images/b.qcow2 -m 512 -nographic
#/etc/qemu-ifdown xyzaaa

#-daemonize

#qemu-system-x86_64  -enable-kvm -net nic -net tap,ifname=xyzaaa -hda /images/b.qcow2 -m 512 -vnc :5,vncpass -daemonize

#qemu-system-x86_64  -enable-kvm -net nic -net tap,ifname=xyzaaa -hda /images/b.qcow2 -m 512 -vnc :5,vncpass -monitor stdio

#  -daemonize -display none

# qemu-system-x86_64  -enable-kvm -net nic -net tap,ifname=xyzaaa -hda /images/b.qcow2 -m 512  -daemonize
# qemu-system-x86_64  -enable-kvm -net nic -net tap,ifname=xyzaaa -hda /images/b.qcow2 -m 512  -daemonize -display none

qemu-system-x86_64  -enable-kvm -net nic -net tap,ifname=xyzaaa -hda /images/b.qcow2 -m 512 -vnc :5 -daemonize

