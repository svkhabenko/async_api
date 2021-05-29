#!/bin/bash

# -e Exit immediately if a pipeline returns a non-zero status
# -x Print a trace of simple commands
# -u Treat unset variables and parameters as an error
set -ex
#set -u
echo "$1"
echo "$@"

case $1 in
    api)
        echo "START API"
        exec gunicorn src.main:app -w 4 -b 0.0.0.0:8000 -k uvicorn.workers.UvicornWorker
        ;;
    *)
        if [ $# -eq 0]
          then
            echo "No arguments supplied"
          else
            echo "Running '$1' command..."
            exec "$1"
        fi
        ;;
esac
