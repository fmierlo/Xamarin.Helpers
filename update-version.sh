#!/bin/bash

for dir in Helpers Tests/Droid Tests/iOS
do
    cd "${dir}"
    python update-version.py
    cd -
done
