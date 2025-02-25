#!/bin/bash

if [ -z "$1" ];then
  read -p "What is the host address: " HOST
else
  HOST=$1
fi

if [ -z "$2" ];then
  read -p "What is the username: " USER
else
  USER=$2
fi

if [ -z "$3" ];then
  read -p "What is the database name: " DATABASE
else
  DATABASE=$3
fi

read -p "What is the database password: " PASSWORD

echo -e "\n"

source tables.txt

for TABLENAME in "${TABLES[@]}"
do
    printf "Uploading Schema + Data | $TABLENAME \n"
    `PGPASSWORD=$PASSWORD psql -h $HOST -U $USER -d $DATABASE < $TABLENAME.sql`
done
