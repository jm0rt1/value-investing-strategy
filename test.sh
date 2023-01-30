#!/usr/bin/env bash

if [python3 -m unittest discover -s tests -p '*test*.py']; then

    echo "Passed?"

fi