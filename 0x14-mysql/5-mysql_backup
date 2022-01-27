#!/usr/bin/env bash
# Script that generates a back up from a database
DATE=$(date +'%d-%m-%Y')
mysqldump -uroot --password="$11" --all-databases > backup.sql
sudo tar -czf "$DATE".tar.gz backup.sql
