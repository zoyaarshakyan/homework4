
# coding: utf-8

# In[7]:

import json
import requests
    from BeautifulSoup import *


# In[9]:

url="https://www.youtube.com/feed/trending"
response = requests.get(url)
page= response.text
soup=BeautifulSoup(page)


# In[10]:

a_tags=soup.findAll('a', attrs={'class':"yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link "})
duration = soup.findAll('span', attrs={'class': 'video-time'})
username = soup.findAll('a', attrs={'class': 'g-hovercard yt-uix-sessionlink       spf-link '})
views = soup.findAll("ul", attrs={ 'class':"yt-lockup-meta-info", } ) 


# In[12]:

list1=[]
for i in views:
    for j in i:
        list1.append(j.text)
elements=list1[1::2]
list2=[]
for i,j,y,x in zip(a_tags,duration,username,elements):
    list2.append({'Title ' :i.get("title"),"URL" : "https://www.youtube.com"+i.get('href'),'Duration':j.text,"Username":z.text,"Views": x})
print(list2)
with open('trendingmovies.json', 'w') as output:
    json.dump(list2, output, sort_keys = True, indent = 4)


import unicodecsv as csv

with open('trendingmovies.csv', 'w') as csv_file:
    for i in list2:
            writer = csv.writer(csv_file)
            for y, x in i.items():
                writer.writerow([y, x])
            writer.writerow([])


# In[13]:

import json

with open('trendingmovies.json') as json_data:
    file1 = json.load(json_data)
    print(file1)


# In[14]:

from pprint import*
pprint(file1)


# In[ ]:



