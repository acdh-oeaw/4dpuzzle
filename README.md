# 4dpuzzle

This is the code repo for [Tell el Daba  A Puzzle in 4D](https://4dpuzzle.orea.oeaw.ac.at/).

# Important Notice

This application is still in development and not for productive use.

# Licensing

All code unless otherwise noted is licensed under the terms of the MIT License (MIT).
Please refer to the file COPYING in the root directory of this repository.

All documentation and images unless otherwise noted are licensed under the terms of Creative Commons Attribution-ShareAlike 4.0 International License.
To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/

# Install

## Required Software
This software was developed with Python 3.6.x. Since the application deals with GIS-Data, it uses [GeoDjango](https://docs.djangoproject.com/en/1.11/ref/contrib/gis/). Please refer to the official documentation in regards of needed dependencies and how to install them.

To install additional required Python/Django packages execute:

`pip install -r requirements.txt`

## Configuration Files

### custom settings file

This django project uses modularized settings as described in [this blog post](https://simpleisbetterthancomplex.com/tips/2017/07/03/django-tip-20-working-with-multiple-settings-modules.html) to keep sensitiv information out of GitHub. Therefore you'll have to adapt `4dpuzzle/settings/dev.py` to your needs, like changing the `SECRET_KEY` or adding your specific data base settings.
To start the dev-server you'll have to pass in a settings parameter pointing to your custom settings file like: `python manage.py runserver --settings=4dpuzzle.settings.{nameOfCustomSettingsFile}`

### basic metadata file

Basic metadata like the application's title, author, some description or version number of the application is captured in `webpage/metadata.py`. Adapt this file according to your needs.
