# Min.io
* https://min.io/ and [docs](https://docs.min.io/)
* Open Source, Amazon S3 Compatible Object Storage
* To pull/update `docker pull minio/minio` 
* To test: 

`
docker run -p 9000:9000 -e "MINIO_ACCESS_KEY=access_key" -e "MINIO_SECRET_KEY=secret_key" minio/minio server /data
` 

then http://localhost:9000 but note data will be lost on restart.

## Python API
* https://github.com/minio/minio-py

## Synology
* Instructions -> https://blog.jonaharagon.com/installing-minio-on-synology/ -> main catch is you need to use the execution command `minio server /data`, also I noticed you need to edit the environment variable name for the access_key to `MINIO_ACCESS_KEY`