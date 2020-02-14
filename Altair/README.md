## Altair
* https://altair-viz.github.io
* Altair is a declarative statistical visualization library for Python, based on Vega and Vega-Lite.
* Data in Altair is built around the Pandas Dataframe. 
* Once you have visualized your data, perhaps you would like to publish it somewhere on the web. This can be done straightforwardly using the Vega-Embed javascript package
* May not be suitable for plotting large amounts of data - defaults to limit to 5000 rows

## Tips
* `chart.save('mychart.html')`` will save the chart to HTML. At that point you can email the file to someone, or post it on a website.

## Vega-lite
* https://vega.github.io/vega-lite/
* Vega-Lite enables concise descriptions of visualizations as a set of encodings that map data fields to the properties of graphical marks. Vega-Lite uses a portable JSON format that compiles to full specifications in the larger Vega language.
* [Supported in Kibana](https://www.elastic.co/blog/getting-started-with-vega-visualizations-in-kibana)

## altair_data_server
* https://github.com/altair-viz/altair_data_server
* [It is also possible](https://altair-viz.github.io/user_guide/faq.html#local-data-server) to serve your data from a local threaded server to avoid writing datasets to disk. Note that this approach may not work on some cloud-based Jupyter notebook services.

## Altair-viewer
* https://github.com/altair-viz/altair_viewer/
* Plots launched in seperate window

## Grammar of graphics
* TLDR: a structured way of describing a plot
* [Read](https://towardsdatascience.com/a-comprehensive-guide-to-the-grammar-of-graphics-for-effective-visualization-of-multi-dimensional-1f92b4ed4149)