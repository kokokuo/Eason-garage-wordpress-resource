from distutils.core import setup
import py2exe

setup(
    options = {'py2exe': {
        'bundle_files': 1,
        'compressed': True,
    }},
    console = [{'script': 'Hello.py',"icon_resources": [(1, "python.ico")]}],
    zipfile = None
)
