import feedparser
import csv
import re




greek_rss_feeds=["https://www.newsit.gr/feed/","https://www.newsbeast.gr/feed","http://feeds.feedburner.com/skai/Uulu","http://feeds.feedburner.com/skai/aqOL",
            "https://www.ert.gr/feed/",'https://www.kathimerini.gr/rss','https://www.euro2day.gr/rss.ashx?catid=121','https://www.naftemporiki.gr/rssFeed',
           'https://www.news.gr/rss.ashx','https://www.real.gr/teleutaies_eidiseis/rss/',
           'https://www.efsyn.gr/feed.xml', 'https://tvxs.gr/feeds/all/feed.xml']


english_rss_feeds = [
                    'https://rss.nytimes.com/services/xml/rss/nyt/World.xml',
                    'http://feeds.bbci.co.uk/news/world/rss.xml',
                     'https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/section/world/rss.xml',
                     'https://www.aljazeera.com/xml/rss/all.xml',
                     'https://www.theguardian.com/world/rss',
                     'https://www.buzzfeed.com/world.xml',
                     'https://www.rt.com/rss/news/']

# greek rss scraping
try : 
    with open('feeds/rss_feed_greek.csv','a',newline='',encoding='utf-8') as f:
        columns =['title','date','summary','link']
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()


        for i in greek_rss_feeds :
            feed = feedparser.parse(i)
            print(feed[ "channel" ]["title"])
            #print('\n')
            
            for item in feed['items'] :
                    title = item["title"].strip()
                    print(title)
                    link=item["link"]
                    print(link)
                    summary = item['summary']
                    summary = re.sub("<.*?>", " ", summary) #καθάρισμα περίληψης από html
                    summary = re.sub(r"\s{4,}", " ", summary) #καθάρισμα απο μεγαλα κενα
                    print(summary)
                    date = item["published_parsed"]
                    date_str="{}-{}-{}".format(date[0],date[1],date[2])
                    print(date_str)
                    print("\n")
                    writer.writerow({'title' : title,'date' :date_str, 'summary' : summary, 'link' : link}) #write entry to .csv file
                    
        print('\n')

except KeyError as k :
    print("KeyError exception:",k)

except AttributeError as a :
    print("AttributeError exception: ",a)



#world rss scraping
try : 
    with open('feeds/rss_feed_english.csv','a',newline='',encoding='utf-8') as f:
        columns =['title','date','summary','link']
        writer = csv.DictWriter(f, fieldnames=columns)
        #writer.writeheader()


        for i in english_rss_feeds :
            feed = feedparser.parse(i)
            print(feed[ "channel" ]["title"])
            #print('\n')
            
            for item in feed['items'] :
                    title = item["title"].strip()
                    print(title)
                    link=item["link"]
                    print(link)
                    summary = item['summary']
                    summary = re.sub("<.*?>", " ", summary) #καθάρισμα περίληψης από html
                    summary = re.sub(r"\s{4,}", " ", summary) #καθάρισμα απο μεγαλα κενα
                    print(summary)
                    date = item["published_parsed"]
                    date_str="{}-{}-{}".format(date[0],date[1],date[2])
                    print(date_str)
                    print("\n")
                    writer.writerow({'title' : title,'date' :date_str, 'summary' : summary, 'link' : link}) #write entry to .csv file
                    
        print('\n')

except KeyError as k :
    print("KeyError exception:",k)
    
except AttributeError as a :
    print("AttributeError exception: ",a)
