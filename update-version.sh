#!/bin/bash

for dir in Helpers Helpers.UITests.Droid Helpers.UITests.iOS
do
    cd "${dir}"
    python update-version.py
    cd ..
done
