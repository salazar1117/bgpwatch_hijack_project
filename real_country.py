import json
import jsonlines
from collections import Counter
import pandas as pd
import numpy as np
import pickle


country_dict={}

def get_json (mylist):
#as-summary
    a=mylist.find('asnName')-7
    b=mylist.find('iso')+9
    asn=mylist[13:a]
    country=mylist[b:b+2]
    country_dict[asn]=country

def get_json1 (mylist):
#as-info
    a=mylist.find('as-org')-3
    b=mylist.find('org_source')-7
    asn=mylist[10:a]
    country=mylist[b:b+2]
    country_dict[asn]=country

def get_json2(mylist):
    aa=mylist.split('|')
    if aa[2]=='asn':
        country_dict[aa[3]]=aa[1]

file=open('as_info.jsonl')
for line in file.readlines():
    json_file=json.dumps(line)
    get_json1 (json_file)



file=open('delegated-apnic-20220601.jsonl')
for line in file.readlines():
    json_file=json.dumps(line)
    get_json2 (json_file)

b = json.dumps(country_dict)
f2 = open('country_dict_2.json', 'w')
f2.write(b)
f2.close()