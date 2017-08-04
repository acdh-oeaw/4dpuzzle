import os
from django.contrib.gis.utils import LayerMapping
from .models import Find, Brick, Stratunit

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


def run_finds(verbose=True):
    lm = LayerMapping(
        Find, finds_shp, find_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)


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
        os.path.dirname(__file__), 'data', 'shapes', 'stratunits.shp'
    ),
)


def run_strat(verbose=True):
    lm = LayerMapping(
        Stratunit, stratunit_shp, stratunit_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)

# Auto-generated `LayerMapping` dictionary for Bricks model
brick_mapping = {
    'objectid': 'OBJECTID',
    'gisbrick_i': 'GISbrick_I',
    'excavation': 'Excavation',
    'stratum_id': 'Stratum_ID',
    'stratum_gi': 'Stratum_GI',
    'phase_id': 'Phase_ID',
    'phase_gis_field': 'Phase_GIS_',
    'archaeolog': 'Archaeolog',
    'archaeol_1': 'Archaeol_1',
    'archaeol_2': 'Archaeol_2',
    'gis_su_id': 'GIS_SU_ID',
    'gis_locus_field': 'GIS_locus_',
    'brick_type': 'brick_type',
    'brick_mate': 'brick_mate',
    'height_max': 'Height_max',
    'extrusion': 'Extrusion',
    'orientatio': 'Orientatio',
    'resource_i': 'Resource_I',
    'base_heigh': 'base_heigh',
    'shape_leng': 'SHAPE_Leng',
    'shape_area': 'SHAPE_Area',
    'geom': 'MULTIPOLYGON',
}

bricks_shp = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 'data', 'shapes',
        'bricks.shp'
    ),
)


def run_brick(verbose=True):
    lm = LayerMapping(
        Brick, bricks_shp, brick_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)
