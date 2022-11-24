import json
import jsonlines
import time
from collections import Counter
import pandas as pd
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

prefix_set=set()
hijacker_set=set()
victim_set=set()

victim_country_list=[]
attacker_country_list=[]
hijacker_list=[]
victim_list=[]

prefix_list=[]
affected_rate=[]
affected_dict={}
affected_dict1={}
affected_dict2={}
n=0
cnt1=0
cnt2=0

def get_json(mylist):
    victim_country=mylist['before_as_country']
    attacker_country=mylist['suspicious_as_country']
    if (victim_country!='US')and(attacker_country!='US'):
        return
    hijacker_set.add(mylist['suspicious_as'])
    victim_set.add(mylist['before_as'])

def real():
    file=open('selected_fh1.jsonl')
    for line in file.readlines():
        try:
            json_file=json.loads(line)
        except:
            n+=1
            print(n)
        else:
            get_json (json_file)

real()
print(list(hijacker_set.intersection(victim_set)))