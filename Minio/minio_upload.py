from minio import Minio
from minio.error import ResponseError

SERVER_IP = '192.168.67.206'
SERVER_PORT = '9000'
SERVER = '{}:{}'.format(SERVER_IP, SERVER_PORT)

MINIO_ACCESS_KEY = 'access_key'
MINIO_SECRET_KEY = 'secret_key'

# FILE_TO_UPLOAD = 'mlx90640-2019-04-11-15-14-27.jpg'
FILE_TO_UPLOAD = 'minio_upload.py'

minioClient = Minio(
    SERVER,
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=False)

# Get buckets
buckets = minioClient.list_buckets()
for bucket in buckets:
    print(bucket.name)
    
minioClient.fput_object(
    buckets[0].name,
    FILE_TO_UPLOAD,
    FILE_TO_UPLOAD
    )

print("Uploaded file {} to {}".format(FILE_TO_UPLOAD, SERVER))