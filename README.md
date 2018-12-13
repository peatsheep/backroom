# Yharnam Clinic

### APIs to facilitate Bloodborne-related webapps, such as:
- Character Build Planner
- Run randomizer
- Info pages for item data & boss strategies
- etc.

### Data setup
1. Ensure Sqlite3 is installed
2. run `sqlite3 bloodborne.db`
3. run the following commands: 
```
.read schema.sql
.mode csv
.import attire.csv attire
```