#Go to https://polisci.wustl.edu/faculty/specialization
#Go to the page for each of the professors.
# Create a .csv file with the following information for each professor:
# 	-Specialization
# 	-Name
# 	-Title
# 	-E-mail
# 	-Web page

from bs4 import BeautifulSoup
import urllib2 
import random
import time
import os
import csv
import re

web_address='https://polisci.wustl.edu/faculty/specialization' #identify initial website
web_page = urllib2.urlopen(web_address)
soup = BeautifulSoup(web_page.read())
faculty_names = soup.find_all('a',{'class':'person-view-primary-field'}) #find the url associated with each faculty member

def find_email(object):
	for link in object:
		if '@' in re.sub(r'<[^>]+>', '',str(link)): return re.sub(r'<[^>]+>', '',str(link))

def getData(object,k):
	web_page = urllib2.urlopen(object)
	soup = BeautifulSoup(web_page.read())
	faculty_attributes = soup.find_all('div',{'class':'field-item even'})
	return {"Name":re.sub(r'<[^>]+>', '', str(soup.find_all('h1',{'class':'pane-title'})[0])), "Title":re.sub(r'<[^>]+>', '', str(faculty_names[k].parent.parent.contents[-1])), "Email":find_email(faculty_attributes), "Webpage":object}

with open('faculty_attributes.csv', 'wb') as f:
	my_writer = csv.DictWriter(f, fieldnames=("Name", "Title", "Email", "Webpage"))
	my_writer.writeheader()
	k=0
	for i in faculty_names:
		my_writer.writerow(getData('https://polisci.wustl.edu'+i['href'],k))
		k+=1
#		getData() #loop through strong classes and obtain url for each faculty member
		