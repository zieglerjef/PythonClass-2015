import tweepy
import time
import csv
import re
import wikipedia

#access api twitter through application
auth = tweepy.OAuthHandler('###', '###')
auth.set_access_token('###', '###')
api = tweepy.API(auth)

#open csv file to read names of MEPs
mepNames=[] #create list to hold MEP names
reader = csv.reader(open('mepNames.csv', 'U'), dialect='excel') #read MEP names in from csv file
for row in reader: #read in names to list
    mepNames.append(row)

#open list that will include each twitter user's screen name
mepScreenNames=[] #create list to hold MEP screen names
for item_name in mepNames: #generate loop to match search name with MEP name in list mepNames
	try:
		if str(api.search_users(item_name)[0].name).lower() == re.search(r'\[\'(.*?)\'\]', str(item_name).lower()).group(1):
			mepScreenNames.append(str(api.search_users(item_name)[0].screen_name))
		else: pass #if there isn't a match, pass
	except: #general exception raised, timeout
		time.sleep(1)

mepTweets = [] #create object for each instance of a tweet by a single MEP
def writeTweets(item):
	tweet_list=tweepy.Cursor(api.user_timeline, item, since='2009-07-14', until='2014-07-01').items()
	for tweet in tweet_list: #grab all items on a single user's timeline
		try:
			tweetUser = str(tweet.user.screen_name) #define what the user's screen name is
			tweetDate = str(unicode(tweet.created_at).encode("utf-8")) #define the date that the tweet was made
			tweetContent = str(unicode(tweet.text).encode("utf-8")) #define the contents of a single tweet
			mepTweets.append({'Name': tweetUser, 'Date': tweetDate, 'Content': tweetContent}) #append the list with each tweet and subsequent info
		except tweepy.TweepError:
			time.sleep(1)
        	writeTweets(item)
	
def combineTweets(item):
	try:
		writeTweets(person)
	except tweepy.TweepError:
		time.sleep(1)
       	combineTweets(person)
       	
for person in mepScreenNames: #loop through each MEP screen name instance
	combineTweets(person)

with open('mepTweets.csv', 'wb') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, fieldnames=("Name", "Date", "Content"))
    w.writeheader()
    for item in mepTweets:
    	w.writerow(item)