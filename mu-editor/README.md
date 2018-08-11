* https://github.com/mu-editor/mu/tree/master/mu
* `$ pip3 install mu_editor --upgrade`
* `$ mu-editor`
* Plotting example https://codewith.mu/en/tutorials/1.0/plotter

```python
import time
import random

while True:
    # Just keep emitting three random numbers in a Python tuple.
    time.sleep(0.05)
    print((random.randint(0, 100), random.randint(-100, 0), random.randint(-50, 50)))
```