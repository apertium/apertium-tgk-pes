#!/bin/bash

C=2
GREP='.'
if [ $# -eq 1 ]
then
    C=$1
    GREP='WORKS'
fi

sh wiki-tests.sh Pending tg fa update | grep -C $C "$GREP"

sh wiki-tests.sh Pending fa tg update | grep -C $C "$GREP"


