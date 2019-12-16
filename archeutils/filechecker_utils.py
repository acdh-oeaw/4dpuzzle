import json
import pandas as pd


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
