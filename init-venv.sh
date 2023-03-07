#!/usr/bin/env bash
echo "OSTYPE = ${OSTYPE}"
if [[ "$OSTYPE" == "darwin"* ]]; then
    #mac zsh
    echo "OS = MacOS"
    python3 -m venv ./venv 
    source ./venv/bin/activate
elif [[ "$OSTYPE" == "msys" ]]; then
    #windows mingw/git bash
    echo "OS = Windows"
    py -3.11 -m venv ./venv
    source ./venv/Scripts/activate

else
    echo "OS not found."
    exit
fi
FILE=requirements.txt
if test -f "$FILE"; then
    pip install -r requirements.txt
    pip install -U autopep8
fi
