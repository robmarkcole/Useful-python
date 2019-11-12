## Plotly
* https://github.com/plotly/plotly.py -> follow all the jupyterlab specific install instructions or plots won't render in notebooks
* Read -> https://towardsdatascience.com/introduction-to-interactive-time-series-visualizations-with-plotly-in-python-d3219eb7a7af
* Online mode -> Free plotly account which gives you 25 public charts and 1 private chart. API key required for online mode. 
* Offline mode -> Key not required if running in offline mode -> https://plot.ly/python/offline/ -> `init_notebook_mode(connected=False)`
* When we make a plotly online graph, it’s published online by default which makes sharing visualizations easy -> https://plot.ly/feed/#/
* Chart editor to improve look of plots -> https://github.com/plotly/jupyterlab-chart-editor

## Plotly Express (use for rapid plotting)
* https://plot.ly/python/plotly-express/
* Intro post -> https://medium.com/plotly/introducing-plotly-express-808df010143d
* TLDR: a less verbose API than full plotly that exposes a simple syntax for complex charts. Takes a “tidy” data frame as input

## Dash
* Gallery -> https://dash-gallery.plotly.host/Portal/
* Dash is a platform for building analytical web applications. No JavaScript required.
* The dash-canvas component library of Dash (https://dash.plot.ly/canvas) is an interactive component for annotating images with several tools (freehand brush, lines, bounding boxes, ...). See examples -> https://dash-canvas.plotly.host/Portal/

## References
* On "tidy" data -> http://www.jeannicholashould.com/tidy-data-in-python.html