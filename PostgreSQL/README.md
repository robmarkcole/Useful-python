# PostgreSQL
* On Mac, for running the postgres server use https://postgresapp.com/ or Docker
* On Synology in Docker, select use default network and allow auto port (5432 is blocked for some reason)
* [Psql](http://postgresguide.com/utilities/psql.html) is the command line tool for working with Postgres
* For UI admin https://www.pgadmin.org/ ([download](https://www.pgadmin.org/download/pgadmin-4-macos/))

## psycopg2
* https://pypi.org/project/psycopg2-binary/
* Psycopg2 is the most popular PostgreSQL database adapter for the Python.
* Install `psycopg2-binary` instead of `psycopg2` if you are getting install errors
* Psycopg2 is mostly implemented in C as a libpq wrapper. For a pure python alternative checkout [pg8000](https://github.com/tlocke/pg8000)

## PostGIS
* [PostGIS](http://postgis.net/) is a spatial database extender. It adds support for geographic objects allowing location queries to be run in SQL.

```sql
SELECT superhero.name
FROM city, superhero
WHERE ST_Contains(city.geom, superhero.geom)
AND city.name = 'Gotham';
```

* PgAdmin 4.3 [has a PostGIS geometry viewer](http://www.bostongis.com/blog/index.php?url=archives/272-pgAdmin4-now-offers-PostGIS-geometry-viewer.html#feedback). You will be able to see the graphical output of your query directly in pgAdmin.
* We will be interested in [GeoAlchemy2](https://geoalchemy-2.readthedocs.io/en/latest/)

## PGadmin
* [Getting started guide](https://linuxhint.com/pgadmin4_tutorial_beginners/) -> create a table using the GUI
* To export a `CREATE TABLE` script select the db, select BACKUP, format 'Plain' and "Only schema".

## Postico
* Simple mac app for exploring db
* https://eggerapps.at/postico/