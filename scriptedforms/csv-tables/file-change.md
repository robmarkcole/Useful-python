<!-- markdownlint-disable MD033 -->

# An example of the file change section

<variable-table>from_csv</variable-table>

<section-filechange paths="['input.csv']">

```python
from_csv = pd.read_csv('input.csv', index_col=0)
from_csv
```

</section-filechange>
