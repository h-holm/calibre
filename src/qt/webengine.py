# autogenerated by __main__.py do not edit
from .webengine_name_map import module_names, name_map
from .loader import dynamic_load

already_imported = {}
qt_modules = {}

def __getattr__(name):
    return dynamic_load(name, name_map, already_imported, qt_modules, module_names)
