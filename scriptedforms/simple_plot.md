<!-- markdownlint-disable MD033 -->

# A Demo Plot

<section-start api="start">
```python
x = np.linspace(0, 2 * np.pi, 1e3)
wavelength_a = 1.0
wavelength_b = 1.0
y = np.sin(wavelength_a * x) + np.sin(wavelength_b * x)
```
</section-start>


Below is a `<section-live>` containing a `<variable-slider>` element. 

<section-live>
<variable-slider min="0" max="30" step="0.1">wavelength_a</variable-slider>
<variable-slider min="0" max="30" step="0.1">wavelength_b</variable-slider>

```python
y = np.sin(wavelength_a * x) + np.sin(wavelength_b * x)
plt.plot(x, y);
```
</section-live>

