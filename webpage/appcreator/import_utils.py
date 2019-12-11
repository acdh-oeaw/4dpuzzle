import glob
import json

from django.core.serializers.json import DjangoJSONEncoder

from django.apps import apps
from django.core.exceptions import FieldDoesNotExist

from pandas import pandas as pd
from . populate_fields import *


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


def run_import(app_name, format_string, glob_pattern, m2m_sep="|", date_range_sep="/", limit=False):
    """ runs data import from a collection of excel-files matching the model class of the
        passed in applications
        :param app_name: name of the application
        :paramformat_string: a python format string 'someprefix{classname}somesuffix' used to map
        class names to files names matching your glob pattern.
        :param glob_pattern: a glob pattern matching the Excel files you'd like to immport
        :param m2m_sep: Character used in your data to separate values in a cell, defaults to '|'
        :param date_range_sep: Character used in your data to separate date ranges in a cell,
        defaults to '|'
        :param limit: The number of rows which should be imported, defaults to 'False', meaning all
        rows of each spreadsheet will be imported.
        :return: prints the name of the spraedsheet which is currently imported
        the populated database
    """
    file_class_map = create_file_class_map(app_name, format_string, glob_pattern)
    for current_class in fetch_models('archiv'):
        model_name = current_class.__name__
        try:
            source_file = file_class_map[current_class.__name__]
        except KeyError:
            continue
        try:
            df_data = pd.read_excel(source_file)
            print(source_file)
        except FileNotFoundError:
            df_data = False
            continue
        if isinstance(df_data, pd.DataFrame):
            df_data.columns = map(str.lower, df_data.columns)
            df_keys = df_data.keys()
            nr_cols = len(df_keys)
            if limit:
                df_data = df_data.head(limit)
            for i, row in df_data.iterrows():
                temp_item, _ = current_class.objects.get_or_create(legacy_id=f"{row[0]}".lower().strip())
                row_data = f"{json.dumps(row.to_dict(), cls=DjangoJSONEncoder)}"
                temp_item.orig_data_csv = row_data
                col_counter = 0
                while col_counter < nr_cols:
                    cur_attr = df_keys[col_counter]
                    try:
                        cur_attr_type = current_class._meta.get_field(
                            df_keys[col_counter]
                        ).get_internal_type()
                    except FieldDoesNotExist:
                        cur_attr_type = None
                    if cur_attr_type is not None:

                        if "{}".format(cur_attr_type) == "CharField":
                            pop_char_field(temp_item, row, cur_attr, max_length=249)

                        elif "{}".format(cur_attr_type) == "TextField" and isinstance(
                            row[cur_attr], str
                        ):
                            pop_text_field(temp_item, row, cur_attr)

                        elif "{}".format(cur_attr_type) == "ForeignKey" and isinstance(
                            row[cur_attr], str
                        ):
                            pop_fk_field(current_class, temp_item, row, cur_attr)

                        elif "{}".format(cur_attr_type) == "ManyToManyField" and isinstance(
                            row[cur_attr], str
                        ):
                            pop_m2m_field(current_class, temp_item, row, cur_attr, sep=m2m_sep)

                        elif "{}".format(cur_attr_type) == "DateField":
                            pop_date_field(temp_item, row, cur_attr)

                        elif "{}".format(cur_attr_type) == "DateRangeField":
                            pop_date_range_field(temp_item, row, cur_attr, sep=date_range_sep)
                        else:
                            pass
                    try:
                        temp_item.save()
                    except Exception as e:
                        print(e)
                    col_counter += 1


def delete_all(app_name):
    """ deletes all objects from passed in app
        :param app_name: the app to delte all model class objects from
    """
    all_models = all_models = fetch_models(app_name)
    for x in all_models:
        for y in x.objects.all():
            y.delete()
