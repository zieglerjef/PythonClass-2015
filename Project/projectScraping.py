from bs4 import BeautifulSoup
import urllib2
import csv
import re

web_address='http://www.europarl.europa.eu/sides/getDoc.do?type=PV&reference=20140417&secondRef=TOC&language=EN' #identify initial website
web_page = urllib2.urlopen(web_address)
soup = BeautifulSoup(web_page.read()) #define soup

table = soup.find('table',{'class':'doc_box_header'})
for row in table.find_all('tr'):
	agendaLinks = table.find_all('a')[1:]

def clean(object): #create function to clean html
	for link in object:
		return re.sub(r'<[^>]+>', '', str(link))

def getData(items): #create function to generate petition attributes from each minutes page (Title, Published Date, Content)
	web_page = urllib2.urlopen(items) #update webpage to each individual instance's url
	soup2 = BeautifulSoup(web_page.read()) #redefine soup for each minutes' page
	sections = soup2.find_all('table',{'class':'doc_box_header'}) #grab petition title
	agendaContent = sections.find_all('td')	
	print agendaContent
	return {"Date":clean(agendaDate)}

with open('europeanParliamentMinutes.csv', 'wb') as f: #open csv file to write to
	my_writer = csv.DictWriter(f, fieldnames=("Title", "Date", "Content")) #create dictionary w/ item names
	my_writer.writeheader() #create writeheader
	for item in petition_name: #loop through each petition instance
		my_writer.writerow(getData(item['href']))