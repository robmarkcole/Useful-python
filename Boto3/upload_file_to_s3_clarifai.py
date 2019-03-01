"""
Main code for processing images with clarify, saving image to s3, and returning contents of images.
"""

import boto3
from clarifai.rest import ClarifaiApp

aws_bucket_name = '85276b70-14d2-431c'
valid_classes = ['apple', 'banana', 'tangerine']
#image_file_path = 'image.jpg'


def identify_image(image_file_path):
    clarifai_app = ClarifaiIdentify(aws_bucket_name, valid_classes)
    name, value = clarifai_app.process_file(image_file_path)
    if name:
        return name
    return 'Unidentified'


class ClarifaiIdentify():
    """
    Class to identify the most likely object in an image.
    """

    def __init__(self, aws_bucket_name, valid_classes):
        self._aws_bucket_name = aws_bucket_name
        self._valid_classes = valid_classes

        app = ClarifaiApp()
        self._general_model = app.models.get('general-v1.3')
        self._s3_client = boto3.client('s3')
        self._s3_url = ''
        self._concepts = []

    def upload_file_to_s3(self, file_path):
        """
        Upload an image file to s3 and return the url.
        """
        self._s3_client.upload_file(Filename=file_path,
                                    Bucket=self._aws_bucket_name,
                                    Key=self._aws_bucket_name,
                                    ExtraArgs={'ACL': 'public-read'})
        s3_url = print('https://s3.amazonaws.com/{0}/{0}'.format(self._aws_bucket_name))
        return s3_url

    def process_file(self, file_path):
        """
        Process a file.
        """
        self._s3_url = self.upload_file_to_s3(file_path)
        response = self._general_model.predict_by_url(self._s3_url)

        self._concepts = response['outputs'][0]['data']['concepts']
        for concept in self._concepts:
            if concept['name'] in self._valid_classes:
                return (concept['name'], concept['value'])
        return None, None
