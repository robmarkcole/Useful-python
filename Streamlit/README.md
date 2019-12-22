## Streamlit
* https://streamlit.io/
* https://streamlit.io/docs/
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

## Example repos
* https://github.com/MarcSkovMadsen/awesome-streamlit
* https://github.com/JAVI897/ML-Metrics
* https://github.com/arvkevi/nba-roster-turnover
* CNN app -> https://towardsdatascience.com/full-stack-ai-building-a-ui-for-your-latest-ai-project-in-no-time-at-all-7e5c8fd4eafd
* [A minimal example of how to use streamlit on Heroku](https://github.com/ericmjl/minimal-streamlit-example)
* [Include bokeh plots and deploy on Heroku](https://pythonforundergradengineers.com/streamlit-app-with-bokeh.html)

## Streamlit vs alternatives
* [Good article comparing streamlit to voila & panel](https://ericmjl.github.io/essays-on-data-science/miscellaneous/dashboarding-landscape/)
* `Streamlit uses a procedural paradigm, rather than a callback paradigm, for app construction. We just have to think of the app as a linear sequence of actions that happen from top to bottom. State is never really an issue, because every code change and interaction re-runs the source file from top to bottom, from scratch. When building quick apps, this paradigm really simplifies things compared to a callback-based paradigm.`