import requests
from bs4 import BeautifulSoup
from newspaper import Article
import heapq

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

# Function to get article text and metadata using newspaper3k
def get_article_details(article_url):
    article = Article(article_url)
    article.download()
    article.parse()
    return {
        'title': article.title,
        'text': article.text,
        'publish_date': article.publish_date,
        'top_image': article.top_image
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
    
    # Get the top N articles by publish date (most recent)
    top_articles = heapq.nlargest(top_n, articles, key=lambda x: x['publish_date'] if x['publish_date'] else "")
    return top_articles

if __name__ == "__main__":
    top_trending_articles = get_top_trending_articles(news_websites, top_n=10)
    for idx, article in enumerate(top_trending_articles):
        print(f"{idx+1}. {article['title']}")
        print(f"Published on: {article['publish_date']}")
        print(f"URL: {article['top_image']}")
        print("="*50)
