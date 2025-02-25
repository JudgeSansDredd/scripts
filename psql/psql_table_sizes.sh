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

TABLES=(`PGPASSWORD=$PASSWORD psql -h $HOST -U $USER -d $DATABASE -t -c "SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND table_type='BASE TABLE' ORDER BY table_name ASC;"`)

for tablename in "${TABLES[@]}"
do
    SIZE=`PGPASSWORD=$PASSWORD psql -h $HOST -U $USER -d $DATABASE -t -c "SELECT pg_size_pretty(pg_total_relation_size('$tablename'));"`
    printf "%-45s | %-10s\n" "$tablename" "$SIZE"
done

DBSIZE=`PGPASSWORD=$PASSWORD psql -h $HOST -U $USER -d $DATABASE -t -c "SELECT pg_size_pretty(pg_database_size('$DATABASE'));"`
echo -e "----------------------------------------\n"
echo "Total Database Size - $DBSIZE"
