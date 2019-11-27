## Tensorflow-serving
* GPRC and Rest API
* https://www.tensorflow.org/tfx/serving/api_rest
* Serve via docker - [resnet example](https://medium.com/tensorflow/serving-ml-quickly-with-tensorflow-serving-and-docker-7df7094aa008)
* https://github.com/fpaupier/tensorflow-serving_sidecar -> deploy on GCP

## Precit

Predict API (omitting optional `/versions/${MODEL_VERSION}`):

```
POST http://host:port/v1/models/${MODEL_NAME}/:predict
```

The body must be of form:

```
{
  // (Optional) Serving signature to use.
  // If unspecifed default serving signature is used.
  "signature_name": <string>,

  // Input Tensors in row ("instances") or columnar ("inputs") format.
  // A request can have either of them but NOT both.
  "instances": <value>|<(nested)list>|<list-of-objects>
  "inputs": <value>|<(nested)list>|<object>
}
 ```
    
Response format:
```
{
  "predictions": <value>|<(nested)list>|<list-of-objects>
}
```

## Encoding binary values

JSON uses UTF-8 encoding. If you have input feature or tensor values that need to be binary (like image bytes), you must Base64 encode the data and encapsulate it in a JSON object having b64 as the key as follows:
```
{ "b64": <base64 encoded string> }
```

A classification request with image (binary data) and caption features is shown below:
```
{
  "signature_name": "classify_objects",
  "examples": [
    {
      "image": { "b64": "aW1hZ2UgYnl0ZXM=" },
      "caption": "seaside"
    },
    {
      "image": { "b64": "YXdlc29tZSBpbWFnZSBieXRlcw==" },
      "caption": "mountains"
    }
  ]
}
```
    
  