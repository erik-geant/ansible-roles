#!/bin/bash

. ~faucet/virtenv/bin/activate
. /etc/faucet/gauge-environment.sh

export GAUGE_CONFIG
export GAUGE_LOG
export GAUGE_EXCEPTION_LOG

ryu-manager --config-file=$GAUGE_RYU_CONF  $GAUGE_APP

