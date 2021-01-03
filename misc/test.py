import timeit
import datetime
import json

def json_default(arg_obj):
    if isinstance(arg_obj, float):
        return round(arg_obj, 9)
    else:
        return arg_obj


t = {
    'a': 1,
    'b': 1.1,
    'c': round(1.11100000000000, 9),
}

s = json.dumps(t, default = json_default)
print(s)
