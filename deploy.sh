#!/bin/bash
FILE=$1
if [ -f $FILE ];
then
    if [ ! -z $FILE ];
    then
        scp -i /home/dflies/deploy1/id_rsa $1 fisle:./fisle/pages/
    fi
fi
sleep 1
echo "Building.."
ssh -i /home/dflies/deploy1/id_rsa fisle 'source /home/dflies/fisle/venv/bin/activate && python /home/dflies/fisle/fisle.py build'
echo "Complete!"
