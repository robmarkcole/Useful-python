# Geoserver
* GeoServer is an open source software server written in Java that allows users to share and edit geospatial data. Designed for interoperability, it publishes data from any major spatial data source using open standards.
* https://github.com/geoserver/
* Installation -> https://docs.geoserver.org/latest/en/user/installation/index.html -> cannot find a MacOS .dmg file, assume it no longer exists
* Follow https://docs.geoserver.org/latest/en/user/installation/osx_binary.html to download folder `geoserver-2.14.0`
* Move folder to `/Users/robincole/Documents/geoserver-2.14.0`
* Set the env variable `GEOSERVER_HOME` using `export GEOSERVER_HOME=/Users/robincole/Documents/geoserver-2.14.0` and check with `echo $GEOSERVER_HOME`
* Make myself owner of folder using `sudo chown -R robincole /Users/robincole/Documents/geoserver-2.14.0`
