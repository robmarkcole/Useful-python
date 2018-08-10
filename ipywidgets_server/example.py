# example.py

from ipywidgets import IntSlider, Text, VBox
s = IntSlider(max=200, value=100)
t = Text()

def update_text(change=None):
    t.value = str(float(s.value) ** 2)

s.observe(update_text, names='value')
update_text()
vbox = VBox([s, t])