import json
import jsonlines
from collections import Counter
import pandas as pd
import numpy as np
import pickle


rank_dict={}
n=0
def get_json (mylist):
    global n
    n+=1
    print(n)
    rank_dict[mylist['asn']]=mylist['rank']
    
file=open('as-summary.jsonl')
for line in file.readlines():
    json_file=json.loads(line)
    get_json1 (json_file)


b = json.dumps(rank_dict)
f2 = open('as_rank_dict1.json', 'w')
f2.write(b)
f2.close()