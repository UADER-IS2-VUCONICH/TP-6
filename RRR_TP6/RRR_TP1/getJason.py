# uncompyle6 version 3.9.1
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)]
# Embedded file name: getJason.py
# Compiled at: 2022-06-14 16:15:55
import json, sys
jsonfile = sys.argv[1]
jsonkey = sys.argv[2]
with open(jsonfile, 'r') as myfile:
    data = myfile.read()
obj = json.loads(data)
print str(obj[jsonkey])

# okay decompiling getJason.pyc
