
# SQL More Queries

This project demonstrates advanced MySQL operations including user management, privileges, constraints, and JOINs.

## Tasks

0. **0-privileges.sql** - Lists privileges for users

1. **1-create_user.sql** - Creates user with all privileges

2. **2-create_read_user.sql** - Creates user with SELECT privilege

3. **3-force_name.sql** - Creates table with NOT NULL constraint

4. **4-never_empty.sql** - Creates table with DEFAULT value

5. **5-unique_id.sql** - Creates table with UNIQUE constraint

6. **6-states.sql** - Creates states table with PRIMARY KEY

7. **7-cities.sql** - Creates cities table with FOREIGN KEY

8. **8-cities_of_california_subquery.sql** - Lists cities using subquery

9. **9-cities_by_state_join.sql** - Lists cities using JOIN

10. **10-genre_id_by_show.sql** - Lists shows with genres

11. **11-genre_id_all_shows.sql** - Lists all shows (with LEFT JOIN)

12. **12-no_genre.sql** - Lists shows without genres

13. **13-count_shows_by_genre.sql** - Counts shows by genre

14. **14-my_genres.sql** - Lists genres for specific show

15. **15-comedy_only.sql** - Lists comedy shows

16. **16-shows_by_genre.sql** - Lists shows with their genres

## Key Concepts

- **PRIMARY KEY**: Unique identifier for records

- **FOREIGN KEY**: Maintains referential integrity

- **NOT NULL**: Prevents NULL values

- **UNIQUE**: Ensures unique values

- **DEFAULT**: Sets default values

- **JOIN**: Combines rows from multiple tables

- **LEFT JOIN**: Returns all records from left table

## Requirements

- MySQL 8.0

- Ubuntu 20.04 LTS

- All SQL keywords in UPPERCASE

- Comments before each query

## Usage

```bash

cat <file>.sql | mysql -uroot -p [database]

```

## Author

Norah Alnujidi

