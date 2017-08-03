import os
from django.contrib.gis.utils import LayerMapping
from .models import Stratunit

# Auto-generated `LayerMapping` dictionary for stratunit model
stratunit_mapping = {
    'objectid': 'OBJECTID',
    'type': 'Type',
    'gis_su_id': 'GIS_SU_ID',
    'excavation': 'Excavation',
    'stratum_id': 'Stratum_ID',
    'stratum_gi': 'Stratum_GI',
    'phase_id': 'Phase_ID',
    'phase_gis_field': 'Phase_GIS_',
    'locus_id': 'Locus_ID',
    'archaeolog': 'Archaeolog',
    'archaeol_1': 'Archaeol_1',
    'archaeol_2': 'archaeol_2',
    'height_top': 'Height_top',
    'height_t_1': 'height_t_1',
    'height_bot': 'Height_bot',
    'height_b_1': 'Height_b_1',
    'extrusion': 'Extrusion',
    'base_heigh': 'base_heigh',
    'eigner_map': 'Eigner_map',
    'resources_field': 'resources_',
    'pit_fill': 'pit_fill',
    'pit_find_g': 'pit_find_G',
    'bp_materia': 'bp_materia',
    'bp_door_st': 'bp_door_st',
    'bp_door_1': 'bp_door__1',
    'wall_type': 'wall_type',
    'wall_brick': 'wall_brick',
    'wall_inter': 'wall_inter',
    'wall_bri_1': 'wall_bri_1',
    'locus_laye': 'locus_laye',
    'shape_clas': 'Shape_clas',
    'orientatio': 'Orientatio',
    'stratum': 'Stratum',
    'phase': 'Phase',
    'wall_funct': 'wall_funct',
    'su_nummer': 'SU_Nummer',
    'wall_conne': 'wall_conne',
    'old_object': 'old_object',
    'shape_leng': 'SHAPE_Leng',
    'shape_area': 'SHAPE_Area',
    'geom': 'MULTIPOLYGON',
}

stratunit_shp = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 'data', 'j21', 'TD_F-I_j21', 'TED_GDB_qgis2shp', 'stratunits',
        'stratunits.shp'
    ),
)


def run(verbose=True):
    lm = LayerMapping(
        Stratunit, stratunit_shp, stratunit_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)
