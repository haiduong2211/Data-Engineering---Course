#!/bin/bash "C:\Users\Duong Nguyen\Desktop\DE\DEP302\DEP302_ASM2"

#stop on error
set -e

DB_NAME = DEP302_ASM2

DB_AUTH = "-u -root -p dbpw11 -h localhost"

#redirect to C:\Users\Duong Nguyen\Desktop\DE\DEP302\DEP302_ASM2> folder
cd "C:\Users\Duong Nguyen\Desktop\DE\DEP302\DEP302_ASM2"
#current directory
cd "$(dirname "$0")"

#Drop the database
mongosh $DB_AUTH --quiet "$DB_NAME" --eval "db.dropDatabase()"
echo "Database $DB_NAME dropped"

echo "Create full collection with mongoimport"
mongoimport $DB_AUTH --db $DB_NAME --collection full --type csv --headerline "US Adult Income.CSV"


