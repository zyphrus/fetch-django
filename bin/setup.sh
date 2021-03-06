#!/bin/bash

if [ ! -n $1 ]; then
    $1=""
fi

[ ! -n "$(command -v pip)" ] && echo "Requires pip to install" && exit
[ ! -n "$(command -v npm)" ] && echo "Requires npm to install" && exit
# [ ! -n "$(command -v bower)" ] && echo "Missing bower. Installing it" && exit

# python
pip install -r requirements/common.txt

# bower - frontend
python manage.py bower install $1

# django
python manage.py migrate $1
