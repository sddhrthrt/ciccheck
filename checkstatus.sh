#!/bin/bash

set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
TARGET=$DIR/target
mkdir -p $TARGET

echo "Target automatically selected: $TARGET"

if [[ ! -d "$TARGET/venv" ]]
then
    virtualenv -p python2 "$TARGET/venv"
fi
source "$TARGET/venv/bin/activate"
pip install selenium

DL_DRIVER=false
if [[ $# -gt 0 ]]
then
    DRIVER=$1
    echo "Driver selected: $DRIVER"
else
    if [[ -n "`which phantomjs`" ]]
    then
        DRIVER=phantomjs
    elif [[ -n "`which geckodriver`" ]]
    then
        DRIVER=geckodriver
    else
        DRIVER=geckodriver
    fi
    echo "Driver automatically selected: $DRIVER"
fi

if [[ -n "`which $DRIVER`" ]] 
then 
    echo "Driver found at `which $DRIVER`"
elif [[ -f "$TARGET/bin/$DRIVER" ]]
then
    echo "Driver found at $TARGET/bin/$DRIVER"
    export PATH=$PATH:$TARGET/bin/
else
    echo "Driver not found. Downloading to $TARGET/bin/"
    DL_DRIVER=true
fi


if [[ $DL_DRIVER = true ]]
then
    mkdir -p $TARGET/bin
    if [[ $DRIVER = 'phantomjs' ]]
    then
        wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 -O phantom.tar.bz2
        tar xvjf phantom.tar.bz2
        mv phantomjs-2.1.1-linux-x86_64/bin/phantomjs $TARGET/bin/
        rm -rf phantomjs-2.1.1-linux-x86_64 phantom.tar.bz2
    else
        wget https://github.com/mozilla/geckodriver/releases/download/v0.17.0/geckodriver-v0.17.0-linux64.tar.gz -O geckodriver.tar.gz
        tar xzvf geckodriver.tar.gz
        mv geckodriver $TARGET/bin/
        rm geckodriver.tar.gz
    fi 
    export PATH=$PATH:$TARGET/bin/

fi

export DRIVER
python status.py
