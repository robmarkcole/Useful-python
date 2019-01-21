## Fast.ai course v3
* TLDR: deep learning course using the [fastai](https://docs.fast.ai/) package
* [fastai website](https://www.fast.ai/)
* Course (v3) dates: 2019 March 18 - April 30 (7 weeks)

Course components:
1. Seven [full video lessons](https://course.fast.ai/lessons/lessons.html) of a little over 2 hours each, plus two shorter introductory videos
2. A set of [detailed notebooks](https://github.com/fastai/course-v3) showing how to complete the steps demonstrated in each video.
3. The [forums](https://forums.fast.ai/), which should be your first step for asking questions not answered by the wiki or course notes.

## Free GPU - Colab
* Free GPU (shared, not always available), but some setup of the env required for each notebook, and need to make data available.
* [Getting started with Colab and fast.ai](https://course-v3.fast.ai/start_colab.html) -> a little bit of prep is required before using each notebook. Use the Github repo to get the latest course notebooks entering the source repo as `fastai/course-v3` and in the first cell of a notebook run `!curl https://course-v3.fast.ai/setup/colab | bash`
* TLDR - OK for initial tryout, bit frustrating to use seriously

## Paid GPU
* Overview of paid options -> https://course-v3.fast.ai/index.html
* I've been using Floydhub which has a nice ecosystem ($1.20/hour + $9.00/month (100GB storage)), but am now experimenting with Salamander as cheaper (tracks the AWS spot price +26%, K80: $0.36 per hour, storage min 40GB at $4 month, automatically bills $20 when you are low on credit).

### Salamander
* Recommend selecting 40GB storage option to keep costs low.
* Have to `pip install fastai` in terminal in the base env (note the `fastai` env is not kept up to date) 