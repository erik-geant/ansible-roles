#!/bin/bash

. ~faucet/virtenv/bin/activate
. /etc/faucet/faucet-environment.sh

export FAUCET_CONFIG
export FAUCET_LOG
export FAUCET_EXCEPTION_LOG

ryu-manager --config-file=$FAUCET_RYU_CONF  $FAUCET_APP

