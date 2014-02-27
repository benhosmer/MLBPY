#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
from bs4 import BeautifulSoup

url = "http://www.meetup.com/Melbourne-Makerspace-Florida-USA"

data = urllib.urlopen(url).read()

assert isinstance(data, object)
soup = BeautifulSoup(data)


upcoming_meetups = {}

meetup_title = soup.find_all('span', {'itemprop': 'summary'})
meetup_date = soup.find_all('span', {'class': 'date'})
meetup_time = soup.find_all('span', {'class': 'time'})

upcoming_meetups = dict(zip(meetup_title, dict(zip(meetup_date, meetup_time))))
print upcoming_meetups


