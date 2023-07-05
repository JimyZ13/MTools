#!/bin/bash

PARAM_FILE="params.txt"

CHANGE_FILE="al.scf.in"
SUBMIT_FILE="submit.pw"

cp "./$CHANGE_FILE.bak" "$CHANGE_FILE"
cp "./$SUBMIT_FILE.bak" "$SUBMIT_FILE"

while IFS= read -r param_value; do

	param_value=$(echo "$param_value" | tr -d '\n')

	sed -i "s/parameter_placeholder/$param_value/g" "$CHANGE_FILE"
	sed -i "s/num_holder/$param_value/g" "$SUBMIT_FILE"
	sleep 1
	sbatch submit.pw
	sleep 10
	cp "./$CHANGE_FILE.bak" "$CHANGE_FILE"
	cp "./$SUBMIT_FILE.bak" "$SUBMIT_FILE"

done < "$PARAM_FILE"

