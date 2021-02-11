import GetOldTweets3 as got
import csv

#column names in csv
columns = ['text','date']
#setting no of tweets:
a=1000

#tags : #covid19Gr,

keywords_gr=['#Ρομα','#κορωναιος','#covid19greece']
keywords_en = ['#COVID19','#COVID-19','#coronavirus','#Covid_19']

###--------TWEETS IN GREEK LANGUAGE---------------###

with open('ncov19 tweets/tweets_greek.csv','a',newline='',encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=columns)
    #writer.writeheader()
    
    for k in keywords_gr :
        tweetCriteria = got.manager.TweetCriteria().setQuerySearch(k).setMaxTweets(a)\
                                                    .setNear("Greece")\
                                                    #.setSince("2020-03-21")\
                                                    #.setTopTweets(True)
                                                   #.setUntil('2020-03-11')\
                                                   
                
        tweet = got.manager.TweetManager.getTweets(tweetCriteria)

        for i in range(len(tweet)):
            date = str(tweet[i].date)
            date = date.split()
            text = tweet[i].text
            print(i,text,date[0])
            writer.writerow({'text' : text,'date' :str(date[0])}) #write entry to .csv file


###--------TWEETS IN ENGLISH LANGUAGE---------------###

with open('ncov19 tweets/tweets_english.csv','a',newline='',encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=columns)
    #writer.writeheader()

    for k in keywords_en :

        tweetCriteria = got.manager.TweetCriteria().setQuerySearch(k)\
                                                   .setMaxTweets(a)\
                                                   .setTopTweets(True)
                
        tweet = got.manager.TweetManager.getTweets(tweetCriteria)

        for i in range(len(tweet)):
            date = str(tweet[i].date)
            date = date.split()
            text = tweet[i].text
            print(i,text,date[0])
            writer.writerow({'text' : text,'date' :str(date[0])}) #write entry to .csv file
            

        


