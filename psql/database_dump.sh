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

for TABLENAME in "${TABLES[@]}"
do
    printf "Dumping Schema + Data | $TABLENAME \n"
    `PGPASSWORD=$PASSWORD pg_dump -h $HOST -U $USER -d $DATABASE -t $TABLENAME --file=$TABLENAME.sql`
    `ex -sc '9i|SET session_replication_role = replica;' -c '$a|SET session_replication_role = default;' -cx $TABLENAME.sql`
    `tar rf $DATABASE.tar $TABLENAME.sql`
    `rm $TABLENAME.sql`
done

echo -e "----------------------------------------\n\n"

printf "Zipping up $DATABASE.tar to $DATABASE.tar.gz\n"
`gzip $DATABASE.tar`
