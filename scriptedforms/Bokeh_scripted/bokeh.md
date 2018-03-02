<!-- markdownlint-disable MD033 -->

# A Bokeh Plot

<section-start api="start">
```python
from bokeh.plotting import figure, output_file, output_notebook, show
# prepare some data
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]
# output to static HTML file
# output_file("lines.html")
output_notebook()
```
</section-start>


Below is a `<section-live>` containing a bokeh plot.

<section-live>
```python
# create a new plot with a title and axis labels
p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')
# add a line renderer with legend and line thickness
p.line(x, y, legend="Temp.", line_width=2)
# show the results
show(p)
```
</section-live>
