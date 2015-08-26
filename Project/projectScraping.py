from bs4 import BeautifulSoup
import urllib2
import csv
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def findContent(items): #create function to find @ symbol within faculty_attributes
	for table in items:
		if 'Minutes' in str(table): return str(unicode(table.get_text()).encode("utf-8")) 

def removeDuplicates(seq, idfun=None): 
	if idfun is None:
		def idfun(x): return x
	seen = {}
	result = []
	for item in seq:
		marker = idfun(item)
		if marker in seen: continue
		seen[marker] = 1
		result.append(item)
	return result

EPMinutes = []
EPDocuments = []

def getData(items): #create function to generate petition attributes from each minutes page (Title, Published Date, Content)
	web_page = urllib2.urlopen(items)
	soup = BeautifulSoup(web_page.read())
	table = soup.find('table',{'class':'doc_box_header'})
	for row in table.find_all('tr'):
		agendaLinks = table.find_all('a')[1:]
	debateLinks = []
	for links in agendaLinks:
		if '(debate)' in str(links): debateLinks.append(links)
	for debates in debateLinks:
		web_page2 = urllib2.urlopen('http://www.europarl.europa.eu' + debates['href']) #update webpage to each individual instance's url
		soup2 = BeautifulSoup(web_page2.read()) #redefine soup for each minutes' page
		sections = soup2.find_all('table',{'class':''})
		agenda = findContent(sections.pop(0)).split("Minutes",1)[1] #find table with Minutes
		agendaDate = unicode(agenda.split("Final", 1)[0]).encode("utf-8")
		agendaContent = unicode(agenda.split("edition", 1)[1]).encode("utf-8")
		if 'procedure:' in str(agendaContent):
			catch = str(re.split(r"\w+ye' procedure:", agendaContent)[1])
		else: catch = 'NA'
		EPMinutes.append({"Date":agendaDate, "Catch the Eye":str(re.split(r"\.", catch)[0]), "Content":agendaContent})	
		# oralProceeding=[]
# 		for url in soup2.find_all('a',{'class':'ring_ref_link'}):
# 			if 'O-' in url:
# 				oralProceeding.append(removeDuplicates(url)['href'])
# 			else: pass
# 		for content in oralProceeding:
# 			web_page3 = urllib2.urlopen('http://www.europarl.europa.eu' + re.sub('amp;', '', content['href']))
# 			soup3 = BeautifulSoup(web_page3.read()) #redefine soup for each minutes' page
# 			sections2 = soup3.find_all('table',{'class':''})
# 			if 'Subject:' in str(sections2):
# 				oralQuestion = str(re.split(r"\w Subject:", sections2)[1])
# 			else: pass
# 			if 'Catch-the-eye procedure' in str(sections2):
# 				oralCatch = findContent(sections2.pop(0)).split("Catch-the-eye",1)[1]
# 			else: oralCatch = 'NA'
# 			oralCatch = unicode(oralCatch.split("catch-the-eye", 1)[0]).encode("utf-8")
# 			EPDocuments.append({"Catch the Eye":oralCatch})	
	nextTable = soup.find('table',{'class':'buttondocwin'})
	for row in nextTable.find_all('tr'):
		print row
		nextButton = nextTable.find_all('a')[1:]
	for links in nextButton:
		print links
		web_address2 = 'http://www.europarl.europa.eu' + links['href']
	print web_address2
	getData(web_address2)	

web_address='http://www.europarl.europa.eu/sides/getDoc.do?pubRef=-//EP//TEXT+PV+20140417+TOC+DOC+XML+V0//EN&language=EN' #identify initial website

getData(web_address)

with open('europeanParliamentMinutes.csv', 'wb') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, fieldnames=("Date", "Catch the Eye", "Content"))
    w.writeheader()
    for item in EPMinutes:
    	w.writerow(item)