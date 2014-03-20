#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup


url = "http://www.meetup.com/Melbourne-Makerspace-Florida-USA"

request = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })
data = urllib2.urlopen(request).read()

assert isinstance(data, object)
soup = BeautifulSoup(data)


upcoming_meetups = {}

meetup_title = soup.find_all('span', {'itemprop': 'summary'})
meetup_date = soup.find_all('span', {'class': 'date'})
meetup_time = soup.find_all('span', {'class': 'time'})

# Zip it all up in to a nice workable dicitonary.
upcoming_meetups = dict(zip(meetup_title, dict(zip(meetup_date, meetup_time))))
print upcoming_meetups

#Extract the text between the tags
print [str(x.get_text()) for x in meetup_title]


