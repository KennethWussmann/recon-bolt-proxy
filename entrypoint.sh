#!/bin/bash

COMMAND="mitmweb -s /app/modify_reconbolt_requests.py --web-host 0.0.0.0 --allow-hosts ^(?:.*\.)?(auth\.riotgames\.com|pvp\.net)$ --listen-host 0.0.0.0"

if [[ ! -z "$MODE" ]]
then
  echo "Executing in mode ${MODE}"
  COMMAND="${COMMAND} --mode $MODE"
fi

$COMMAND
