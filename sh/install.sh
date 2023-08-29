#!/bin/bash

rm -rf .venv
virtualenv .venv
. .venv/bin/activate

pip3 install -r requirements.txt

mkdir -p log
