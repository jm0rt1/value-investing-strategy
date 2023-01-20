#!/usr/bin/env bash
python3 -m venv ./venv 
source ./venv/bin/activate
FILE=requirements.txt
if test -f "$FILE"; then
    pip install -r requirements.txt
fi
