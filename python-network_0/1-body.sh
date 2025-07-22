#!/bin/bash
# Sends a GET request and displays the body only if the response code is 200
curl -sL -w "%{http_code}" "$1" -o tmp_body | {
    read -r status
    if [ "$status" -eq 200 ]; then
        cat tmp_body
    fi
    rm -f tmp_body
}
