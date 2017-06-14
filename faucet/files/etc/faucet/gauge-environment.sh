# directory containing FAUCET application code
GAUGE_APP=faucet.gauge
# file containing Gauge's custom ryu.conf
GAUGE_RYU_CONF=/etc/faucet/ryu.conf
# location of Gauge's configuration file.
GAUGE_CONFIG=/etc/faucet/gauge.yml
# where Gauge should log to
# (directory must exist and be writable by FAUCET_USER)
GAUGE_LOG="/var/log/faucet/gauge.log"
# where Gauge should log exceptions to (directory must exist as above)
GAUGE_EXCEPTION_LOG="/var/log/faucet/gauge-exception.log"
