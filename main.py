import requests


def introspection_info(obj):
    type_obj = type(obj).__name__
    attributs_obj = [i for i in dir(obj) if not callable(getattr(obj, i))]
    methods_obj = [n for n in dir(obj) if callable(getattr(obj, n))]
    module = obj.__class__.__module__

    b = {'type': type_obj, "attributs": attributs_obj, "methods": methods_obj, 'module': module}
    return b


numbs = introspection_info(20)

print(numbs)
