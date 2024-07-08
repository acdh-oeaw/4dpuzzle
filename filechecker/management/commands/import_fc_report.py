import warnings

from django.core.management.base import BaseCommand, CommandError

from archeutils.utils import ARCHE_PREFIX_REMOVE

from filechecker.filechecker_utils import (
    filechecker_to_df,
    filename_to_arche_id,
    remove_trailing_slash,
    path2cols,
)
from filechecker.models import FcCollection, FcResource

file = r"fileList.json"
warnings.filterwarnings("ignore")


class Command(BaseCommand):

    help = "Import a fileList.json from located in the project's root directory"

    def add_arguments(self, parser):
        parser.add_argument(
            "file", type=str, default="fileList.json", help="Path to fileList"
        )

    def handle(self, *args, **kwargs):
        file = kwargs["file"]
        df = filechecker_to_df(file)
        all_dirs = len(df.groupby("directory"))
        counter = 0
        for gr in df.groupby("directory"):
            col_fullname = f"{gr[0]}"
            col_fullname = remove_trailing_slash(
                col_fullname.replace(ARCHE_PREFIX_REMOVE, "")
            )
            counter += 1
            if len(col_fullname) > 0:
                print(
                    f"Import {len(gr[1])} resources from directory: {col_fullname} {counter}/{all_dirs}"
                )
                fc_col, _ = FcCollection.objects.get_or_create(fc_fullname=col_fullname)
                fc_col.fc_items = len(gr[1])
                fc_col.fc_size = gr[1].sum(axis=0, skipna=True)["size"]
                fc_col.fc_lastmod = (
                    gr[1]
                    .sort_values(by=["lastmod"], ascending=False)["lastmod"]
                    .iloc[0]
                )
                fc_col.fc_firstmod = (
                    gr[1].sort_values(by=["lastmod"], ascending=True)["lastmod"].iloc[0]
                )
                fc_col.save()
                try:
                    path2cols(col_fullname)
                except Exception as e:
                    print(f"failed by {col_fullname} because of {e}")
                for i, row in gr[1].iterrows():
                    res, _ = FcResource.objects.get_or_create(
                        fc_fullname=f"{row['name']}"
                    )
                    res.fc_filename = f"{row['filename']}"
                    res.fc_lastmod = row.lastmod
                    res.fc_size = row["size"]
                    res.fc_directory = fc_col
                    res.fc_type = row["type"]
                    res.fc_extension = row["extension"]
                    res.save()
            else:
                print(f"skipped {col_fullname}")
