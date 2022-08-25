from importlib import import_module
import os

dict_ref = {}

current_dir = os.path.dirname(os.path.abspath(__file__))

excluded_files = ['__init__.py', 'reference.py']
list_apis = [filename.split('.')[0] for filename in os.listdir(current_dir) if (filename not in excluded_files) and filename.endswith('.py')]

for api_name in list_apis:

    mod = import_module('evidence.references.'+api_name)

    dict_ref[api_name]=getattr(mod, api_name)

del(current_dir, excluded_files, list_apis, mod, api_name)

