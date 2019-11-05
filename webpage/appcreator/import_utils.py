import datetime
import glob
from django.apps import apps
from dateutil.parser import parse
from pandas import pandas as pd
from vocabs.models import *


def fetch_models(app_name):
    """ returns all models from an app
        :param app_name: The name of the application you'd like to recieve the models from
        :return: A list of the app's model classes {app}.models.{ModelName}
    """
    all_models = [x for x in apps.all_models['archiv'].values() if '_' not in x.__name__]
    return all_models


def create_file_class_map(app_name, format_string, glob_pattern):
    """ create a dictionary mapping model names to their spreadsheets
        (the spreadsheet must contain the model name)
        :param app_name: The name of the app you'd like to work with
        :format string: A python format string with one placeholder for the actual class name
        :glob_pattern: A python glob pattern matching the files you'd like to import data from
        :return: A dict where class names are keys and the full path to their matching files
    """
    all_models = fetch_models(app_name)
    files = glob.glob(glob_pattern)
    file_class_map = {}
    for cl in all_models:
        for file in files:
            con_file_name = format_string.format(cl.__name__).lower()
            if con_file_name in file.lower():
                file_class_map[cl.__name__] = file
    return file_class_map


def pop_char_field(temp_item, row, cur_attr, max_length=249):
    """ adds value to CharField on the current temp_item
        :param temp_item: a model class object
        :param row: A pandas DataFrame row with column names matching the items field names
        :param cur_attr: field name of the temp_item object
        :param max_length: The max_length of the current CharField of the object
        :return: The temp_item
    """
    try:
        my_val = f"{(row[cur_attr])[:max_length]}"
        setattr(temp_item, cur_attr, my_val)
    except TypeError:
        pass
    return temp_item


def pop_text_field(temp_item, row, cur_attr):
    """ adds value to TextField on the current temp_item
        :param temp_item: a model class object
        :param row: A pandas DataFrame row with column names matching the items field names
        :param cur_attr: field name of the temp_item object
        :return: The temp_item
    """
    try:
        my_val = f"{(row[cur_attr])}"
        setattr(temp_item, cur_attr, my_val)
    except TypeError:
        pass
    return temp_item


def pop_fk_field(current_class, temp_item, row, cur_attr):
    """ adds value to ForeignKey Field on the current temp_item
        :param current_class: a model class
        :param temp_item: a model class object
        :param row: A pandas DataFrame row with column names matching the items field names
        :param cur_attr: field name of the temp_item object
        :param cur_field: the index number of the current collection
        :return: The temp_item
    """
    fk = current_class._meta.get_field(cur_attr)
    rel_model_name = fk.related_model._meta.model_name
    temp_rel_obj, _ = fk.related_model.objects.get_or_create(legacy_id=row[cur_attr])
    if rel_model_name == 'skosconcept':
        temp_rel_obj.pref_label = row[cur_attr]
        col, _ = SkosCollection.objects.get_or_create(name=f"{row[cur_attr]}")
        temp_rel_obj.collection.add(col)
        temp_rel_obj.save()
    setattr(temp_item, cur_attr, temp_rel_obj)
    return temp_item


def pop_m2m_field(current_class, temp_item, row, cur_attr, sep='|'):
    """ adds value to ManyToMany Field on the current temp_item
        :param current_class: a model class
        :param temp_item: a model class object
        :param row: A pandas DataFrame row with column names matching the items field names
        :param cur_attr: field name of the temp_item object
        :param col_counter: the index number of the current collection
        :return: The temp_item
    """
    fk = current_class._meta.get_field(cur_attr)
    rel_model_name = fk.related_model._meta.model_name
    if rel_model_name == 'skosconcept':
        col, _ = SkosCollection.objects.get_or_create(name=f"{row[cur_attr]}")
        rel_things = []
        for x in row[cur_attr].split(sep):
            temp_rel_obj, _ = fk.related_model.objects.get_or_create(pref_label=x.strip())
            temp_rel_obj.collection.add(col)
            rel_things.append(temp_rel_obj)
        m2m_attr = getattr(temp_item, cur_attr)
        m2m_attr.set(rel_things)
    else:
        rel_things = []
        for x in row[cur_attr].split(sep):
            temp_rel_obj, _ = fk.related_model.objects.get_or_create(legacy_id=x.strip())
            rel_things.append(temp_rel_obj)
        m2m_attr = getattr(temp_item, cur_attr)
        m2m_attr.set(rel_things)
    return temp_item


def pop_date_field(temp_item, row, cur_attr):
    """ adds value to DateField on the current temp_item
        :param temp_item: a model class object
        :param row: A pandas DataFrame row with column names matching the items field names
        :param cur_attr: field name of the temp_item object
        :return: The temp_item
    """
    if isinstance(row[cur_attr], float):
        value = None
    if isinstance(row[cur_attr], int):
        value = parse(f"{row[cur_attr]}-01-01")
    elif isinstance(row[cur_attr], datetime.date):
        value = row[cur_attr]
    elif isinstance(row[cur_attr], str):
        try:
            value = parse(row[cur_attr])
        except Exception as e:
            print(f"{row[cur_attr]} for field: {cur_attr} could not be parsed, due to Error: {e}")
            value = None
    elif pd.isnull(row[cur_attr]):
        value = None
    if value is not None:
        setattr(temp_item, cur_attr, value)
    return temp_item


def pop_date_range_field(temp_item, row, cur_attr, sep="|"):
    """ adds value to DateRangeField on the current temp_item
        :param temp_item: a model class object
        :param row: A pandas DataFrame row with column names matching the items field names
        :param cur_attr: field name of the temp_item object
        :param sep: The separator used between start and end date
        :return: The temp_item
    """
    if pd.isnull(row[cur_attr]):
        return temp_item
    elif isinstance(row[cur_attr], str) and sep in row[cur_attr]:
        if len(row[cur_attr].split(sep)) == 2:
            start_date, end_date = row[cur_attr].split('/')
            try:
                valid_start = parse(start_date)
                valid_end = parse(end_date)
            except Exception as e:
                print(f"could not parse {start_date} or {end_date} due to: {e}")
                valid_end = None
            if valid_end is not None:
                setattr(temp_item, cur_attr, (start_date, end_date))
                return temp_item
        return temp_item
    else:
        return temp_item


def delete_all(app_name):
    """ deletes all objects from passed in app
        :param app_name: the app to delte all model class objects from
    """
    all_models = all_models = fetch_models(app_name)
    for x in all_models:
        for y in x.objects.all():
            y.delete()
