import json
import jsonlines
from collections import Counter
import pandas as pd
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt


rank_dict=json.load(open('as_rank_dict.json'))
victim_list=[]
hijacker_list=[]
victim_rank_list=[]
hijacker_rank_list=[]

def get_json(mylist):
    victim=mylist['before_as']
    victim_list.append(victim)

    hijacker=mylist['suspicious_as']
    hijacker_list.append(hijacker)


def draw_cdf():
    count0 = Counter(victim_rank_list)
    totalnumber0=sorted(count0.items(),key=lambda x:x[0])

    count1 = Counter(hijacker_rank_list)
    totalnumber1=sorted(count1.items(),key=lambda x:x[0])

    x=range(80000)
    y=[0 for index in range(80000)]
    z=[0 for index in range(80000)]

    for i,v in totalnumber0:
        y[i]=v

    for i,v in totalnumber1:
        z[i]=v

    pdf_vic=y/np.sum(y)
    cdf_vic=np.cumsum(pdf_vic)

    pdf_att=z/np.sum(z)
    cdf_att=np.cumsum(pdf_att)

    plt.plot(x, cdf_vic,label='victim')
    plt.plot(x, cdf_att,label='hijacker')
    plt.legend()
    plt.xlim(0,75000)
    plt.ylim(0,1.0)
    plt.xlabel("AS Rank")
    plt.ylabel("probability value")
    plt.grid(True)
    plt.title("cdf of Victim/Hijacker AS Rank")
    plt.show()
    plt.savefig('cdf_rank_2.png')
    

file=open('selected_fh1.jsonl')
for line in file.readlines():
    json_file=json.loads(line)
    get_json (json_file)

victim_list=list(dict.fromkeys(victim_list))
hijacker_list=list(dict.fromkeys(hijacker_list))
print(len(victim_list))
print(len(hijacker_list))
for i in  victim_list:
    if i in rank_dict:
        victim_rank=rank_dict[i]
        victim_rank_list.append(victim_rank)

for i in hijacker_list:
    if i in rank_dict:
        hijacker_rank=rank_dict[i]
        hijacker_rank_list.append(hijacker_rank)
        
count1 = Counter(hijacker_rank_list)
totalnumber1=sorted(count1.items(),key=lambda x:x[1],reverse=True)
print(totalnumber1[:10])

count0 = Counter(victim_rank_list)
totalnumber0=sorted(count0.items(),key=lambda x:x[1],reverse=True)
print(totalnumber0[:10])
