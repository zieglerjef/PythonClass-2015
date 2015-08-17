from bs4 import BeautifulSoup
import urllib2
import csv
import re

web_address='http://www.europarl.europa.eu/plenary/en/minutes.html#sidesForm' #identify initial website
web_page = urllib2.urlopen(web_address)
soup = BeautifulSoup(web_page.read()) #define soup

agenda_section = soup.find_all('a',{'class':'title'}) #locate the div class that petition titles are located within and pull out the url of each petition

def clean(object): #create function to clean html
	for link in object:
		return re.sub(r'<[^>]+>', '', str(link))

def getData(object): #create function to generate petition attributes from each minutes page (Title, Published Date, Content)
	web_page = urllib2.urlopen(object) #update webpage to each individual instance's url
	soup2 = BeautifulSoup(web_page.read()) #redefine soup for each minutes' page
	motion_type = soup2.find_all('p',{'class':'contents'}) #grab petition title
	motion_date = soup2.find_all('title') #take published date
	return {"Title":clean(petition_title), "Date":clean(petition_date), "Content":clean(petition_issues)}

with open('europeanParliamentMinutes.csv', 'wb') as f: #open csv file to write to
	my_writer = csv.DictWriter(f, fieldnames=("Title", "Date", "Content")) #create dictionary w/ item names
	my_writer.writeheader() #create writeheader
	for item in petition_name: #loop through each petition instance
		my_writer.writerow(getData(item['href']))