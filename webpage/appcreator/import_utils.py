import glob
from django.apps import apps

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
        :param cur_attr: fieldname of the temp_item object
        :param max_length: The max_length of the current CharField of the object
        :return: The temp_item
    """
    try:
        my_val = f"{(row[cur_attr])[:max_length]}"
        setattr(temp_item, cur_attr, my_val)
    except TypeError:
        pass
    return temp_item


def pop_fk_field(current_class, temp_item, row, cur_attr, cur_field):
    """ adds value to ForeignKey Field on the current temp_item
        :param current_class: a model class
        :param temp_item: a model class object
        :param row: A pandas DataFrame row with column names matching the items field names
        :param cur_attr: fieldname of the temp_item object
        :param col_counter: the index number of the current collection
        :return: The temp_item
    """
    fk = current_class._meta.get_field(cur_field)
    rel_model_name = fk.related_model._meta.model_name
    temp_rel_obj, _ = fk.related_model.objects.get_or_create(legacy_id=row[cur_attr])
    if rel_model_name == 'skosconcept':
        temp_rel_obj.pref_label = row[cur_attr]
        col, _ = SkosCollection.objects.get_or_create(name=f"{cur_field}")
        temp_rel_obj.collection.add(col)
        temp_rel_obj.save()
    setattr(temp_item, cur_attr, temp_rel_obj)
    return temp_item


def delete_all(app_name):
    """ deletes all objects from passed in app
        :param app_name: the app to delte all model class objects from
    """
    all_models = all_models = fetch_models(app_name)
    for x in all_models:
        for y in x.objects.all():
            y.delete()
