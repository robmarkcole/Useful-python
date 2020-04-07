# https://github.com/archydeberker/corona-calculator/blob/master/s3_utils.py
import datetime
import os
from io import BytesIO

import boto3
from botocore.exceptions import ClientError

_S3_ACCESS_KEY = os.environ["AWSAccessKeyId"].replace("\r", "")
_S3_SECRET_KEY = os.environ["AWSSecretKey"].replace("\r", "")
_S3_BUCKET_NAME = "coronavirus-calculator-data"

DATESTRING_FORMAT_READABLE = "%A %d %B %Y, %H:%M %Z"  # 'Sunday 30 November 2014'


def _configure_client():
    # Upload the file
    s3_client = boto3.client(
        "s3", aws_access_key_id=_S3_ACCESS_KEY, aws_secret_access_key=_S3_SECRET_KEY
    )
    return s3_client


def upload_file(data: bytes, object_name: str):
    """
    Upload a file to an S3 bucket
    :param data: Bytes to upload.
    :param object_name: S3 object name.
    :return: True if file was uploaded, else False
    """
    buf = BytesIO(data)
    s3_client = _configure_client()
    try:
        response = s3_client.put_object(
            Body=buf, Bucket=_S3_BUCKET_NAME, Key=object_name
        )
    except ClientError as e:
        print(e)
        return False
    return True


def download_file(object_name: str):
    """
    Download a file from S3 bucket.
    :param object_name: Name of object to download.
    :return: Object bytes and date last modified.
    """
    s3_client = _configure_client()
    download = s3_client.get_object(Key=object_name, Bucket=_S3_BUCKET_NAME)
    content = download["Body"].read()
    last_modified = download["LastModified"].strftime(DATESTRING_FORMAT_READABLE)
    return content, last_modified
