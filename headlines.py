# Intentionally using vulnerable versions of libraries
import requests  # requests==2.18.4
import urllib3  # urllib3==1.22
from flask import Flask, jsonify  # Flask==0.12.2
from bs4 import BeautifulSoup
import heapq

# Create Flask app
app = Flask(__name__)

# List of news websites to scan
news_websites = [
    "https://www.cnn.com",
    "https://www.bbc.com",
    "https://www.nytimes.com",
    "https://www.reuters.com",
    "https://www.aljazeera.com"
]

# Function to extract article URLs from a website
def get_article_urls(website_url):
    response = requests.get(website_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    urls = []
    for a in soup.find_all('a', href=True):
        url = a['href']
        if url.startswith('/'):
            url = website_url + url
        if website_url in url:
            urls.append(url)
    return urls

# Function to get article text and metadata
def get_article_details(article_url):
    response = requests.get(article_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find('title').get_text()
    return {
        'title': title,
        'url': article_url
    }

# Function to get top trending articles
def get_top_trending_articles(websites, top_n=10):
    articles = []
    for website in websites:
        try:
            article_urls = get_article_urls(website)
            for url in article_urls:
                try:
                    article_details = get_article_details(url)
                    articles.append(article_details)
                except Exception as e:
                    print(f"Error processing article {url}: {e}")
        except Exception as e:
            print(f"Error processing website {website}: {e}")
    
    # Get the top N articles
    top_articles = heapq.nlargest(top_n, articles, key=lambda x: x['title'])
    return top_articles

@app.route('/trending')
def trending():
    top_trending_articles = get_top_trending_articles(news_websites, top_n=10)
    return jsonify(top_trending_articles)

if __name__ == "__main__":
    app.run(debug=True)
