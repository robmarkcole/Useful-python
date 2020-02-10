## Pre-commit hooks
* `pip install pre-commit`
* https://pre-commit.com/
* Git hook scripts are useful for identifying simple issues before submission to code review. We run our hooks on every commit to automatically point out issues in code such as missing semicolons, trailing whitespace, and debug statements. 
* pre-commit will use a ``.pre-commit-config.yaml` file to make decisions about what to do at the various Git hook points, [see home assistant repo](https://github.com/home-assistant/home-assistant/blob/dev/.pre-commit-config.yaml)