# Import
import praw
import re
import pandas as pd
import pprint

# Setup Reddit App
reddit = praw.Reddit(client_id='yourClientID',
                    client_secret='yourSecretKey',
                    user_agent='yourUsername',
                    username='yourUsername',
                    password='yourPassword')

subreddit = reddit.subreddit('wallstreetbets')

# Get a dictionary of tickers
with open('NASDAQ.txt') as f:
    lines = f.readlines()
companies = lines[1:]
companies[1][2:companies[1].find('|',2)]

# Setup dictionaries
all_tickers = {}
hot_tickers = {}

for line in companies:
    ticker = line[2:line.find('|',2)]
    all_tickers[ticker] = 1

regexPattern = r'\b([A-Z]+)\b'

# Find most discussed tickers
for submission in subreddit.hot():
    strings = [submission.title]
    submission.comments.replace_more(limit=0)
    for comment in submission.comments.list():
        strings.append(comment.body)
    for s in strings:
        for phrase in re.findall(regexPattern,s):
            if phrase in all_tickers:
                if phrase not in hot_tickers:
                    hot_tickers[phrase] = 1
                else:
                    hot_tickers[phrase] += 1

series = pd.Series(hot_tickers).sort_values(ascending = False)
print(series[:10])
