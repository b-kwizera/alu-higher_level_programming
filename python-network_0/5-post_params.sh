#!/bin/bash
# Sends a POST request with email and subject as parameters and displays the response body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
