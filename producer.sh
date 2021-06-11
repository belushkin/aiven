#! /bin/sh

python -m flake8 --ignore=E501,F401 .
python -m pytest
python ./producer.py
