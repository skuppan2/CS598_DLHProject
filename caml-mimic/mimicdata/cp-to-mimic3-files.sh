#!/bin/bash
if [ $# -eq 0 ]
  then
    echo "Copy required MIMIC 3 raw data (CSV) files"
    echo "usage: ./link-to-mimic3-files.sh mimic3_sourcedir"
    exit -1
fi
echo "Creating symlinks to MIMIC3 data in $1"
cp $1/D_ICD_DIAGNOSES.csv D_ICD_DIAGNOSES.csv
cp $1/D_ICD_PROCEDURES.csv D_ICD_PROCEDURES.csv
cp $1/NOTEEVENTS.csv mimic3/NOTEEVENTS.csv
cp $1/DIAGNOSES_ICD.csv mimic3/DIAGNOSES_ICD.csv
cp $1/PROCEDURES_ICD.csv mimic3/PROCEDURES_ICD.csv
echo "...success"
