#!/bin/bash
# This script sends a request to a URL using curl and display only status code
curl -s -o /dev/null -w "%{http_code}" "$1"
