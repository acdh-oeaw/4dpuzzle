import os
from django.contrib.gis.utils import LayerMapping
from .models import Find

# Auto-generated `LayerMapping` dictionary for Finds model
find_mapping = {
    'objectid': 'OBJECTID',
    'gisfind_id': 'GISfind_ID',
    'excavation': 'Excavation',
    'stratum_id': 'Stratum_ID',
    'stratum_gi': 'Stratum_GI',
    'phase_id': 'Phase_ID',
    'phase_gis_field': 'Phase_GIS_',
    'archaeolog': 'Archaeolog',
    'gis_locus_field': 'GIS_locus_',
    'gis_su_id': 'GIS_SU_ID',
    'gis_commen': 'GIS_commen',
    'find_mater': 'Find_mater',
    'find_type': 'Find_type',
    'height': 'Height',
    'find_inven': 'Find_inven',
    'find_local': 'Find_local',
    'eigner_map': 'Eigner_Map',
    'resource_i': 'resource_I',
    'geom': 'MULTIPOINT',
}


finds_shp = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 'data', 'shapes',
        'finds.shp'
    ),
)


def run(verbose=True):
    lm = LayerMapping(
        Find, finds_shp, find_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)
