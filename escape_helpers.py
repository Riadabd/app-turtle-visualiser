import datetime
import re

def sparql_escape_string(obj):
    obj = str(obj)
    return '"""' + re.sub(r'[\\\'"]', lambda s: "\\" + s.group(0), obj) + '"""'

def sparql_escape_datetime(obj):
    if isinstance(obj, datetime.datetime):
        obj = obj.replace(microsecond=0) # xsd doesn't support microseconds in ISO time format
        return '"{}"^^xsd:dateTime'.format(obj.isoformat())
    try:
        obj = datetime.datetime.strptime(str(obj), "%Y-%m-%dT%H:%M:%S")
        return '"{}"^^xsd:dateTime'.format(obj.isoformat())
    except ValueError as e: # Failed casting to string or invalid dateTime format
        raise e

def sparql_escape_date(obj):
    if isinstance(obj, datetime.date):
        return '"{}"^^xsd:date'.format(obj.isoformat())
    try:
        obj = datetime.datetime.strptime(str(obj), "%Y-%m-%d").date()
        return '"{}"^^xsd:date'.format(obj.isoformat())
    except ValueError as e: # Failed casting to string or invalid date format
        raise e

def sparql_escape_time(obj):
    if isinstance(obj, datetime.time):
        obj = obj.replace(microsecond=0) # xsd doesn't support microseconds in ISO time format
        return '"{}"^^xsd:time'.format(obj.isoformat())
    try:
        obj = datetime.datetime.strptime(str(obj), "%H:%M:%S").time()
        return '"{}"^^xsd:time'.format(obj.isoformat())
    except ValueError as e: # Failed casting to string or invalid time format
        raise e

def sparql_escape_int(obj):
    if isinstance(obj, int):
        return '"{}"^^xsd:integer'.format(obj)
    try:
        obj = str(int(obj))
        return '"{}"^^xsd:integer'.format(obj)
    except ValueError as e: # Failed casting
        raise e

def sparql_escape_float(obj):
    if isinstance(obj, float):
        return '"{}"^^xsd:float'.format(obj)
    try:
        obj = str(float(obj))
        return '"{}"^^xsd:float'.format(obj)
    except ValueError as e: # Failed casting
        raise e

def sparql_escape_bool(obj):
    if isinstance(obj, bool):
        return '"{}"^^xsd:boolean'.format(obj)
    try:
        obj = str(bool(obj))
        return '"{}"^^xsd:boolean'.format(obj)
    except ValueError as e: # Failed casting
        raise e

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
