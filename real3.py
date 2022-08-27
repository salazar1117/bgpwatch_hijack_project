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
number_list0=[0 for index in range(237)]
number_high=[0 for index in range(237)]
number_middle=[0 for index in range(237)]

date_l=range(237)
duration_list=[]
country_dict=json.load(open('country_dict_1.json'))

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
cnt=0
xx=set()
yy=set()
def parse(text):
    with jsonlines.open('case1.jsonl',mode='a') as writer:
        writer.write(text)
def parse1(text):
    with jsonlines.open('real11.jsonl',mode='a') as writer:
        writer.write(text)
def parse2(text):
    with jsonlines.open('real12.jsonl',mode='a') as writer:
        writer.write(text)
def timestamp2time(stamp):
    structtime=time.localtime(stamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', structtime) 

def get_json (mylist):
    global n,cnt
    timespand=mylist['duration']
    duration=t2m(timespand)

    duration_list.append(duration)
    prefix=mylist['prefix']
    prefix_list.append(prefix)

    date0=timestamp2time(mylist['start_timestamp']) [0:10]
    index=date_dict[date0]

    number_list[index]+=1

    if mylist['level']=='high':
        number_high[index]+=1
    
    if mylist['level']=='middle':
        number_middle[index]+=1

    hijacker=mylist['suspicious_as']
    hijacker_list.append(hijacker)
    victim=mylist['before_as']
    victim_list.append(victim)
    prefix_len=mylist['prefix'][-2:]
    victim_country=mylist['before_as_country']
    hijacker_country=mylist['suspicious_as_country']
    if victim_country=='' or hijacker_country=='':
        if victim in country_dict:
            victim_country=country_dict[victim]
        if hijacker in country_dict:
            hijacker_country=country_dict[hijacker]
        if victim_country=='' or hijacker_country=='':
            xx.add(victim+','+victim_country+','+ hijacker+','+hijacker_country)
        if victim_country=='':
            yy.add(victim)
        if hijacker_country=='':
            yy.add(hijacker)

    if victim not in victim_set:
        victim_set.add(victim)
        victim_country_list.append(victim_country)

    if hijacker not in hijacker_set:
        hijacker_set.add(hijacker)
        attacker_country_list.append(hijacker_country)

def get_json1(mylist):
    date0=timestamp2time(mylist['start_timestamp']) [0:10]
    replay=mylist['replay']
    all_vp=[]
    affected_as=[]
    hijacker=mylist['suspicious_as']
    victim=mylist['before_as']

    for tm in replay:
        pathlist=replay[tm]['path_list']
        for path in pathlist:
            path_tmp=list(dict.fromkeys(path.split()))
            all_vp.append(path_tmp[0])
            if path_tmp[-1]==hijacker:
                affected_as.append(path_tmp[0])

    all_vp=list(dict.fromkeys(all_vp))
    affected_as=list(dict.fromkeys(affected_as))
    len_all_vp=str(len(all_vp))
    len_affected_as=str(len(affected_as))

    if hijacker+' '+date0 not in affected_dict:
        affected_dict[hijacker+' '+date0]=[]
        affected_dict1[hijacker+' '+date0]=[]
        affected_dict2[hijacker+' '+date0]=[]

    rate_affected=len_affected_as+':'+len_all_vp
    affected_dict[hijacker+' '+date0].append(rate_affected)
    affected_dict1[hijacker+' '+date0]+=all_vp
    affected_dict2[hijacker+' '+date0]+=affected_as

def draw_number ():
    plt.figure(figsize=(14,7))
    plt.plot(date_list, number_list,label='total')
    plt.plot(date_list,number_high,label='high level')
    plt.plot(date_list, number_middle,label='middle level')
    plt.ylim(0,2650)
    plt.xlim(0,225)
    plt.xlabel("date")
    plt.ylabel("amount")
    plt.yscale('symlog')
    plt.xticks(range(12,len(date_list),30),rotation=35,fontsize=8)
    plt.legend()
    plt.grid(True)
    plt.title("hijack event")
    plt.savefig('attack_year_0.png')

def draw2y():
    fig=plt.figure()
    ax1=fig.add_subplot(111)
    pl2=ax1.plot(date_list, number_middle,color='slateblue',label='middle level')
    pl1=ax1.plot(date_list,number_high,'r',label='high level')
    #ax1.legend(loc=1)
    ax1.set_ylabel('amount',color='slateblue')
    ax1.set_xlabel('date')
    ax1.set_ylim(0,265)
    #ax1.set_ylim(0,52)

    for tl in ax1.get_xticklabels():
        tl.set_rotation(30)
        tl.set_fontsize(8)

    for tl in ax1.get_yticklabels():
        tl.set_color('slateblue')

    ax2=ax1.twinx()
    pl3=ax2.plot(date_list, number_list,'--',color='pink',label='total amount')
    #ax2.legend(loc=2)
    ax2.set_ylabel('total amount',color='hotpink')
    ax2.set_ylim(0,2650)
    #ax2.set_ylim(0,520)
    for tl in ax2.get_yticklabels():
        tl.set_color('hotpink')
    
    plt.xlim(0,225)
    plt.xticks(range(12,len(date_list),30),rotation=35,fontsize=1)
    ax1.grid(axis='both',linestyle='-.')
    plt.title("hijack event of middle/high level")
    pl=pl1+pl2+pl3
    labs=[l.get_label() for l in pl]
    ax1.legend(pl,labs,loc=1,fontsize=10)
    plt.show()
    plt.savefig('attack_year_1.png')

def t2s(t):
    h,m,s = t.strip().split(":")
    return int(h) * 3600 + int(m) * 60 + int(s)
def t2m(t):
    h,m,s = t.strip().split(":")
    return int(h) * 60 + int(m) 


def draw_cdf():

    count0 = Counter(duration_list)
    totalnumber=sorted(count0.items(),key=lambda x:x[0])

    x=range(0,3003)
    y=[0 for index in range(3003)]

    for i,v in totalnumber:
        y[i]=v

    pdf=y/np.sum(y)
    cdf=np.cumsum(pdf)

    plt.plot(x, cdf)
    plt.xlim(0,3003)
    plt.ylim(0,1)
    plt.xlabel("symlog of duration/min")
    plt.ylabel("probability value")
    plt.title("cdf of hijack duration")
    plt.xscale('symlog')
    plt.grid(True)
    plt.show()
    plt.savefig('duration_cdf_log.png')

def number_cdf_date():

    pdf1=number_high/np.sum(number_high)
    cdf1=np.cumsum(pdf1)

    pdf2=number_middle/np.sum(number_middle)
    cdf2=np.cumsum(pdf2)

    plt.figure()
    plt.plot(date_list, cdf1,label='high level')
    plt.plot(date_list, cdf2,label='middle level')
    #plt.plot(date_list,number_high,label='high level')
    #plt.plot(date_list, number_middle,label='middle level')
    plt.ylim(0,1)
    plt.xlim(0,225)
    plt.xlabel("date")
    plt.ylabel("probability values")
    plt.xticks(range(12,len(date_list),30),rotation=35,fontsize=8)
    plt.legend()
    plt.grid(True)
    plt.title("cdf of high/middle level hijack event")
    plt.savefig('attack_cdf.png')

def number_cdf_amount():

    count1 = Counter(number_high[:223])
    totalnumber1=sorted(count1.items(),key=lambda x:x[0])

    count2 = Counter(number_middle[:223])
    totalnumber2=sorted(count2.items(),key=lambda x:x[0])

    count0 = Counter(number_list[:223])
    totalnumber0=sorted(count0.items(),key=lambda x:x[0])

    x=range(2610)
    y=[0 for index in range(2610)]
    z=[0 for index in range(2610)]
    t=[0 for index in range(2610)]
    for i,v in totalnumber1:
        y[i]=v
    for i,v in totalnumber2:
        z[i]=v
    for i,v in totalnumber0:
        t[i]=v

    pdf1=y/np.sum(y)
    cdf1=np.cumsum(pdf1)

    pdf2=z/np.sum(z)
    cdf2=np.cumsum(pdf2)

    pdf0=t/np.sum(t)
    cdf0=np.cumsum(pdf0)

    plt.plot(x, cdf1,label='high level')
    plt.plot(x, cdf2,label='middle level')
    plt.plot(x, cdf0,label='total event')
    plt.xlim(0,2610)
    plt.ylim(0,1)
    plt.xlabel("amount per day")
    plt.ylabel("probability value")
    plt.title("symlog of hijack event amount cdf")
    plt.xscale('symlog')
    plt.grid(True)
    plt.legend()
    plt.show()
    plt.savefig('number_cdf.png')

def prefix_length_cdf():
    global cnt1
    prefix_list1=[]
    prefix_list2=[]
    prefix_list1=list(dict.fromkeys(prefix_list))
    for i in prefix_list1:
        cnt1+=1
        prefix_len=int(i[-2:])
        prefix_list2.append(prefix_len)
    count1 = Counter(prefix_list2)
    prefix_dict=sorted(count1.items(),key=lambda x:x[0])

    len=[0 for index in range(50)]
    for i,v in prefix_dict:
        len[i]=v

    plt.bar(range(50),len)
    ax = plt.gca()
    plt.xlabel("prefix length")
    plt.ylabel("amount")
    plt.title("pdf of prefix_length")
    plt.show()
    plt.savefig('prefix_length_bar_1.png')

    print(cnt1)
    print('prefix length:')
    print(prefix_dict)

def victim_cdf():

    count0 = Counter(victim_list)
    totalnumber0=sorted(count0.items(),key=lambda x:x[1])
    count1 = Counter(hijacker_list)
    totalnumber1=sorted(count1.items(),key=lambda x:x[1])

    count0=[0 for index in range(4201)]
    count1=[0 for index in range(4201)]
    for i,v in totalnumber0:
        count0[v]+=1
    for i,v in totalnumber1:
        count1[v]+=1
    
    pdf0=count0/np.sum(count0)
    cdf0=np.cumsum(pdf0)

    pdf1=count1/np.sum(count1)
    cdf1=np.cumsum(pdf1)
    
    x=range(4201)

    plt.plot(x, cdf0,label='victim ASn')
    plt.plot(x, cdf1,label='hijacker ASn')
    plt.xlim(0,4201)
    plt.ylim(0,1)
    plt.xlabel("frequency per ASn")
    plt.ylabel("probability value")
    plt.title("symlog of ASn frequency cdf")
    plt.xscale('symlog')
    plt.grid(True)
    plt.legend()
    plt.show()
    plt.savefig('frequency_cdf.png')    

def real():
    file=open('selected_fh2.jsonl')
    for line in file.readlines():
        try:
            json_file=json.loads(line)
        except:
            n+=1
            print(n)
        else:
            get_json (json_file)

def affected_as():
    affected_rate=json.load(open('real3.json'))
    affected_list=[]
    affected_dict={}
    affected_number=[0 for index in range(55)]
    for i in affected_rate:
        j=i.split(':')
        if int(j[1])==0:
            continue
        affected_list.append(int(j[-1]))

    count1 = Counter(affected_list)
    affected_dict=sorted(count1.items(),key=lambda x:x[0])
    
    lll=[0,0,0,0,0,0]
    for i,v in affected_dict:
        lll[i//10]+=v
        affected_number[i]=v
    print(lll)

    pdf1=affected_number/np.sum(affected_number)
    cdf1=np.cumsum(pdf1)

    plt.plot(range(55),cdf1)
    plt.xlabel("affected_AS")
    plt.ylabel("probability value")
    plt.title("symlog of affected AS amount cdf")
    plt.grid(True)
    plt.xlim(0,53)
    plt.ylim(0,1)
    plt.xscale('symlog')
    plt.show()
    plt.savefig('cdf_affected.png')

def affected_as_1():
    hijacker_list=[]
    hijacker_dict={}
    affected_list0=[]
    affected_list1=[]
    affected_dict={}
    affected_dict=json.load(open('real32.json'))
    mydict={}
    cnt=0
    for i,v in affected_dict.items():
        for j in v:
            j=j.split(':')
            if int(j[0])==0:
                cnt+=1

    print(cnt)

real()

# aaa=''
# for i in yy:
#     aaa+=('\"'+str(i)+'\"'+': \"\", ')
# print(aaa)

# a={}
# b=[]
# c=['2021-10-23', '2021-11-16', '2021-11-29', '2021-12-11', '2022-01-05', '2022-01-13', '2022-02-17', '2022-03-08', '2022-03-09', '2022-03-11', '2022-03-22', '2022-04-06', '2022-04-20', '2022-06-01', '2021-11-09', '2021-11-17', '2021-11-24', '2021-12-20', '2022-01-08', '2022-05-04']
# for i in c:
#     print(number_list[date_dict[i]])

# for i in number_high:
#     if i==0:
#         continue
#     b.append(i)

# print(number_high)

# for i,v in zip(date_list,number_high):
#     if v==0:
#         continue
#     a[i]=v

# highest10=sorted(a.items(),key=lambda x:x[1],reverse=True)
# print(highest10[:10])

# print(np.var(duration_list))
# #print(np.var(number_high[:223]))
# print(np.mean(duration_list))
# print(np.median(duration_list))
# print('finish')