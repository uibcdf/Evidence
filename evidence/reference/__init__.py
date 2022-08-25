from importlib import import_module
import os

_dict_ref = {}

current_dir = os.path.dirname(os.path.abspath(__file__))

excluded_files = ['__init__.py', 'database.py']
list_refs = [filename.split('.')[0] for filename in os.listdir(current_dir) if (filename not in excluded_files) and filename.endswith('.py')]

for ref_name in list_refs:

    mod = import_module('evidence.reference.'+ref_name)

    ref = getattr(mod, ref_name)

    _dict_ref[mod.name]=ref
    locals()[ref_name]=ref

del(current_dir, excluded_files, list_refs, ref_name, mod, ref)

def add_database(name=None, id=None, long_name=None, web=None, webid=None, info=None):

    if name is not None:

        from evidence.reference.database import DataBase

        def __init__database(self, id=None):

            self.id = id

        name_class = name.replace(' ', '_')

        new_class = type(name_class, (DataBase, ), {
            "__init__": __init__database,
            "name": name,
            "long_name": long_name,
            "web":web,
            "webid":webid,
            "info": info
            })

        _dict_ref[name] = new_class
        locals()[name_class] = new_class

