# GDAL
* https://www.gdal.org/
* C++ tools for raster and vector geospatial data tasks ([source](https://github.com/OSGeo/gdal))
* Download binaries for Mac from http://www.kyngchaos.com/software:frameworks and installed 2.2 as latest available
* [Current release is 2.3.1](https://trac.osgeo.org/gdal/wiki/Release/2.3.1-News)
* Python bindings https://pypi.org/project/GDAL/ and `$ pip install GDAL` but [get a long list of errors](https://github.com/OSGeo/gdal/issues/845#issuecomment-412429914) as requires 2.3. Can install 2.2 bindings with `$ pip install gdal===2.2.0`. For 2.3 will need to build from source, or see if Brew has latest version.
* For an alternative see [Rasterio](https://github.com/mapbox/rasterio)