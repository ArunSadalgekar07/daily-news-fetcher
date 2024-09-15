# Daily News Fetcher

The **Daily News Fetcher** is a Python script that fetches the latest top headlines from various news sources using the [NewsAPI](https://newsapi.org/). The script allows you to specify a country and optionally a category to get relevant news, displaying the top 10 headlines along with the source and a link to the full article.

## How it Works

- **NewsAPI**: The script uses the NewsAPI to fetch top news headlines.
- **API Key**: Replace `'your_newsapi_key_here'` with your own NewsAPI key. You can obtain one by signing up at [NewsAPI](https://newsapi.org/).
- **Country & Category**: You can specify a country (e.g., `us`, `in`, `gb`) and optionally a news category (e.g., business, sports, technology). If no category is specified, it fetches general news.
- **Headlines**: The script fetches and displays the top 10 headlines along with the source and a link to the full article.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ArunSadalgekar07/daily-news-fetcher.git

   ```
   ```bash
   cd daily-news-fetcher
   ```
2. **Install the required dependencies**:
   ```bash
   pip install requests
   ```

3. **Add your API Key**:
   - Open the script and replace `'your_newsapi_key_here'` with your NewsAPI key:
     ```python
     api_key = 'your_newsapi_key_here'
     ```

## Running the Script

Run the script by executing:

```bash
python news_fetcher.py
```

You will be prompted to enter the country code and category:

```bash
Enter the country code (e.g., 'us' for USA, 'in' for India): us
Enter the news category (e.g., 'technology', 'business', 'sports', leave blank for all): technology
```

## Example Output

```
Enter the country code (e.g., 'us' for USA, 'in' for India): us
Enter the news category (e.g., 'technology', 'business', 'sports', leave blank for all): technology

Top News Headlines:
------------------
1. Apple unveils new iPhone with major camera upgrades
   Source: TechCrunch
   Link: https://techcrunch.com/apple-unveils-new-iphone

2. Google's AI model beats human benchmarks in language processing
   Source: The Verge
   Link: https://www.theverge.com/google-ai-model

3. Tesla announces new battery technology that could change EV market
   Source: Bloomberg
   Link: https://bloomberg.com/tesla-battery-tech
...
```

## Customization

- **Country and Category**: You can modify the input country code and category to fetch news from different regions and categories.
- **Limit the number of headlines**: You can change the number of headlines fetched by modifying the code.
