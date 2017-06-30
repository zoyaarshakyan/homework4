
# coding: utf-8

# In[1]:

import json
import urllib2
from lxml import html


# In[2]:

url = "https://www.youtube.com/feed/trending"
response = urllib2.urlopen(url)
page = response.read()
tree = html.document_fromstring(page)
title = tree.cssselect('[class="yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link "] ')
link= tree.cssselect('[class="yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link "]')
duration=tree.cssselect('[class="video-time"]')
username=tree.cssselect('[class="g-hovercard yt-uix-sessionlink       spf-link "]')
views = tree.cssselect('[class="yt-lockup-meta-info"] ' ) 
list1=[]
for i in views:
    for j in i:
        list1.append(j.text)
elements=list1[1::2]
list2=[]
for i,j,z,a,b in zip(title,duration,link,username,elements):
    list2.append({'Title ' :i.get("title"),"URL" : "https://www.youtube.com"+a.get('href'),'Duration':j.text,"Username":z.text,"Views": b})
print(list2)

with open('trendingmovies_urllib.json', 'w') as output:
    json.dump(list2, output, sort_keys = True, indent = 4)


import unicodecsv as csv

with open('trendingmovies_urllib.csv', 'w') as csv_file:
    for i in list2:
            writer = csv.writer(csv_file)
            for z, x in i.items():
                writer.writerow([z, x])
            writer.writerow([])


# In[3]:

import json

with open('trendingmovies.json') as json_data:
    file1 = json.load(json_data)
    print(file1)


# In[4]:

from pprint import*
pprint(file1)


# In[ ]:



