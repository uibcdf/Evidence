from importlib import import_module
import os

_dict_class = {}
_name_to_class_name = {}

current_dir = os.path.dirname(os.path.abspath(__file__))

excluded_files = ['__init__.py', 'database.py']
list_module_names = [filename.split('.')[0] for filename in os.listdir(current_dir) if (filename not in excluded_files) and filename.endswith('.py')]

for module_name in list_module_names:

    class_name = module_name
    module = import_module('evidence.reference.'+module_name)
    _dict_class[class_name]=getattr(module, class_name)
    locals()[class_name]=getattr(module, class_name)
    _name_to_class_name[module.name]=class_name

del(current_dir, excluded_files, list_module_names, class_name, module)

def add_database(name=None, id=None, long_name=None, web=None, webid=None, info=None):

    if name is not None:

        from evidence.reference.database import DataBase

        def __init__database(self, id=None):

            self.id = id

        class_name = _name_to_class_name[name]

        new_class = type(class_name, (DataBase, ), {
            "__init__": __init__database,
            "name": name,
            "long_name": long_name,
            "web":web,
            "webid":webid,
            "info": info
            })

        _dict_class[class_name] = new_class
        locals()[class_name] = new_class

