# p4d app

djangobaseproject based app for A Puzzle in 4D

## what to do

* download gsheet [p4d_datamodel](https://docs.google.com/spreadsheets/d/1YlB8YmSyw7Cv9ll_Wkbe-4b4z42kQPMZqP0DE8dwCdc/edit#gid=0)
* save into data directory
* run something like

```python

from webpage.appcreator import creator

file = "data/p4d_datamodel.xlsx"

dicts = [x for x in creator.xlsx_to_classdicts(file)]

creator.serialize_data_model(dicts, app_name="archiv")

```

* create an app called `archiv`:  `python manage.py startapp archiv`

copy the content of `output_model.py` (should be created by the script above) into `archiv.models.py`

* do the same with the remaining function defined in `webpage.appcreator.creator` to create views, urls, tables, filters and forms
