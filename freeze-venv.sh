#!/usr/bin/env bash
python3 -m venv ./venv 
source ./venv/bin/activate
pip freeze > requirements.txt