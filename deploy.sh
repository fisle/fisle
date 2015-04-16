#!/bin/bash
FILE=$1
if [ -f $FILE ];
then
    if [ ! -z $FILE ];
    then
        scp $1 fisle:./fisle/pages/
    fi
fi
sleep 1
echo "Building.."
ssh fisle 'source /home/dflies/fisle/venv/bin/activate && python /home/dflies/fisle/fisle.py build'
echo "Complete!"
