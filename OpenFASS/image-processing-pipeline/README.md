* Article -> https://blog.alexellis.io/openfaas-storage-for-your-functions/
* Code -> https://github.com/alexellis/function-storage-example

## Summary
The pipeline consists of 2 functions:

`LoadImages`: Passed a JSON map of URLs, Download the images and puts them into an incoming bucket, Calls ProcessImages with the filenames and paths of the images

`ProcessImages`: Downloads the images from the bucket, Converts to black and white, Uploads to a new processed bucket