import datetime
import re

def sparql_escape(obj):
    if type(obj) is str:
        def replacer(a):
            return "\\"+a.group(0)
        return '"' + re.sub(r'[\\"]', replacer, obj) + '"'
    elif type(obj) is datetime.time:
        return '"' + obj.isoformat() + '"^^xsd:dateTime'
    elif type(obj) is datetime.date:
        return '"' + obj.isoformat() + '"^^xsd:date'
    elif type(obj) is int:
        return '"' + str(obj) + '"^^xsd:integer'
    elif type(obj) is float:
        return '"' + str(obj) + '"^^xsd:float'
    elif type(obj) is bool:
        return '"' + str(obj) + '"^^xsd:boolean'
    else:
        return ""
