#!/usr/bin/env bash 

rsync -aPh ../Projects/extracted/ ../Projects/extracted-source/ 
python3 sort-libraries.py ../Projects/extracted-source/ .
