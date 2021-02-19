## Streamlit
* https://streamlit.io/
* https://awesome-streamlit.org/
* To run demo -> `streamlit hello`
* Streamlit is a Python app framework built specifically for Machine Learning and Data Science teams. Install Streamlit, import it, write a few lines of code, and run your script. Streamlit watches for changes on each save and updates automatically, visualizing your output while you’re coding. Code runs from top to bottom, always from a clean state, and with no need for callbacks. It’s a simple and powerful app model that lets you build rich UIs incredibly quickly. 

## `st.write()` 
Text, data, Matplotlib figures, Altair charts, and more. Don’t worry, Streamlit will figure it out and render things the right way. There are other data specific functions like `st.dataframe()` and `st.table()` that you can also use for displaying data.

## `st.line_chart` and `st.area_chart`
* https://streamlit.io/docs/api.html#display-charts
* Altair, Bokeh, Plotly, Matplotlib 

## `st.progess()`
When adding long running computations to an app, you can use st.progess() to display status in real time.

## Docker deploy
* [Read](https://maelfabien.github.io/project/Streamlit/#)
* Simple example -> https://github.com/Ashton-Sidhu/toot

## RPi installation
* Had fo `sudo apt-get install libatlas-base-dev` but then was able to run streamlit on rpi

## streamlit-launchpad
* [streamlit-launchpad](https://github.com/ideonate/streamlit-launchpad)
* Browse a folder containing multiple streamlit apps and launch them immediately 

## Example repos
* https://github.com/madewithml/e2e-ml-app-pytorch -> end-to-end ML pipeline with PyTorch, W&B, FastAPI, Docker, Streamlit and Heroku. 
* https://github.com/robmarkcole/streamlit_forecasting_app
* https://github.com/MarcSkovMadsen/awesome-streamlit
* https://github.com/JAVI897/ML-Metrics
* https://github.com/arvkevi/nba-roster-turnover
* CNN app -> https://towardsdatascience.com/full-stack-ai-building-a-ui-for-your-latest-ai-project-in-no-time-at-all-7e5c8fd4eafd
* [Include bokeh plots and deploy on Heroku](https://pythonforundergradengineers.com/streamlit-app-with-bokeh.html)
* [Regression app](https://github.com/andfanilo/regression-streamlit-viz)
* [Corona virus model](https://github.com/archydeberker/corona-calculator)
* [pymedphys](https://discuss.streamlit.io/t/an-example-deployed-streamlit-app-pymedphys/2681?u=randyzwitch)
* [Schelling Segregation Model](http://adilmoujahid.com/posts/2020/05/streamlit-python-schelling/)
* [NLP app Insight using fastAPI](https://github.com/abhimishra91/insight)

## Deployment
* https://discuss.streamlit.io/t/streamlit-deployment-guide-wiki/5099
* [Using Streamlit + Nginx + Docker to build and put in production dashboards in AWS Lightsail](https://medium.com/@dasirra/using-streamlit-nginx-docker-to-build-and-put-in-production-dashboards-in-aws-lightsail-781dab8f2836)
* [A minimal example of how to use streamlit on Heroku](https://github.com/ericmjl/minimal-streamlit-example)
* https://discuss.streamlit.io/t/deployment-on-aws-with-authentication/4073 with example [sagemaker-explaining-credit-decisions](https://github.com/awslabs/sagemaker-explaining-credit-decisions)
* [Via EC2](https://blog.jcharistech.com/2019/10/29/how-to-deploy-streamlit-apps-on-aws-ec2/)
* Via docker and [beanstalk (not working?)](https://discuss.streamlit.io/t/deploying-streamlit-app-to-aws-beanstalk-using-docker/1493/4)
* https://github.com/davidefiocco/streamlit-fastapi-model-serving
* https://hersanyagci.medium.com/model-deployment-with-streamlit-on-aws-ec2-f52ab42d7813

## Streamlit vs alternatives
* [Good article comparing streamlit to voila & panel](https://ericmjl.github.io/essays-on-data-science/miscellaneous/dashboarding-landscape/)
* `Streamlit uses a procedural paradigm, rather than a callback paradigm, for app construction. We just have to think of the app as a linear sequence of actions that happen from top to bottom. State is never really an issue, because every code change and interaction re-runs the source file from top to bottom, from scratch. When building quick apps, this paradigm really simplifies things compared to a callback-based paradigm.`