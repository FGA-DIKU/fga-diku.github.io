# Running this file OVERWRITES the current publications.md with Mads Nielsens 100 newest google scholar articles sorted by year 

from bs4 import BeautifulSoup
from urllib.request import urlopen

# Get the html of Mads Nielsens 100 newest google scholar articles sorted by year  
with urlopen('https://scholar.google.com/citations?view_op=list_works&hl=en&hl=en&user=2QCJXEkAAAAJ&sortby=pubdate&pagesize=100') as response:
    base_url = "https://scholar.google.com"
    soup = BeautifulSoup(response, 'html.parser')
ts = soup.find_all('tr', {"class": "gsc_a_tr"}) # go to tr
ts = [t.td for t in ts] # go to first td
title_tags = [t.a for t in ts] # These tags contain title
titles = [t.text for t in title_tags]
title_urls = [base_url + t.get('href') for t in title_tags]
subtitle_tags = [t.find_all('div') for t in ts]
subtitles = [[s.text for s in t] for t in subtitle_tags]
first_sub_titles = [t[0] for t in subtitles]
second_sub_titles = [t[1][:-6] for t in subtitles]
years = [t[1][-4:] for t in subtitles]

# Filtering some articles off
idx_to_keep = []
for i in range(len(titles)):
    if "MS Nielsen" in first_sub_titles[i]:
        pass
    else:
        idx_to_keep += i,

title_tags = [title_tags[i] for i in idx_to_keep] 
titles = [titles[i] for i in idx_to_keep] 
title_urls = [title_urls[i] for i in idx_to_keep] 
subtitle_tags = [subtitle_tags[i] for i in idx_to_keep] 
subtitles = [subtitles[i] for i in idx_to_keep] 
first_sub_titles = [first_sub_titles[i] for i in idx_to_keep] 
second_sub_titles = [second_sub_titles[i] for i in idx_to_keep] 
years = [years[i] for i in idx_to_keep] 


# The top of publications.md
publications_head = """---
title: "FiGra - Publications"
layout: gridlay
excerpt: "FiGra -- Publications."
sitemap: false
permalink: /publications/
---

[//]: # (This file should be changed within the scrape_google_scholar.py file but NOT directly from the publications.md file.) 

# Publications

"""

# The list of publications formatted in separate strings
publications_list = [f"""#### [{title}]({url}) ####
{sub_one}\\
{sub_two}

<br/>

""" for title, url, sub_one, sub_two in zip (titles, title_urls, first_sub_titles, second_sub_titles)]

# Inserting the year separators into the list
year = "NaN"
for i in range(len(publications_list)):
    if year != years[i] and years[i] != '':
        string = f'\n\n<h3 style="padding-bottom: 0px;margin-bottom: 0; text-align: center;">{years[i]}</h3>\n---\n\n'
        publications_list.insert(i, string)
        year = years[i]

# Joining the list into a single string
publications = ''.join(publications_list)

with open("./_pages/publications.md", mode='w') as file:
    file.write(publications_head + publications)
