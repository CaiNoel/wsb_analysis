# wsb_analysis

## Abstract
This project is meant to be a tool for gauging social media sentiment on specific financial tickers. It will consist of multiple components and stages, which I will update as I make more progress. The main way we will be getting data is from PushShift, which is an external API for accessing Reddit statistics. For this project, we will be primarily accessing the popular subreddit **r/wallstreetbets**.

## Part #1: WSB Scraper
* NASDAQ.txt
* wsb_scraper.py

Right now, these two files allow you to see the most discussed tickers on r/wallstreetbets for the last twenty-four hours. "NASDAQ.txt" is simply a text file containing almost every American stock symbol, and "wsb_scraper.py" is the main logic. Feel free to open it up and look over it if you're interested in how to access the Reddit API.

**You cannot run this code as is! You will need your own Reddit script and API keys! Fortunately, this is very easy for an individual to do. Once you do, replace the fields in the beginning of the script with your username, password, and API keys.**

