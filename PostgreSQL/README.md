# PostgreSQL
* On mac have https://postgresapp.com/ and for admin https://www.pgadmin.org/ ([download](https://www.pgadmin.org/download/pgadmin-4-macos/))
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
