#!/bin/bash

declare -A ELFS=()

INC=1
ELFS[$INT]=0

#pasted the data set to a file
INGEST=`cat 1.input | sed 's|^$|NULL|g'`

for FOOD in $INGEST
do
    if [ ${FOOD} != NULL ]
    then
        echo "Adding $FOOD to ELF$INC"
        ELFS[$INC]=$((${ELFS[$INC]}+$FOOD))
    elif [ ${FOOD} == NULL ]
    then
        echo "ELF${INC} total: ${ELFS[$INC]}"
        echo "Incrementing Elf"
        INC=$(($INC+1))
    else
        echo "Something is wrong with the food"
    fi
done

HV2=0
HV3=0
HIGHEST_VALUE=0
for KEY in "${!ELFS[@]}"
do
    echo "Key: $KEY \t Value: ${ELFS[$KEY]}"
    if [ ${ELFS[$KEY]} -ge $HIGHEST_VALUE ]
    then
        HV3=$HV2
        HV2=$HIGHEST_VALUE
        HIGHEST_ELF=$KEY
        HIGHEST_VALUE=${ELFS[$KEY]}
    fi
done

echo "Highest Elf is $HIGHEST_ELF and its value is $HIGHEST_VALUE"
echo "Three highest elves summed to: $(($HIGHEST_VALUE+$HV2+$HV3))"

print_all_values () {
    for KEY in "${!ELFS[@]}"
    do
        echo "${ELFS[$KEY]}"
    done | sort -n | tail -10
}

print_all_values
