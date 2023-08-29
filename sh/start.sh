#!/bin/bash

PORT=12345
FORCE=false

while [ $# -gt 0 ]; do
    opt="$1";
    shift;

    case "$opt" in
        --force|-f)
            FORCE=true
            ;;
        *)
            echo "Unknown argument: $1"
            ;;
    esac
done

RUNNING=false
if lsof -i :${PORT} >/dev/null 2>&1; then
    RUNNING=true
fi

t=$(date "+%Y-%m-%d %H:%M:%S")
if [ "${RUNNING}" = false ] || [ "${FORCE}" = true ]; then
    pid=$(lsof -ti:${PORT})
    kill -9 ${pid}

    mkdir -p ~/log

    . .venv/bin/activate
    . ./sh/env.sh
    PYTHONPATH=$PYTHONPATH:../ python3 app.py 2> ~/log/notify.txt &

    echo "[${t}] [INFO] started."
else
    echo "[${t}] [INFO] already running."
fi
