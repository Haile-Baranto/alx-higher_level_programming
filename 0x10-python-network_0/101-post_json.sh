#!/bin/bash
# This script sends a JSON POST request to a URL with the contents of a file in the body, and displays the body of the response.
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"
