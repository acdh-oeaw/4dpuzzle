# generated by appcreator
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset
from crispy_forms.bootstrap import Accordion, AccordionGroup

from .models import FcCollection, FcResource


class FcCollectionFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(FcCollectionFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.helper.form_tag = False
        self.add_input(Submit("Filter", "Search"))
        self.layout = Layout(
            Fieldset(
                "Basic search options",
                "id",
                "fc_fullname",
                "fc_name",
                css_id="basic_search_fields",
            ),
            Accordion(
                AccordionGroup(
                    "Advanced search",
                    "fc_ordername",
                    "fc_firstmod",
                    "fc_lastmod",
                    "fc_size",
                    "fc_items",
                    "parent",
                    "fc_arche_id",
                    "fc_arche_description",
                    "lft",
                    "rght",
                    "tree_id",
                    "level",
                    css_id="more",
                ),
            ),
        )


class FcCollectionForm(forms.ModelForm):
    class Meta:
        model = FcCollection
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(FcCollectionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3"
        self.helper.field_class = "col-md-9"
        self.helper.add_input(
            Submit("submit", "save"),
        )


class FcResourceFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(FcResourceFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.helper.form_tag = False
        self.add_input(Submit("Filter", "Search"))
        self.layout = Layout(
            Fieldset("Basic search options", "id", css_id="basic_search_fields"),
            Accordion(
                AccordionGroup(
                    "Advanced search",
                    "fc_fullname",
                    "fc_filename",
                    "fc_lastmod",
                    "fc_size",
                    "fc_directory",
                    "fc_type",
                    "fc_extension",
                    "fc_arche_cat",
                    "fc_arche_id",
                    "fc_arche_description",
                    css_id="more",
                ),
            ),
        )


class FcResourceForm(forms.ModelForm):
    class Meta:
        model = FcResource
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(FcResourceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3"
        self.helper.field_class = "col-md-9"
        self.helper.add_input(
            Submit("submit", "save"),
        )
