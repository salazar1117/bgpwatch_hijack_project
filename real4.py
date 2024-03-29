import json
import jsonlines
import time
from collections import Counter
import pandas as pd
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

date_list=['2021-10-22', '2021-10-23', '2021-10-24', '2021-10-25', '2021-10-26', '2021-10-27', '2021-10-28', '2021-10-29', '2021-10-30', '2021-10-31', '2021-11-01', '2021-11-02', '2021-11-03', '2021-11-04', '2021-11-05', '2021-11-06', '2021-11-07', '2021-11-08', '2021-11-09', '2021-11-10', '2021-11-11', '2021-11-12', '2021-11-13', '2021-11-14', '2021-11-15', '2021-11-16', '2021-11-17', '2021-11-18', '2021-11-19', '2021-11-20', '2021-11-21', '2021-11-22', '2021-11-23', '2021-11-24', '2021-11-25', '2021-11-26', '2021-11-27', '2021-11-28', '2021-11-29', '2021-11-30', '2021-12-01', '2021-12-02', '2021-12-03', '2021-12-04', '2021-12-05', '2021-12-06', '2021-12-07', '2021-12-08', '2021-12-09', '2021-12-10', '2021-12-11', '2021-12-12', '2021-12-13', '2021-12-14', '2021-12-15', '2021-12-16', '2021-12-17', '2021-12-18', '2021-12-19', '2021-12-20', '2021-12-21', '2021-12-22', '2021-12-23', '2021-12-24', '2021-12-25', '2021-12-26', '2021-12-27', '2021-12-28', '2021-12-29', '2021-12-30', '2021-12-31', '2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05', '2022-01-06', '2022-01-07', '2022-01-08', '2022-01-09', '2022-01-10', '2022-01-11', '2022-01-12', '2022-01-13', '2022-01-14', '2022-01-15', '2022-01-16', '2022-01-17', '2022-01-18', '2022-01-19', '2022-01-20', '2022-01-21', '2022-01-22', '2022-01-23', '2022-01-24', '2022-01-25', '2022-01-26', '2022-01-27', '2022-01-28', '2022-01-29', '2022-01-30', '2022-01-31', '2022-02-01', '2022-02-02', '2022-02-03', '2022-02-04', '2022-02-05', '2022-02-06', '2022-02-07', '2022-02-08', '2022-02-09', '2022-02-10', '2022-02-11', '2022-02-12', '2022-02-13', '2022-02-14', '2022-02-15', '2022-02-16', '2022-02-17', '2022-02-18', '2022-02-19', '2022-02-20', '2022-02-21', '2022-02-22', '2022-02-23', '2022-02-24', '2022-02-25', '2022-02-26', '2022-02-27', '2022-02-28', '2022-03-01', '2022-03-02', '2022-03-03', '2022-03-04', '2022-03-05', '2022-03-06', '2022-03-07', '2022-03-08', '2022-03-09', '2022-03-10', '2022-03-11', '2022-03-12', '2022-03-13', '2022-03-14', '2022-03-15', '2022-03-16', '2022-03-17', '2022-03-18', '2022-03-19', '2022-03-20', '2022-03-21', '2022-03-22', '2022-03-23', '2022-03-24', '2022-03-25', '2022-03-26', '2022-03-27', '2022-03-28', '2022-03-29', '2022-03-30', '2022-03-31', '2022-04-01', '2022-04-02', '2022-04-03', '2022-04-04', '2022-04-05', '2022-04-06', '2022-04-07', '2022-04-08', '2022-04-09', '2022-04-10', '2022-04-11', '2022-04-12', '2022-04-13', '2022-04-14', '2022-04-15', '2022-04-16', '2022-04-17', '2022-04-18', '2022-04-19', '2022-04-20', '2022-04-21', '2022-04-22', '2022-04-23', '2022-04-24', '2022-04-25', '2022-04-26', '2022-04-27', '2022-04-28', '2022-04-29', '2022-04-30', '2022-05-01', '2022-05-02', '2022-05-03', '2022-05-04', '2022-05-05', '2022-05-06', '2022-05-07', '2022-05-08', '2022-05-09', '2022-05-10', '2022-05-11', '2022-05-12', '2022-05-13', '2022-05-14', '2022-05-15', '2022-05-16', '2022-05-17', '2022-05-18', '2022-05-19', '2022-05-20', '2022-05-21', '2022-05-22', '2022-05-23', '2022-05-24', '2022-05-25', '2022-05-26', '2022-05-27', '2022-05-28', '2022-05-29', '2022-05-30', '2022-05-31', '2022-06-01', '2022-06-02', '2022-06-03', '2022-06-04', '2022-06-05', '2022-06-06', '2022-06-07', '2022-06-08', '2022-06-09', '2022-06-10', '2022-06-11', '2022-06-12', '2022-06-13', '2022-06-14', '2022-06-15']
date_dict={'2021-10-22': 0, '2021-10-23': 1, '2021-10-24': 2, '2021-10-25': 3, '2021-10-26': 4, '2021-10-27': 5, '2021-10-28': 6, '2021-10-29': 7, '2021-10-30': 8, '2021-10-31': 9, '2021-11-01': 10, '2021-11-02': 11, '2021-11-03': 12, '2021-11-04': 13, '2021-11-05': 14, '2021-11-06': 15, '2021-11-07': 16, '2021-11-08': 17, '2021-11-09': 18, '2021-11-10': 19, '2021-11-11': 20, '2021-11-12': 21, '2021-11-13': 22, '2021-11-14': 23, '2021-11-15': 24, '2021-11-16': 25, '2021-11-17': 26, '2021-11-18': 27, '2021-11-19': 28, '2021-11-20': 29, '2021-11-21': 30, '2021-11-22': 31, '2021-11-23': 32, '2021-11-24': 33, '2021-11-25': 34, '2021-11-26': 35, '2021-11-27': 36, '2021-11-28': 37, '2021-11-29': 38, '2021-11-30': 39, '2021-12-01': 40, '2021-12-02': 41, '2021-12-03': 42, '2021-12-04': 43, '2021-12-05': 44, '2021-12-06': 45, '2021-12-07': 46, '2021-12-08': 47, '2021-12-09': 48, '2021-12-10': 49, '2021-12-11': 50, '2021-12-12': 51, '2021-12-13': 52, '2021-12-14': 53, '2021-12-15': 54, '2021-12-16': 55, '2021-12-17': 56, '2021-12-18': 57, '2021-12-19': 58, '2021-12-20': 59, '2021-12-21': 60, '2021-12-22': 61, '2021-12-23': 62, '2021-12-24': 63, '2021-12-25': 64, '2021-12-26': 65, '2021-12-27': 66, '2021-12-28': 67, '2021-12-29': 68, '2021-12-30': 69, '2021-12-31': 70, '2022-01-01': 71, '2022-01-02': 72, '2022-01-03': 73, '2022-01-04': 74, '2022-01-05': 75, '2022-01-06': 76, '2022-01-07': 77, '2022-01-08': 78, '2022-01-09': 79, '2022-01-10': 80, '2022-01-11': 81, '2022-01-12': 82, '2022-01-13': 83, '2022-01-14': 84, '2022-01-15': 85, '2022-01-16': 86, '2022-01-17': 87, '2022-01-18': 88, '2022-01-19': 89, '2022-01-20': 90, '2022-01-21': 91, '2022-01-22': 92, '2022-01-23': 93, '2022-01-24': 94, '2022-01-25': 95, '2022-01-26': 96, '2022-01-27': 97, '2022-01-28': 98, '2022-01-29': 99, '2022-01-30': 100, '2022-01-31': 101, '2022-02-01': 102, '2022-02-02': 103, '2022-02-03': 104, '2022-02-04': 105, '2022-02-05': 106, '2022-02-06': 107, '2022-02-07': 108, '2022-02-08': 109, '2022-02-09': 110, '2022-02-10': 111, '2022-02-11': 112, '2022-02-12': 113, '2022-02-13': 114, '2022-02-14': 115, '2022-02-15': 116, '2022-02-16': 117, '2022-02-17': 118, '2022-02-18': 119, '2022-02-19': 120, '2022-02-20': 121, '2022-02-21': 122, '2022-02-22': 123, '2022-02-23': 124, '2022-02-24': 125, '2022-02-25': 126, '2022-02-26': 127, '2022-02-27': 128, '2022-02-28': 129, '2022-03-01': 130, '2022-03-02': 131, '2022-03-03': 132, '2022-03-04': 133, '2022-03-05': 134, '2022-03-06': 135, '2022-03-07': 136, '2022-03-08': 137, '2022-03-09': 138, '2022-03-10': 139, '2022-03-11': 140, '2022-03-12': 141, '2022-03-13': 142, '2022-03-14': 143, '2022-03-15': 144, '2022-03-16': 145, '2022-03-17': 146, '2022-03-18': 147, '2022-03-19': 148, '2022-03-20': 149, '2022-03-21': 150, '2022-03-22': 151, '2022-03-23': 152, '2022-03-24': 153, '2022-03-25': 154, '2022-03-26': 155, '2022-03-27': 156, '2022-03-28': 157, '2022-03-29': 158, '2022-03-30': 159, '2022-03-31': 160, '2022-04-01': 161, '2022-04-02': 162, '2022-04-03': 163, '2022-04-04': 164, '2022-04-05': 165, '2022-04-06': 166, '2022-04-07': 167, '2022-04-08': 168, '2022-04-09': 169, '2022-04-10': 170, '2022-04-11': 171, '2022-04-12': 172, '2022-04-13': 173, '2022-04-14': 174, '2022-04-15': 175, '2022-04-16': 176, '2022-04-17': 177, '2022-04-18': 178, '2022-04-19': 179, '2022-04-20': 180, '2022-04-21': 181, '2022-04-22': 182, '2022-04-23': 183, '2022-04-24': 184, '2022-04-25': 185, '2022-04-26': 186, '2022-04-27': 187, '2022-04-28': 188, '2022-04-29': 189, '2022-04-30': 190, '2022-05-01': 191, '2022-05-02': 192, '2022-05-03': 193, '2022-05-04': 194, '2022-05-05': 195, '2022-05-06': 196, '2022-05-07': 197, '2022-05-08': 198, '2022-05-09': 199, '2022-05-10': 200, '2022-05-11': 201, '2022-05-12': 202, '2022-05-13': 203, '2022-05-14': 204, '2022-05-15': 205, '2022-05-16': 206, '2022-05-17': 207, '2022-05-18': 208, '2022-05-19': 209, '2022-05-20': 210, '2022-05-21': 211, '2022-05-22': 212, '2022-05-23': 213, '2022-05-24': 214, '2022-05-25': 215, '2022-05-26': 216, '2022-05-27': 217, '2022-05-28': 218, '2022-05-29': 219, '2022-05-30': 220, '2022-05-31': 221, '2022-06-01': 222, '2022-06-02': 223, '2022-06-03': 224, '2022-06-04': 225, '2022-06-05': 226, '2022-06-06': 227, '2022-06-07': 228, '2022-06-08': 229, '2022-06-09': 230, '2022-06-10': 231, '2022-06-11': 232, '2022-06-12': 233, '2022-06-13': 234, '2022-06-14': 235, '2022-06-15': 236}

