#!/bin/bash -x

DATABASE_DIR="docs"
TEMP_DIR="temp"
CSV_DIR="csv"

ssconvert -S -O 'separator=;' "$DATABASE_DIR/Database.ods" "$TEMP_DIR/Database.txt"

ssconvert -S -O 'separator=;' "$DATABASE_DIR/Strategy.ods" "$TEMP_DIR/Strategy.txt"

ssconvert -S -O 'separator=;' "$DATABASE_DIR/Combos.ods" "$TEMP_DIR/Combos.txt"

cp "$TEMP_DIR/Database.txt.0" "$CSV_DIR/pieces.csv"
cp "$TEMP_DIR/Database.txt.1" "$CSV_DIR/species.csv"
cp "$TEMP_DIR/Database.txt.2" "$CSV_DIR/classes.csv"
cp "$TEMP_DIR/Database.txt.3" "$CSV_DIR/items.csv"
cp "$TEMP_DIR/Strategy.txt.0" "$CSV_DIR/strategies.csv"
cp "$TEMP_DIR/Combos.txt.0" "$CSV_DIR/combos.csv"
