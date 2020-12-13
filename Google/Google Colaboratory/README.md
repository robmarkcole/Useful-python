## Colab
* See https://colab.research.google.com/
* Read https://medium.com/deep-learning-turkey/google-colab-free-gpu-tutorial-e113627b9f5d
* My own repo https://github.com/robmarkcole/robins-google-colaboratory
* Chrome extension https://chrome.google.com/webstore/detail/open-in-colab/iogfkhleblhcpcekbiedikdehleodpjo?hl=en
* Integrate with Google Drive -> share large files via drive and work on them collaboratively.
* Access to a GPU for deep learning and easily import Keras, TensorFlow, PyTorch, and OpenCV.
* Connect to a local runtime so you can keep your files local -> https://research.google.com/colaboratory/local-runtimes.html

## Expose over internet
* https://imadelhanafi.com/posts/google_colal_server/
* https://github.com/robmarkcole/pytorch-serve-from-colab

* https://stackoverflow.com/questions/59508225/is-it-possible-to-connect-vscode-on-a-local-machine-with-google-colab-the-fre

```
# Install jupyterlab and ngrok
!pip install jupyterlab pyngrok -q

# Run jupyterlab in background
!nohup jupyter lab --ip=0.0.0.0 &

# Make jupyterlab accessible via ngrok
from pyngrok import ngrok
print(ngrok.connect(8888))
```