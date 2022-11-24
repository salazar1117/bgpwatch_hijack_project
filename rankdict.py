import json
import jsonlines
from collections import Counter
import pandas as pd
import numpy as np
import pickle


rank_dict={}

def get_json (mylist):
    if mylist[1:5]=='None':
        return
    print(mylist)
    a=mylist.find(',')-1
    b=mylist.find('\'rank\':')+8
    asn=mylist[10:a]
    rank=int(mylist[b:-4])
    rank_dict[asn]=rank
    
file=open('asinfo.jsonl')
for line in file.readlines():
    json_file=json.dumps(line)
    get_json (json_file)


b = json.dumps(rank_dict)
f2 = open('as_rank_dict.json', 'w')
f2.write(b)
f2.close()