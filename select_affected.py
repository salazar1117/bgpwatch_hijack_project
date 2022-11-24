import json
import jsonlines
from collections import Counter
import pandas as pd
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

affected_rate=[]
victim_rank_list=[]
attacker_rank_list=[]

asrank= open('rank_dict.json', 'r')
content0 = asrank.read()
rank_dict= json.loads(content0)



def get_json (mylist):
    hijacker=mylist['suspicious_as']
    victim=mylist['before_as']
    timestamp=str(int(mylist['start_timestamp']))
    replay=mylist['replay']
    all_vp=[]
    affected_as=[]
    for tm in replay:
        pathlist=replay[tm]['path_list']
        for path in pathlist:
            path_tmp=list(dict.fromkeys(path.split()))
            all_vp.append(path_tmp[0])
            if path_tmp[-1]==hijacker:
                affected_as.append(path_tmp[0])

    all_vp=list(dict.fromkeys(all_vp))
    affected_as=list(dict.fromkeys(affected_as))
    if len(all_vp)==len(affected_as):
        affected_rate.append('all')
    else:
        affected_rate.append(len(affected_as)/len(all_vp))


    if victim in rank_dict:
        victim_rank=rank_dict[victim]
        victim_rank_list.append(victim_rank)
    if hijacker in rank_dict:
        attacker_rank=rank_dict[hijacker]
        attacker_rank_list.append(attacker_rank)

def draw_cdf():
    count0 = Counter(victim_rank_list)
    totalnumber0=sorted(count0.items(),key=lambda x:x[0])

    count1 = Counter(attacker_rank_list)
    totalnumber1=sorted(count1.items(),key=lambda x:x[0])

    x=range(75000)
    y=[0 for index in range(75000)]
    z=[0 for index in range(75000)]

    for i,v in totalnumber0:
        y[i]=v

    for i,v in totalnumber1:
        z[i]=v

    pdf_vic=y/np.sum(y)
    cdf_vic=np.cumsum(pdf_vic)

    pdf_att=z/np.sum(z)
    cdf_att=np.cumsum(pdf_att)

    plt.plot(x, cdf_vic,'b',label='victim')
    plt.plot(x, cdf_att,'g',label='hijacker')
    plt.legend()
    plt.xlim(0,75000)
    plt.ylim(0,1.0)
    plt.xlabel("AS Rank")
    plt.ylabel("probability")
    plt.title("cdf of Victim/Hijacker AS Rank")
    plt.show()
    plt.savefig('cdf_rank.png')


file=open('selected_hijack_1.jsonl')
for line in file.readlines():
    json_file=json.loads(line)
    get_json (json_file)
    
draw_cdf()
print(affected_rate)