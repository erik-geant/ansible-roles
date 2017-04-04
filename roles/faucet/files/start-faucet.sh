#!/bin/bash

. ~faucet/virtenv/bin/activate
. /etc/default/faucet

export FAUCET_CONFIG
export FAUCET_LOG
export FAUCET_EXCEPTION_LOG

ryu-manager --config-file=$FAUCET_RYU_CONF --ofp-listen-host=$FAUCET_LISTEN_HOST --ofp-tcp-listen-port=$FAUCET_LISTEN_PORT $FAUCET_APP_DIR/faucet.py

