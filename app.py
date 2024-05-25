import re
from urllib.request import urlopen

def fetch_webpage(url):
    # get the source code
    try:
        with urlopen(url) as response:
            html = response.read().decode('UTF-8')
        return html
    
    except Exception as e:
        return None
html = fetch_webpage("https://www.brisbanetimes.com.au/breaking-news")
# print(html)

def fetch_headline(html):
    headline_match = re.search("<h3 c"