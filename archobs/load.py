import os
from django.contrib.gis.utils import LayerMapping
from .models import *

findspot_mapping = {
    'objectid': 'OBJECTID',
    'orea_gis_i': 'OREA_GIS_I',
    'excavation': 'Excavation',
    'stratum_id': 'Stratum_ID',
    'stratum_gi': 'Stratum_GI',
    'phase_id': 'Phase_ID',
    'phase_gis_field': 'Phase_GIS_',
    'archaeolog': 'Archaeolog',
    'gis_commen': 'GIS_commen',
    'find_mater': 'Find_mater',
    'find_type': 'Find_type',
    'height': 'Height',
    'find_inven': 'Find_inven',
    'find_local': 'Find_local',
    'eigner_map': 'Eigner_Map',
    'comments': 'Comments',
    'resources_field': 'Resources_',
    'geom': 'MULTIPOINT',
}
findspot_shp = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 'data', 'shapes',
        'shp_fuer_ACDH', 'Findspots_20170928.shp'
    ),
)


def run_findspot(verbose=True):
    lm = LayerMapping(
        FindSpot, findspot_shp, findspot_mapping,
        transform=True, encoding='utf-8',
    )
    lm.save(strict=True, verbose=verbose)

find_mapping = {
    'objectid': 'OBJECTID',
    'orea_gis_i': 'OREA_GIS_I',
    'find_mater': 'Find_mater',
    'find_type': 'Find_type',
    'excavation': 'Excavation',
    'height': 'Height',
    'function': 'Function',
    'archaeolog': 'Archaeolog',
    'extrusion': 'Extrusion',
    'base_heigh': 'Base_heigh',
    'find_local': 'Find_local',
    'find_inven': 'Find_inven',
    'stratum_id': 'Stratum_ID',
    'stratum_gi': 'Stratum_GI',
    'phase_id': 'Phase_ID',
    'phase_gis_field': 'Phase_GIS_',
    'gis_commen': 'GIS_Commen',
    'eigner_map': 'Eigner_Map',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'resources_field': 'Resources_',
    'geom': 'MULTIPOLYGON',
}


finds_shp = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 'data', 'shapes',
        'shp_fuer_ACDH', 'Finds_20170928.shp'
    ),
)


def run_finds(verbose=True):
    lm = LayerMapping(
        Find, finds_shp, find_mapping,
        transform=True, encoding='utf-8',
    )
    lm.save(strict=True, verbose=verbose)


stratunit_mapping = {
    'objectid': 'OBJECTID',
    'orea_gis_i': 'OREA_GIS_I',
    'excavation': 'Excavation',
    'stratum_id': 'Stratum_ID',
    'phase_id': 'Phase_ID',
    'locus_id': 'Locus_ID',
    'locus_wall': 'Locus_wall',
    'archaeolog': 'Archaeolog',
    'archaeol_1': 'Archaeol_1',
    'archaeol_2': 'Archaeol_2',
    'height_top': 'Height_top',
    'height_t_1': 'Height_t_1',
    'height_bot': 'Height_bot',
    'height_b_1': 'Height_b_1',
    'extrusion': 'Extrusion',
    'base_heigh': 'Base_heigh',
    'eigner_map': 'Eigner_map',
    'pit_fill': 'Pit_fill',
    'pit_find_g': 'Pit_find_G',
    'bp_materia': 'Bp_materia',
    'bp_door_st': 'Bp_door_st',
    'bp_door_1': 'Bp_door__1',
    'wall_type': 'Wall_type',
    'wall_cours': 'Wall_cours',
    'wall_inter': 'Wall_inter',
    'wall_brick': 'Wall_brick',
    'locus_laye': 'Locus_laye',
    'shape_clas': 'Shape_clas',
    'orientatio': 'Orientatio',
    'wall_funct': 'Wall_funct',
    'wall_conne': 'Wall_conne',
    'shape_leng': 'SHAPE_Leng',
    'shape_area': 'SHAPE_Area',
    'resources_field': 'Resources_',
    'geom': 'MULTIPOLYGON',
}


stratunit_shp = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 'data', 'shapes',
        'shp_fuer_ACDH', 'Archaeological_objects_20170928.shp'
    ),
)


def run_strat(verbose=True):
    lm = LayerMapping(
        Stratunit, stratunit_shp, stratunit_mapping,
        transform=True, encoding='utf-8',
    )
    lm.save(strict=True, verbose=verbose)


brick_mapping = {
    'objectid': 'OBJECTID',
    'orea_gis_i': 'OREA_GIS_I',
    'excavation': 'Excavation',
    'stratum_id': 'Stratum_ID',
    'phase_id': 'Phase_ID',
    'archaeolog': 'Archaeolog',
    'archaeol_1': 'Archaeol_1',
    'archaeol_2': 'Archaeol_2',
    'brick_type': 'Brick_type',
    'brick_mate': 'Brick_mate',
    'height_max': 'Height_max',
    'extrusion': 'Extrusion',
    'base_heigh': 'Base_heigh',
    'orientatio': 'Orientatio',
    'shape_leng': 'SHAPE_Leng',
    'shape_area': 'SHAPE_Area',
    'resources_field': 'Resources_',
    'geom': 'MULTIPOLYGON',
}

bricks_shp = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),  'data', 'shapes',
        'shp_fuer_ACDH', 'Bricks_20170928.shp'
    ),
)


def run_brick(verbose=True):
    lm = LayerMapping(
        Brick, bricks_shp, brick_mapping,
        transform=True, encoding='utf-8',
    )
    lm.save(strict=True, verbose=verbose)

# C:\Users\pandorfer\ownCloud\GIT\Redmine\4dpuzzle>python manage.py ogrinspect archobs/data/shapes/shp_fuer_ACDH/Bricks_20170928.shp Brick --srid=4326 --mapping --multi >hansi.py --settings=4dpuzzle.settings.pg_local
