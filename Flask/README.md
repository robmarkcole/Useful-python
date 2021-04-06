## Flask
* https://palletsprojects.com/p/flask/
* Whilst FastAPI is gaining a lot of popularity, flask remains very popular

## Plotting
* Read https://towardsdatascience.com/python-plotting-api-expose-your-scientific-python-plots-through-a-flask-api-31ec7555c4a8
* Trick is to have a function that returns a matplotlib image as bytes, then return that with flas:

```python
def my_plot():
    .
    .
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image

# Then in my flask app
@app.route('/plots/breast_cancer_data/correlation_matrix', methods=['GET'])
def correlation_matrix():
    bytes_obj = do_plot()
    return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')
```

## Flask serve over internet
* https://github.com/gstaff/flask-ngrok

## Dev in VScode
* Can develop in docker container -> https://github.com/microsoft/vscode-remote-try-python

## General
* [Running background tasks with celery](https://danidee10.github.io/2016/11/28/flask-by-example-9.html)
* [example-oauth2-server](https://github.com/authlib/example-oauth2-server)
* [Flask webapp for inference](https://github.com/pycaret/pycaret-deployment-aws/blob/master/app.py) shown [here](https://towardsdatascience.com/deploy-machine-learning-pipeline-on-aws-fargate-eb6e1c50507)
* [Image Recommendations with PyTorch + Flask + PostgreSQL + Heroku deployment](https://towardsdatascience.com/image-recommendations-with-pytorch-flask-postgresql-heroku-deployment-206682d06c6b) with [code](https://github.com/MathMagicx/MediumFlaskImageRecommender)