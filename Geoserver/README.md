# Geoserver
* GeoServer is an open source software server written in Java that allows users to share and edit geospatial data. Designed for interoperability, it publishes data from any major spatial data source using open standards.
* https://github.com/geoserver/
* Installation -> https://docs.geoserver.org/latest/en/user/installation/index.html -> cannot find a MacOS .dmg file, assume it no longer exists
* Follow https://docs.geoserver.org/latest/en/user/installation/osx_binary.html to download folder `geoserver-2.14.0`
* Rename `geoserver-2.14.0` to `geoserver` and move folder to `/usr/local/geoserver`
* Using Terminal, set the [env variable](https://medium.com/@himanshuagarwal1395/setting-up-environment-variables-in-macos-sierra-f5978369b255) `GEOSERVER_HOME` using `echo "export GEOSERVER_HOME=/usr/local/geoserver" >> ~/.bash_profile` to permanently add, restart terminal and check with `echo $GEOSERVER_HOME`
* Make myself owner of folder using `sudo chown -R robincole /Users/robincole/Documents/geoserver-2.14.0`
* `cd bin` and `sh startup.sh` to start GeoServer
* In chrome view http://localhost:8080/geoserver
