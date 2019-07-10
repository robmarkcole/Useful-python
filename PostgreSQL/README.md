# PostgreSQL
* On Mac, for running the postgres server use https://postgresapp.com/ or Docker
* On Synology in Docker, select use default network and allow auto port (5432 is blocked for some reason)
* For admin https://www.pgadmin.org/ ([download](https://www.pgadmin.org/download/pgadmin-4-macos/))
* [PostGIS](http://postgis.net/) is a spatial database extender. It adds support for geographic objects allowing location queries to be run in SQL.

```sql
SELECT superhero.name
FROM city, superhero
WHERE ST_Contains(city.geom, superhero.geom)
AND city.name = 'Gotham';
```

* PgAdmin 4.3 [has a PostGIS geometry viewer](http://www.bostongis.com/blog/index.php?url=archives/272-pgAdmin4-now-offers-PostGIS-geometry-viewer.html#feedback). You will be able to see the graphical output of your query directly in pgAdmin.
* We will be interested in [GeoAlchemy2](https://geoalchemy-2.readthedocs.io/en/latest/)
* [Psql](http://postgresguide.com/utilities/psql.html) is the interactive terminal tool for working with Postgres

## PGadmin
* The official docs aren't great
* [Getting started guide](https://linuxhint.com/pgadmin4_tutorial_beginners/) -> create a table using the GUI
* To export a `CREATE TABLE` script select the db, select BACKUP, format 'Plain' and "Only schema".
