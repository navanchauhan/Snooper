import praw
import readability
import os
import time
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def donotcolourmeplease():
	global red, yellow, green, purple, white, reset, blue
	red = ""
	green = ""
	yellow = ""
	purple = ""
	white = ""
	reset = ""
	blue = ""

def colourmeplease():
	global red, purple, green, yellow, white, reset, blue
	red = "\033[1;31m"
	green = "\033[1;32m"
	blue = "\033[1;34m"
	yellow = "\033[1;33m"
	purple = "\033[1;35m"
	white = "\033[1;37m"
	reset = "\033[39m"



analyser = SentimentIntensityAnalyzer()

reddit = praw.Reddit(client_id='0YYkleuCm6H9yQ', client_secret='aljmxJ3YbkDheiEt8KknwpsKVqo',  user_agent='Snooper by navanchauhan')

username = "PrudentWish"

redditor = reddit.redditor(username)


def getCommentsKarma():
	commentsKarma = redditor.comment_karma
	return commentsKarma
def getPostsKarma():
	postsKarma = redditor.link_karma
	return postsKarma
def getComments():
	comments = [  ]
	for i in redditor.comments.new(limit=1000):
		ib = i.body
		comments.append(ib)
	return comments
def getPosts():
	posts = [ ]
	for i in redditor.submissions.new(limit=1000):
		posts.append(i)
	return posts

def isMod():
	answer = redditor.is_mod
	print(white, "Is Mod?", yellow, answer, reset)
def isEmployee():
	answer = redditor.is_employee
	print(white, "Is Employee?", yellow, answer, reset)
def isgold():
	answer = redditor.is_gold
	print(white, "Gilded Currently?", yellow, answer, reset)
def hasVerifiedEmail():
	answer = redditor.has_verified_email
	print(white, "Veriefied Email?", yellow, answer, reset)
def createdOn():
	answer = redditor.created_utc
	answer = time.ctime(answer)
	print(white, "Account Created On:", yellow, answer, reset)

def performMagic():
	comments = []
	scores = []
	text = ""
	for i in redditor.comments.top(limit=1000):
		txt = i.body
		comments.append(txt)
		text += str(", " + i.body)
		score = i.score
		scores.append(score)
	print(white, "Most Downvoted Comment: \n", red, comments[-1], white, "\nScore: \n", red, scores[-1], reset)
	print(white, "Most Upvoted Comment: \n", yellow, comments[0], white, "\nScore: \n", yellow, scores[0], reset) 
	results = readability.getmeasures(text, lang='en')
	print(white, "Reading Ease: ", yellow, results['readability grades']['FleschReadingEase'], reset)
	score = analyser.polarity_scores(text)
	lb = score['compound']
	print(white, "Sentiment Analysis", reset)
	if(lb >= 0.75):
		print(blue, "Cheerful Person", reset)
	elif(lb >= 0.45):
		print(purple, "Neutral boi", reset)
	else:
		print(red, "Depressed Soul", reset)

def printDetails():
	print(username.center(100))
	print("Karma Breakdown")
	print("Comments:", redditor.comment_karma)
	print("Posts:", redditor.link_karma)
	allcomments = []
	for comments in redditor.comments.new(limit=1000):
		allcomments.append(allcomments)
	print("No. of Comments:", len(allcomments))
	allposts = []
	for posts in redditor.submissions.new(limit=1000):
		allposts.append(allposts)
	print("No. of Posts:", len(allposts))


#printDetails()
def calculateEtPrint():
	print(purple)
	print(username.center(100))
	print(reset)
	commentsKarma = getCommentsKarma()
	postsKamra = getPostsKarma()
	Comments = getComments()
	Posts = getPosts()
	AvgCommentKarma = commentsKarma/len(Comments)
	AvgPostKarma = postsKamra/len(Posts)
	print(white, "Total Karma from Comments: ", yellow, commentsKarma, reset)
	print(white, "TotaL Karma from Posts:", yellow,  postsKamra, reset)
	print(white, "Avg. Posts Karma:", yellow, AvgPostKarma, reset)
	print(white, "Avg. Comments Karma", yellow, AvgCommentKarma, reset)
	isMod()
	isEmployee()
	isgold()
	createdOn()
	performMagic()

if(os.name == "posix" or "darwin" or "linux"):
	colourmeplease()
else:
	donotcolourmeplease()

#result()
calculateEtPrint()



