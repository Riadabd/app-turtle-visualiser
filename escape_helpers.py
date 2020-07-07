import datetime
import re
from warnings import warn

def sparql_escape_string(obj):
    if not isinstance(obj, str):
        warn("You are escaping something that isn't a string with \
        the 'sparql_escape_string'-method. Implicit casting will occurr.")
        obj = str(obj)
    return '"""' + re.sub(r'[\\\'"]', lambda s: "\\" + s.group(0), obj) + '"""'

def sparql_escape_datetime(obj):
    if not isinstance(obj, datetime.datetime):
        warn("You are escaping something that isn't a datetime with \
        the 'sparql_escape_datetime'-method. Implicit casting will occurr.")
        obj = datetime.datetime.strptime(str(obj), "%Y-%m-%dT%H:%M:%S")
    obj = obj.replace(microsecond=0) # xsd doesn't support microseconds in ISO time format
    return '"{}"^^xsd:dateTime'.format(obj.isoformat())

def sparql_escape_date(obj):
    if not isinstance(obj, datetime.date):
        warn("You are escaping something that isn't a date with \
        the 'sparql_escape_date'-method. Implicit casting will occurr.")
        obj = datetime.datetime.strptime(str(obj), "%Y-%m-%d").date()
    return '"{}"^^xsd:date'.format(obj.isoformat())

def sparql_escape_time(obj):
    if not isinstance(obj, datetime.time):
        warn("You are escaping something that isn't a time with \
        the 'sparql_escape_time'-method. Implicit casting will occurr.")
        obj = datetime.datetime.strptime(str(obj), "%H:%M:%S").time()
    obj = obj.replace(microsecond=0) # xsd doesn't support microseconds in ISO time format
    return '"{}"^^xsd:time'.format(obj.isoformat())

def sparql_escape_int(obj):
    if not isinstance(obj, int):
        warn("You are escaping something that isn't an int with \
        the 'sparql_escape_int'-method. Implicit casting will occurr.")
        obj = str(int(obj))
    return '"{}"^^xsd:integer'.format(obj)

def sparql_escape_float(obj):
    if not isinstance(obj, int):
        warn("You are escaping something that isn't a float with \
        the 'sparql_escape_float'-method. Implicit casting will occurr.")
        obj = str(float(obj))
    return '"{}"^^xsd:float'.format(obj)

def sparql_escape_bool(obj):
    if not isinstance(obj, bool):
        warn("You are escaping something that isn't a bool with \
        the 'sparql_escape_bool'-method. Implicit casting will occurr.")
        obj = bool(obj)
    return '"{}"^^xsd:boolean'.format("true" if obj else "false")

def sparql_escape_uri(obj):
    obj = str(obj)
    return '<' + re.sub(r'[\\\'"]', lambda s: "\\" + s.group(0), obj) + '>'

def sparql_escape(obj):
    if isinstance(obj, str):
        escaped_val = sparql_escape_string(obj)
    elif isinstance(obj, datetime.datetime):
        escaped_val = sparql_escape_datetime(obj)
    elif isinstance(obj, datetime.date):
        escaped_val = sparql_escape_date(obj)
    elif isinstance(obj, datetime.time):
        escaped_val = sparql_escape_time(obj)
    elif isinstance(obj, int):
        escaped_val = sparql_escape_int(obj)
    elif isinstance(obj, float):
        escaped_val = sparql_escape_float(obj)
    elif isinstance(obj, bool):
        escaped_val = sparql_escape_bool(obj)
    else:
        warn("Unknown escape type '{}'. Escaping as string".format(type(obj)))
        escaped_val = sparql_escape_string(obj)
    return escaped_val
