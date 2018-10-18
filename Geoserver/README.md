# Geoserver
* GeoServer is an open source software server written in Java that allows users to share and edit geospatial data. Designed for interoperability, it publishes data from any major spatial data source using open standards.
* User manual: https://docs.geoserver.org/latest/en/user/
* https://github.com/geoserver/
* Installation -> https://docs.geoserver.org/latest/en/user/installation/index.html -> cannot find a MacOS .dmg file, assume it no longer exists
* Follow https://docs.geoserver.org/latest/en/user/installation/osx_binary.html to download folder `geoserver-2.14.0`
* Rename `geoserver-2.14.0` to `geoserver` and move folder to `/usr/local/geoserver`
* Using Terminal, set the [env variable](https://medium.com/@himanshuagarwal1395/setting-up-environment-variables-in-macos-sierra-f5978369b255) `GEOSERVER_HOME` using `echo "export GEOSERVER_HOME=/usr/local/geoserver" >> ~/.bash_profile` to permanently add, restart terminal and check with `echo $GEOSERVER_HOME`
* Make myself owner of folder using `sudo chown -R robincole /Users/robincole/Documents/geoserver-2.14.0`
* `cd bin` and `sh startup.sh` to start GeoServer

## Admin
* In chrome view http://localhost:8080/geoserver
* Default creds: `{User name: admin, Password: geoserver}`
* [Add a postGIS db](https://docs.geoserver.org/latest/en/user/data/database/postgis.html)
* Run docs server locally https://github.com/geoserver/geoserver.github.io
* [CURL docs](https://docs.geoserver.org/2.0.0/user/extensions/rest/rest-config-examples-curl.html)

## Python API
* [Read](https://docs.geoserver.org/latest/en/user/community/scripting/py/index.html)

## OWSLib
* https://github.com/geopython/OWSLib
* OWSLib is a Python package for client programming with Open Geospatial Consortium (OGC) web service (hence OWS)

## GSconfig
* https://github.com/boundlessgeo/gsconfig
* Python wrapper to the geoserver rest API
* Last updated in 2015?
* Python 2 and uses [httplib2](https://github.com/httplib2/httplib2)
* Worth bothering with?

## Extensions
* A variety of [extensions](https://docs.geoserver.org/latest/en/user/extensions/index.html#extensions) are available for geoserver
* [NetCDF data store extension](https://docs.geoserver.org/latest/en/user/extensions/netcdf/netcdf.html) - this format is [supported by Pangeo](http://pangeo.io/architecture.html#hdf-and-netcdf)

### Cloud Optimized GeoTIFF
* https://www.cogeo.org/
* GeoServer can use a new GeoTools community module named 's3-geotiff' to use COG's as a datastore.
* [Rio-cogeo](https://github.com/mapbox/rio-cogeo) Rasterio plugin creates Cloud Optimized GeoTIFF's.
* [s3-geotiff](https://github.com/geotools/geotools/tree/master/modules/unsupported/s3-geotiff)

### pycsw
* Publish metadata
* Python
* http://pycsw.org/

### FeatureServer
* http://featureserver.org/ Python server
* https://github.com/iocast/featureserver last activity 2015

### Exoserver
* http://eoxserver.org/
* EOxServer is a Python (2) application and framework for presenting Earth Observation (EO) data and metadata.
* Looks like development has gone cold

## GeoDjango
* Create web app with Geoserver backend https://github.com/liorshahverdi/learning-geodjango
* Example app https://github.com/ngageoint/geoq

### Other references
* Course https://www.udemy.com/enterprise-gis/?couponCode=gisadvisor
* OWSlib http://geopython.github.io/OWSLib/
* https://geotrellis.io/
* [Guide on AWS linux ec2 instance with GeoServer & PostGIS](https://gist.github.com/karlaking/6a58279652f6ea23fd085aa5d7822119)
* [geoserver-docker](https://github.com/DenisCarriere/Geoserver-Docker)

### Acronyms
* **WMS** Web Map Service Interface Standard (WMS) provides a simple HTTP interface for requesting geo-registered map images from one or more distributed geospatial databases.  A WMS request defines the geographic layer(s) and area of interest to be processed. The response to the request is one or more geo-registered map images (returned as JPEG, PNG, etc) that can be displayed in a browser application. The interface also supports the ability to specify whether the returned images should be transparent so that layers from multiple servers can be combined or not.
* **WCS** Web Coverage Service (WCS) offers multi-dimensional coverage data for access over the Internet.
* **WFS** Web Feature Service (WFS) standard, which permits the actual sharing and editing of the data that is used to generate the maps.
