## Virtual Environments
* [Good overview article on stack overflow](https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe)
* I have python 3.7 installed via Anaconda
* I use the batteries included `venv` [following these instructions](https://developers.home-assistant.io/docs/en/development_environment.html) and have experimented with [pyenv](https://github.com/pyenv/pyenv) when different python versions are required
* On VScode you can [develop in Docker containers](https://code.visualstudio.com/docs/remote/containers), which is the ultimate isolation but has caused me issues in the past, such as when I had a dependency in a private repo and I needed to inject an SSH key into the container so it could access the repo
* One of my colleagues is loving [Poetry](https://github.com/sdispater/poetry)