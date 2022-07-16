rm database.db
sqlite3 database.db < create.sql
sqlite3 database.db < fill_with_data.sql
