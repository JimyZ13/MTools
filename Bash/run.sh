#!/bin/bash

PARAM_FILE="params.txt"

CHANGE_FILE="al.scf.in"
SUBMIT_FILE="submit.pw"

cp "./$CHANGE_FILE.bak" "$CHANGE_FILE"
cp "./$SUBMIT_FILE.bak" "$SUBMIT_FILE"

sed -i "s/parameter_placeholder/0.0100/g" "$CHANGE_FILE"
sed -i "s/num_holder/0.0100/g" "$SUBMIT_FILE"

sbatch submit.pw
