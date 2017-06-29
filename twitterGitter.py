# coding: utf-8

import sys
import os
import urllib

def doesAccountExist(webpage):
    match = "Sorry, that page "
    if  str(match) in str(webpage):
        return False
    else:
        return True

def containsLink(tweet):
    if "<a href" in tweet:
        return True
    else:
        return False

def processData(data,fileName):
    targetFile = open(fileName, 'a')
    containerOffset = 37
    tcText = "<div class=\"js-tweet-text-container\">"
    startTweet = data[data.find(tcText)+containerOffset:]
    endTweet = startTweet.find("</div>")
    tweetContainer = startTweet[0:endTweet]
    arrowOffset = 1
    tweetMsg = tweetContainer[tweetContainer.find(">")+arrowOffset:]
    if containsLink(tweetMsg):
        targetFile.write("TWEET: " + tweetMsg[0:tweetMsg.find("<a href=")].replace("&#39;","'") + "\n")
    else:
        targetFile.write("TWEET: " + tweetMsg.replace("</p>", "").replace("&#39;","'"))

    restOfData = startTweet[endTweet:]
    targetFile.close()
    if tcText in restOfData:
        processData(restOfData, fileName)


def main():
    twitter = "https://twitter.com/"
    person = sys.argv[1] 
    twitterPersonUrl = twitter + person
    webpage = urllib.urlopen(twitterPersonUrl)
    fileName = person + '.txt'


    data = webpage.read()
    if not doesAccountExist(data):
        targetFile = open(fileName, 'a')
        targetFile.write("The account " + str(person) + " does not exist.")
        targetFile.close()
        sys.exit(1)
    else:
        processData(data,fileName)

main()