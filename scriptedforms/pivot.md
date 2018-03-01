<!-- markdownlint-disable MD033 -->

# A Demo of tables and pivot
section-start is run once on startup

<section-start api="start">
```python
table = pd.DataFrame({'foo': ['one','one','one','two','two','two'],
                       'bar': ['A', 'B', 'C', 'A', 'B', 'C'],
                       'baz': [1, 2, 3, 4, 5, 6]})
```
</section-start>

Table variables display a full pandas dataframe. The live code can update one
part of the table as other parts are being edited.

<section-live>
<variable-table>table</variable-table>
Lets show our raw table data.
```python
table
```

<variable-table>pivot</variable-table>
Now lets show the pivot table.
```python
pivot = table.pivot(index='foo', columns='bar', values='baz')
```
</section-live>

sales@lenoxlaser.com