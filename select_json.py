import json
import jsonlines
from collections import Counter
import pandas as pd
import numpy as np

n=0
a=[]
moas_as=[['135062','55303','58810'],
['212217','210727'],
['328873','328276'],
['136907','55990'],
['55020','137951'],
['395886','8796'],
['149548','132346'],
['48678','207633']]

def parse(text):
    with jsonlines.open('selected_fh.jsonl',mode='a') as writer:
        writer.write(text)

def get_json (mylist):
    global n
    n+=1
    timespand=mylist['duration']
    h,m,s = timespand.strip().split(":")
    if int(h)>48:
        return

    hijacker=mylist['suspicious_as']
    victim=mylist['before_as']
    timestamp=str(int(mylist['start_timestamp']))
    replay=mylist['replay']

    for tm in replay:
        pathlist=replay[tm]['path_list']
        path_victim=[]
        path_hijacker=[]
        for path in pathlist:
            path_tmp=list(dict.fromkeys(path.split()))
            if path_tmp[-1]==victim:
                path_victim.append(path)
            else:
                path_hijacker.append(path)
        if len(path_hijacker)==0:
            continue
        if len(path_victim)==0:
            continue
        for vic in path_victim:
            via=vic.split()
            if hijacker in via:
                return
        try:
            path_hijacker[0][-2]
        except:
            print('index error:')
            print(path_hijacker[0])
        else:
            if path_victim[0][-2]==path_hijacker[0][-2]:
                return
        break

    if [hijacker,victim] in moas_as:
        return
    if [victim,hijacker] in moas_as:
        return

    parse(mylist)


file=open('fh.jsonl')
for line in file.readlines():
    try:
        json_file=json.loads(line)
    except:
        n+=1
        print(n)
    else:
        get_json (json_file)


