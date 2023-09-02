#!/bin/bash
#takes in url, sends a request and displays the of body of response
curl -s "$1" | wc -c
