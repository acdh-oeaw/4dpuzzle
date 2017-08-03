# 4dpuzzle

for further info for the time being see: https://redmine.acdh.oeaw.ac.at/issues/9183

## issues with data quality

### messed up naming convention

TD_FZ_1000__TD_F-I_j21_Planum2 vs TD_FZ_1000__TD_F-I_j21_Planum_2, first are the actual file names, second the string found in gis_data for stratigraphic units

### missing information

```python
info = 0
no_info = 0
keine = 0
for x in Stratunit.objects.all():
    if x.resources_field.startswith('TD'):
        info += 1
    elif x.resources_field.startswith('ke'):
        keine += 1
    else:
        no_info += 1
print("info: {}".format(info))
print("no_info: {}".format(no_info))
print("keine: {}".format(keine))
```

results in:

```python
info: 323
no_info: 163
keine: 37
```
