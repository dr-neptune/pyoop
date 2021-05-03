import yagmail
import datetime
import pandas as pd
from newsfeed import NewsFeed

# get today and yesterday
today = datetime.datetime.now().strftime("%Y-%m-%d")
yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")

# instantiate a dataframe
df = pd.read_excel("people.xlsx")

# remove NA columns
df = df[df['name'].notna()]

# instantiate an emailer
email_out = yagmail.SMTP(user="",
                         password="")

# for each person in an xlsx file
# send an email with their personalized newsfeed
for index, row in df.iterrows():
    news_feed = NewsFeed(row['interest'], yesterday, today)

    print(f"Sending email to: {row['email']}\n")

    email_out.send(to=row['email'],
                   subject=f"Your {row['interest']} news for today!",
                   contents=f"Hi {row['name']}\nSee what's going on with {row['interest']} today.\n\n\n {''.join(news_feed.get())}")
