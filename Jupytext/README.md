## Jupytext
* https://github.com/mwouts/jupytext
* To get meaningful diffs, we use Jupytext. Jupytext represents notebooks as Markdown files compatible with all major Markdown editors and viewers. The Markdown file does not include any output, just the code. The markdown file is automatically updated by when you save the notebook.
* In our version control system, we only need to track the Markdown file (and we even explicitly ignore all `.ipynb` files)
* [Automated reports with Jupyter Notebooks (using Jupytext and Papermill)](https://medium.com/capital-fund-management/automated-reports-with-jupyter-notebooks-using-jupytext-and-papermill-619e60c37330) -> use jupytext with papermill
* convert the executed notebook to HTML using nbconvert, and publish it on GitHub pages, or on your own HTML server, or send it over email