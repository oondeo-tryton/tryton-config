#!/usr/bin/env python
import os
import sys

directories = [os.path.abspath(os.path.normpath(os.path.join(os.getcwd(),'nereid')))]
directories += [os.path.abspath(os.path.normpath(os.path.join(os.getcwd(),'trytond')))]

for directory in directories:
     print directory
     if os.path.isdir(directory):
         sys.path.insert(0, directory)

from nereid import Nereid

CONFIG = dict(

    # The name of database
    DATABASE_NAME='nereid',

    # Static file root. The root location of the static files. The static/ will
    # point to this location. It is recommended to use the web server to serve
    # static content
    STATIC_FILEROOT='static/',

    # Tryton Config file path
    TRYTON_CONFIG='trytond/etc/trytond.conf',

    # If the application is to be configured in the debug mode
    DEBUG=True,

    # Load the template from FileSystem in the path below instead of the
    # default Tryton loader where templates are loaded from Database
    TEMPLATE_LOADER_CLASS='nereid.templating.FileSystemLoader',
    TEMPLATE_SEARCH_PATH='.',
)


# Create a new application
app = Nereid()

# Update the configuration with the above config values
app.config.update(CONFIG)

# Initialise the app, connect to cache and backend
app.initialise()


if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0')
