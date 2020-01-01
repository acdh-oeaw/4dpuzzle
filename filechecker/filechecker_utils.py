import json
import pandas as pd

from django.contrib.contenttypes.models import ContentType

from archeutils.utils import ARCHE_BASE_URI, ARCHE_PREFIX_REMOVE


def remove_trailing_slash(string):
    if string.endswith('/'):
        return string[:-1]
    else:
        return string


def filename_to_arche_id(
    filename,
    pre_remove=ARCHE_PREFIX_REMOVE,
    pre_add=ARCHE_BASE_URI
):
    if pre_add.endswith('/'):
        pass
    else:
        pre_add = f"{pre_add}/"
    filename = filename.replace(pre_remove, '')
    filename = f"{pre_add}{filename}"
    return filename.replace(pre_remove, pre_add)


def filechecker_to_df(filelist_json):
    """reads a fileList.json and returns a pandas DataFrame
        :param filelist_json": The path to the fileList.json
        :return: A pandas DataFrame
    """
    file = filelist_json
    data = json.load(open(file, "r", encoding="utf-8"))
    df = pd.DataFrame(data['data'])
    return df


def find_matching_objects(model_list, matching_chars, matching_prop="legacy_id"):
    """ find first matching object from a list of classes
        :param model_list: A list of models to search through
        :param matching_chars: A sequence of chars which needs\
        to be identical to the value of the field
        :param matching_prop: The object's properties which value should match
        return: the matching object or None
    """
    leg_id = matching_chars
    all_qs = []
    for x in model_list:
        kwargs = {
            matching_prop: matching_chars
        }
        qs = x.objects.filter(**kwargs)
        if not qs:
            continue
        else:
            all_qs.append(*qs)
        if len(all_qs) == 1:
            return all_qs[0]
        else:
            return None


def path2cols(
    path, separator="/", app_label="filechecker", model="FcCollection"
):
    """takes a splittable string and creates nested collections"""
    counter = 1
    current = 0
    ct = ContentType.objects.get(
        app_label=app_label, model=model.lower()
    ).model_class()
    cols = []
    path_parts = path.split(separator)
    path_length = len(path_parts)
    prefix = path_length
    for x in reversed(path_parts):
        col_title = '/'.join(path_parts[0:prefix])
        col, _ = ct.objects.get_or_create(
            fc_fullname=col_title
        )
        cols.append(col)
        prefix = prefix - 1
        if prefix == 0:
            continue
    while counter != len(cols):
        current_col = cols[current]
        parent_col = cols[counter]
        current_col.parent = parent_col
        current_col.save()
        counter += 1
        current += 1
    return cols
