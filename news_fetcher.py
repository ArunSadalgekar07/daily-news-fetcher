import requests
import json

# Set up the NewsAPI key (Get one from https://newsapi.org/)
API_KEY = 'e1509cf861044d0bbfad3808ea686b16'
NEWS_API_URL = 'https://newsapi.org/v2/top-headlines'

# Function to fetch top news headlines
def fetch_top_headlines(country='us', category=None):
    params = {
        'apiKey': API_KEY,
        'country': country,
        'category': category,
        'pageSize': 10  # Number of top news articles to fetch
    }
    
    try:
        response = requests.get(NEWS_API_URL, params=params)
        data = response.json()

        # Check if the request was successful
        if response.status_code == 200 and data['status'] == 'ok':
            articles = data['articles']
            return articles
        else:
            print(f"Error fetching news: {data['message']}")
            return []
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Function to display news headlines
def display_headlines(articles):
    if not articles:
        print("No articles found.")
        return

    print("\nTop News Headlines:")
    print("------------------")
    for i, article in enumerate(articles, 1):
        print(f"{i}. {article['title']}")
        print(f"   Source: {article['source']['name']}")
        print(f"   Link: {article['url']}\n")

# Main function
if __name__ == '__main__':
    # Set country and category (optional) as per user choice
    country = input("Enter the country code (e.g., 'us' for USA, 'in' for India): ").lower() or 'us'
    category = input("Enter the news category (e.g., 'technology', 'business', 'sports', leave blank for all): ").lower() or None

    # Fetch and display the top news headlines
    news_articles = fetch_top_headlines(country, category)
    display_headlines(news_articles)
