# Go to https://petitions.whitehouse.gov/petitions
# • Go to the petition page for each of the petitions.
# • Create a .csv file with the following information for each petition:
# – Title
# – Published date
# – Issues
# – Number of signatures

from bs4 import BeautifulSoup
import urllib2
import csv
import re

web_address='https://petitions.whitehouse.gov/petitions' #identify initial website
web_page = urllib2.urlopen(web_address)
soup = BeautifulSoup(web_page.read()) #define soup

petition_name = [div.a for div in soup.find_all('div',{'class':'title'})] #locate the div class that petition titles are located within and pull out the url of each petition

def clean(object): #create function to clean html
	for link in object:
		return re.sub(r'<[^>]+>', '', str(link))

def getData(object): #create function to generate petition attributes from each petition page (Title, Published Date, Issues, # of signatures)
	web_page = urllib2.urlopen(object) #update webpage to each individual instance's url
	soup2 = BeautifulSoup(web_page.read()) #redefine soup for each petition instance
	petition_title = soup2.find_all('h1',{'class':'title'}) #grab petition title from h1 class
	petition_date = soup2.find_all('div',{'class':'date'}) #take published date from date div
	petition_issues = soup2.find_all('div',{'class':'issues'}) #take issues from issues div
	petition_signatures = soup2.find_all('div',{'class':'num-block num-block2'}) #take signatures from div
	return {"Title":clean(petition_title), "Date":clean(petition_date), "Issues":clean(petition_issues), "Signatures":clean(petition_signatures)}

with open('petition_attributes.csv', 'wb') as f: #open csv file to write to
	my_writer = csv.DictWriter(f, fieldnames=("Title", "Date", "Issues", "Signatures")) #create dictionary w/ item names
	my_writer.writeheader() #create writeheader
	for item in petition_name: #loop through each petition instance
		my_writer.writerow(getData(item['href']))
		
f.close()