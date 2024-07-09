#!/usr/bin/env bash
# create_fixtures.sh

# make sure you ran `pip install django-fixture-magic` and added `'fixture_magic'` to INSTALLED_APPS
source env/bin/activate
source set_env_variables.sh
mkdir ./archiv/fixtures
touch ./archiv/fixtures/dump.json
echo "create fixtures_archiv"
python manage.py dump_object archiv.fielddrawing 1557 > ./archiv/fixtures/fielddrawing.json
python manage.py dump_object archiv.fotosgescannt 8 > ./archiv/fixtures/fotosgescannt.json

echo "merging fixtures"
python manage.py merge_fixtures ./archiv/fixtures/fielddrawing.json ./archiv/fixtures/fotosgescannt.json > archiv/fixtures/dump.json

rm ./archiv/fixtures/fielddrawing.json
rm ./archiv/fixtures/fotosgescannt.json


echo "done"