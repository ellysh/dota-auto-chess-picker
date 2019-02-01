#!/bin/bash -x

DATABASE_DIR="database/docs"
TEMP_DIR="database/temp"
CSV_DIR="database/csv"

ssconvert -S -O 'separator=;' "$DATABASE_DIR/Database.ods" "$TEMP_DIR/Database.txt"

cp "$TEMP_DIR/Database.txt.0" "$CSV_DIR/buy.csv"
cp "$TEMP_DIR/Database.txt.1" "$CSV_DIR/combo.csv"
cp "$TEMP_DIR/Database.txt.2" "$CSV_DIR/fight.csv"
cp "$TEMP_DIR/Database.txt.3" "$CSV_DIR/recovery.csv"
cp "$TEMP_DIR/Database.txt.4" "$CSV_DIR/assault_enemy_tower.csv"
cp "$TEMP_DIR/Database.txt.5" "$CSV_DIR/farm.csv"