number_list=[0 for index in range(237)]
number_high=[0 for index in range(237)]
number_middle=[0 for index in range(237)]
date_l=range(237)
duration_list=[]

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
high_dict={}
n=0
cnt1=0
cnt2=0

def timestamp2time(stamp):
    structtime=time.localtime(stamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', structtime) 

def t2m(t):
    h,m,s = t.strip().split(":")
    return int(h) * 60 + int(m)

def get_json (mylist):
    global n
    n+=1
    timespand=mylist['duration']
    prefix=mylist['prefix']
    prefix_list.append(prefix)

    date0=timestamp2time(mylist['start_timestamp']) [0:10]
    index=date_dict[date0]

    number_list[index]+=1

    hijacker=mylist['suspicious_as']
    hijacker_list.append(hijacker)
    victim=mylist['before_as']
    victim_list.append(victim)
    prefix_len=mylist['prefix'][-2:]

    try:
        m=int(mylist['level_reason'].split()[0])
    except:
        m=mylist["websites_in_prefix"].count('www')

    yes=date0+' &'+mylist['prefix']+' &'+hijacker+' &'+victim+' &'
    high_dict[yes]=m

def get_json1(mylist):
    timespand=mylist['duration']
    duration=t2m(timespand)

    prefix=mylist['prefix']


    date0=timestamp2time(mylist['start_timestamp']) [0:10]

    level=mylist['level']

    hijacker=mylist['suspicious_as']
    victim=mylist['before_as']
    prefix_len=mylist['prefix'][-2:]
    attacker_country=mylist['suspicious_as_country']
    victim_country=mylist['before_as_country']

    yes=date0+' &'+str(duration) +' &'+prefix+' &'+hijacker+' &'+attacker_country+' &'+victim+' &'+victim_country+'\\\\'
    print(yes)
def real():
    file=open('sample_high.jsonl')
    for line in file.readlines():
        try:
            json_file=json.loads(line)
        except:
            n+=1
            print(n)
        else:
            get_json (json_file)
    
def real1():
    file=open('duration.jsonl')
    for line in file.readlines():
        json_file=json.loads(line)
        get_json1 (json_file)


real()
a=[]
highest10=sorted(high_dict.items(),key=lambda x:x[1],reverse=True)
print(highest10[:12])
# for i,v in high_dict.items():
#     a.append(v)

# print(np.mean(a))
# print(np.median(a))