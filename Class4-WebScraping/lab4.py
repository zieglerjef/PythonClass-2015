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
soup = BeautifulSoup(web_page.read()) #define soup
faculty_names = soup.find_all('a',{'class':'person-view-primary-field'}) #find the url associated with each faculty member by locating <ahref> within class

def find_email(object): #create function to find @ symbol within faculty_attributes
	for link in object:
		if '@' in re.sub(r'<[^>]+>', '',str(link)): return re.sub(r'<[^>]+>', '',str(link))

def getData(object,k): #create function to create faculty_attributes (Name, Title, Email, Webpage)
	web_page = urllib2.urlopen(object)
	soup = BeautifulSoup(web_page.read()) #define soup
	faculty_attributes = soup.find_all('div',{'class':'field-item even'})
	return {"Name":re.sub(r'<[^>]+>', '', str(soup.find_all("h1",{'class':'pane-title'})[0])), "Title":re.sub(r'<[^>]+>', '', str(faculty_names[k].parent.parent.contents[-1])), "Email":find_email(faculty_attributes), "Webpage":object}

with open('faculty_attributes.csv', 'wb') as f: #loop to fill in each key within dict for each faculty member on faculty site
	my_writer = csv.DictWriter(f, fieldnames=("Name", "Title", "Email", "Webpage"))
	my_writer.writeheader()
	k=0 #instance for each faculty members
	for i in faculty_names:
		my_writer.writerow(getData('https://polisci.wustl.edu'+i['href'],k))
		k+=1