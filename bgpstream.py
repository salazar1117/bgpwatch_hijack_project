import requests 
import jsonlines
from bs4 import BeautifulSoup
import chardet
import shelve
import chardet
import re
import json
import datetime
def getYesterday(): 
    yesterday = datetime.date.today() + datetime.timedelta(-1)
    return yesterday

def parse(text):
    with jsonlines.open('bgp_archive.jsonl',mode='a') as writer:
        writer.write(text)

yesterday = getYesterday()

data = open("bgpdata_22_1.json","w")

# page = shelve.open('bgp_shelve')['data']

page = requests.get("https://bgpstream.crosswork.cisco.com")
d = shelve.open("bgp_shelve")
d['data'] = page

leak_id = []
page.encoding = 'utf-8'

# print(page.text)
# ? what?
# * This is important
# ! This is alert()
chardet.detect(page.content)
# soup = BeautifulSoup(page.text,features="html.parser")

soup = BeautifulSoup(page.text,features="lxml")

abss = []
cnt = 0
rows = soup.find_all('tr')
for r in rows:
    start_time = r.find_all('td')[3].string.strip()
    start_time = re.findall(r'(\d{4})-(\d{2})-(\d{2})', start_time)
    print(start_time[0][0],start_time[0][1],start_time[0][2])
    event_date=datetime.date(int(start_time[0][0]),int(start_time[0][1]),int(start_time[0][2]))
    if event_date >= datetime.date(2022,7,5):
        continue
    if(event_date < datetime.date(2021,11,1)):
        break
    cnt+=1
    ab = {}
    if(str(r.td.string).strip() == 'Outage'):
        continue
        temp = r.find_all('td')
        event_id = temp[5].a['href'][7:]
        ab['Event ID'] = event_id
        ab['Event Type'] = "Outage"
        # ab['Country'] = 
        ab['AS'] =temp[2].string.strip()
        #print(temp[2].string.strip())
        ab['Start Time (UTC)'] =temp[3].string.strip()
        #print(temp[3].string.strip())
        ab['End Time (UTC)'] = temp[4].string.strip()
        #print(temp[4].string.strip())
        # more_info_url = 'https://bgpstream.com'+ temp[5].a['href']
        # data_url = "https://portal.bgpmon.net/bgpplay_json_wrapper.php?&eventid="+temp[5].a['href'][7:]
        # more_info = requests.get(more_info_url)


        
        # print(ab)
        # print(more_info)        
        # print(data_url)
    
    elif str(r.td.string).strip() == 'Possible Hijack':
        print(r)
        ab = {}   
        temp = r.find_all('td')
        event_id = temp[5].a['href'][7:]
        ab['Event ID'] = temp[5].a['href'][7:]
        ab['Event Type'] = "Possible Hijack"


        more_info_url = 'https://bgpstream.crosswork.cisco.com'+ temp[5].a['href']
        more_info = BeautifulSoup(requests.get(more_info_url).content.decode('utf-8'),features="lxml" )

        try:
            print('here\n')
            print(more_info.find_all('table')[0].contents)
        except:
            continue
        ss = more_info.find_all('table')[0].contents[5].td.string
        r = ss[17::]
       # r = re.findall(r'(?:\d{1,3}\.)+(?:\d{1,3})/\d{1,2}|', ss)
        if r:
            ab['Hijacked Prefix'] = r
        else:
            ab['Hijacked Prefix'] = ''

        ab['Expected Origin AS'] =str(temp[2].contents[2]).strip()

        ab['Detected Origin AS'] =str(temp[2].contents[6]).strip()

        ab['Start Time (UTC)'] =temp[3].string.strip()
 
        ab['End Time (UTC)'] = temp[4].string.strip()

##############################################################
##受影响的AS
        data_url = "https://portal.bgpmon.net/bgpplay_json_wrapper.php?&eventid="+temp[5].a['href'][7:]
        url = "https://portal.bgpmon.net/bgpplay_json_wrapper.php?&eventid="+ event_id
        response = requests.get(url)
        s =set()
        try:
            d = json.loads(response.content)
        
            expected_as = ab['Expected Origin AS']
        except:
            continue
        print(expected_as)
        for event in d['data']['events']:
            if event['type'] !="A":
                continue
            try:
                path = event['attrs']['path']
            except:
                pass
            if path[-1] != int(re.findall(r'AS (\d+)',expected_as)[0]):
                for AS in path:
                    if AS == int(re.findall(r'AS (\d+)',ab['Detected Origin AS'])[0]):
                        continue
                    s.add(AS)
        li = list(s)
        ab['Affected AS'] = li
#################################################################
        parse(ab)

        
    else:
        continue
        ab = {}
        temp = r.find_all('td')
        event_id = temp[5].a['href'][7:]
        ab['Event ID'] = temp[5].a['href'][7:]
        ab['Event Type'] = "BGP Leak"
        # print(temp[2].contents)
        # print(str(temp[2].contents[2]).strip())
        more_info_url = 'https://bgpstream.crosswork.cisco.com'+ temp[5].a['href']
        more_info = BeautifulSoup(requests.get(more_info_url).content.decode('utf-8') )
        # print(more_info)
        # print(more_info.find_all('table'))
        #print(more_info.find_all('table')[0].contents[5].td)
        #print(more_info.find_all('table')[0].contents[5].td.string[15:31])


        # 9
        try:
        
            table = more_info.find_all('table')[0]
        except:
            continue
        ss = table.contents[5].td.string
        r = ss[17::]
        ab['Leaked Prefix'] =r
        ab['Origin AS'] = str(temp[2].contents[2]).strip()
        ab['Leaker AS'] = str(temp[2].contents[6].strip())
        #print(more_info.find_all('table')[0].contents[9].td.li.string.strip())

        
        li = []
        leak_list = table.contents[9].td.find_all('li')
        for leak_as in leak_list:
            li.append(leak_as.string.strip())

        ab['Leaked To'] =li
        ab['Start Time (UTC)'] =temp[3].string.strip()
        ab['End Time (UTC)'] = temp[4].string.strip()
##############################################################
##受影响的AS
        data_url = "https://portal.bgpmon.net/bgpplay_json_wrapper.php?&eventid="+temp[5].a['href'][7:]
        url = "https://portal.bgpmon.net/bgpplay_json_wrapper.php?&eventid="+ event_id
        response = requests.get(url)
        s =set()
        d = json.loads(response.content)
        for event in d['data']['events']:
            if event['type'] !="A":
                continue
            try:
                path = event['attrs']['path']
        
                for leak_as in li:
                    leakedTo = re.findall(r'(\d+)',leak_as)[0]
                    print(leakedTo)
                    try:
                        if int(leakedTo) in path:
                            index = path.index(int(leakedTo))
                            for i in range(index+1):
                                s.add(path[i])
                    except:
                        pass
            except:
                pass
        li = list(s)
        ab['Affected AS'] = li
###################################################################
        
    abss.append(ab)

data.close()