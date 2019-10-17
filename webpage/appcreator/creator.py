import ast
import pandas as pd
from jinja2 import Template
from . import code_templates


def xlsx_to_classdicts(file):
    """
    parses an Excel sheet and yields dicts of model definitions
    :param file: path to an Excel sheet
    :return: yields dicts
    """
    df = pd.read_excel(file)
    classes = df.groupby('class name technical')
    for x in classes:
        local_df = x[1]
        class_dict = {}
        class_dict['model_name'] = x[0]
        class_dict['model_helptext'] = x[1]['class name helptext'].iloc[0]
        class_dict['model_verbose_name'] = x[1]['class name verbose_name'].iloc[0]
        class_dict['model_representation'] = "{}".format(
            x[1]['class self representation'].iloc[0]
        )
        class_dict['model_order'] = "{}".format(
            x[1]['class object order by field'].iloc[0]
        )
        class_dict['model_fields'] = []
        for i, row in local_df.iterrows():
            org_field_name = row['field name technical'].lower().replace('/', '_').replace('|', '_')
            org_field_name = org_field_name.replace('__', '_')
            if org_field_name[0].isdigit():
                org_field_name = f"xx_{org_field_name}"
            field_name = org_field_name.replace('-', '_').replace('\n', '').replace(' ', '')
            if isinstance(field_name, str) and isinstance(row['field type'], str):
                field = {}
                field['field_name'] = field_name
                if ' ' in row['field type'].strip():
                    continue
                if '|' in row['field type']:
                    field_type = row['field type'].split('|')[0]
                    if field_type == 'FK':
                        field['field_type'] = 'ForeignKey'
                    else:
                        field['field_type'] = 'ManyToManyField'
                    field['related_class'] = row['field type'].split('|')[1].split(':')[0]
                    temp_related_name = "rvn_{}_{}_{}".format(
                        x[0].lower(),
                        field_name,
                        field['related_class'].lower()
                    ).replace('__', '_')
                    field['related_name'] = temp_related_name
                elif row['field type'] == "URI":
                    field['field_type'] = "CharField"
                elif row['field type'].startswith('Integ'):
                    field['field_type'] = "IntegerField"
                elif row['field type'].startswith('TextF'):
                    field['field_type'] = "TextField"
                elif row['field type'].startswith('DateR'):
                    field['field_type'] = "DateRangeField"
                elif row['field type'].startswith('Date'):
                    field['field_type'] = "DateField"
                elif row['field type'] == "Boolean":
                    field['field_type'] = "BooleanField"
                elif row['field type'] == "CharField":
                    field['field_type'] = "CharField"
                elif row['field type'] == "ChoiceField":
                    if isinstance(row['choices'], str):
                        field['choices'] = ast.literal_eval(row['choices'])
                    field['field_type'] = "CharField"
                else:
                    continue
                if isinstance(row['verbose field name'], str):
                    field['field_verbose_name'] = row['verbose field name']
                else:
                    field['field_verbose_name'] = field_name
                if isinstance(row['helptext'], str):
                    field['field_helptext'] = row['helptext']
                else:
                    field['field_helptext'] = f"helptext for {field_name}"

                class_dict['model_fields'].append(field)
        yield class_dict


def serialize_data_model(dicts, app_name="my_app", file_name='output_model.py'):
    t = Template(code_templates.MODELS_PY)
    output = t.render(
        data=dicts,
        app_name=app_name
    )
    with open(file_name, "w") as text_file:
        print(output, file=text_file)
    return file_name


def serialize_admin(dicts, app_name="my_app", file_name='output_admin.py'):
    t = Template(code_templates.ADMIN_PY)
    output = t.render(
        data=dicts,
        app_name=app_name
    )
    with open(file_name, "w") as text_file:
        print(output, file=text_file)
    return file_name


def serialize_tables(dicts, app_name="my_app", file_name='output_tables.py'):
    t = Template(code_templates.TABLES_PY)
    output = t.render(
        data=dicts,
        app_name=app_name
    )
    with open(file_name, "w") as text_file:
        print(output, file=text_file)
    return file_name


def serialize_views(dicts, app_name="my_app", file_name='output_views.py'):
    t = Template(code_templates.VIEWS_PY)
    output = t.render(
        data=dicts,
        app_name=app_name
    )
    with open(file_name, "w") as text_file:
        print(output, file=text_file)
    return file_name


def serialize_forms(dicts, app_name="my_app", file_name='output_forms.py'):
    t = Template(code_templates.FORMS_PY)
    output = t.render(
        data=dicts,
        app_name=app_name
    )
    with open(file_name, "w") as text_file:
        print(output, file=text_file)
    return file_name


def serialize_filters(dicts, app_name="my_app", file_name='output_filters.py'):
    t = Template(code_templates.FILTERS_PY)
    output = t.render(
        data=dicts,
        app_name=app_name
    )
    with open(file_name, "w") as text_file:
        print(output, file=text_file)
    return file_name


def serialize_urls(dicts, app_name="my_app", file_name='output_urls.py'):
    t = Template(code_templates.URLS_PY)
    output = t.render(
        data=dicts,
        app_name=app_name
    )
    with open(file_name, "w") as text_file:
        print(output, file=text_file)
    return file_name
