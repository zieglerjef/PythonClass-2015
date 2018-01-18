import tweepy
import time
import csv
import re
import wikipedia

#access api twitter through application
auth = tweepy.OAuthHandler('d68FTuyH7HpNjgd3V3xRVsnEj', 'AtTmfOZAabROJJiwvIvO9wQmdosgYT8404QAzJWXohgUXZgblA')
auth.set_access_token('1733128674-YpKzjMAoW5D9FsQFjoMhbpXoo2XNtVcj4En5w0S', 'WAHV5Qc0hFzIO0tXeWu2EqtzX0zsq26aHUBkamCau2UGg')
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

# 	for person in mepScreenNames: #loop through each MEP screen name instance

def writeTweets(person):
	not_finished_again = True
	while not_finished_again:
		try:
			tweet_list=tweepy.Cursor(api.user_timeline, person).items()
			for tweet in tweet_list:
				not_finished = True
				while not_finished:
					try:
						tweetUser = str(tweet.user.screen_name) #define what the user's screen name is
						tweetDate = str(unicode(tweet.created_at).encode("utf-8")) #define the date that the tweet was made
						tweetContent = str(unicode(tweet.text).encode("utf-8")) #define the contents of a single tweet
						tweetLocation =str(tweet.coordinates) #define the coordinates
						tweetLanguage =str(unicode(tweet.lang).encode("utf-8")) #define the coordinates
						mepTweets.append({'Name': tweetUser, 'Date': tweetDate, 'Content': tweetContent, 'Location': tweetLocation, 'Language': tweetLanguage}) #append the list with each tweet and subsequent info
						not_finished=False
					except tweepy.TweepError:
						time.sleep(1)
			not_finished_again=False
		except tweepy.TweepError:
			time.sleep(1)

with open('mepTweets0.csv', 'wb') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, fieldnames=("Name", "Date", "Content", "Location", "Language"))
    w.writeheader()
    for item in mepTweets:
    	w.writerow(item)