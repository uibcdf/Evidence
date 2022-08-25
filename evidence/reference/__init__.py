from importlib import import_module
import os

_dict_ref = {}

current_dir = os.path.dirname(os.path.abspath(__file__))

excluded_files = ['__init__.py', 'database.py']
list_refs = [filename.split('.')[0] for filename in os.listdir(current_dir) if (filename not in excluded_files) and filename.endswith('.py')]

for ref_name in list_refs:

    mod = import_module('evidence.reference.'+ref_name)

    ref = getattr(mod, ref_name)

    _dict_ref[ref.name]=ref
    locals()[ref_name]=ref

del(current_dir, excluded_files, list_refs, ref_name, mod, ref)

