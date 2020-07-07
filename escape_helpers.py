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
        return sparql_escape_string(obj)
    if isinstance(obj, datetime.datetime):
        return sparql_escape_datetime(obj)
    if isinstance(obj, datetime.date):
        return sparql_escape_date(obj)
    if isinstance(obj, datetime.time):
        return sparql_escape_time(obj)
    if isinstance(obj, int):
        return sparql_escape_int(obj)
    if isinstance(obj, float):
        return sparql_escape_float(obj)
    if isinstance(obj, bool):
        return sparql_escape_bool(obj)
    return ""
