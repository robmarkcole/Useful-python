<!-- markdownlint-disable MD033 -->

# A Complex Plot

<section-start api="start">
```python
dummy = 0
```
</section-start>


Below is a `<section-live>` containing a `<variable-slider>` element. 

<section-live>
<variable-slider>dummy</variable-slider>

```python
a = dummy
A = np.random.rand(5, 5)

fig, axs = plt.subplots(1, 3, figsize=(10, 3))
for ax, interp in zip(axs, ['nearest', 'bilinear', 'bicubic']):
    ax.imshow(A, interpolation=interp)
    ax.set_title(interp.capitalize())
    ax.grid(True)

plt.show()
```
</section-live>

