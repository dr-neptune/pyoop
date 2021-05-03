# api key: 890603a55bfa47048e4490069ebee18c
import requests

class NewsFeed:
    """
    Represents multiple news titles and links as a string
    """
    base_url = "https://newsapi.org/v2/everything?"
    api_key = "890603a55bfa47048e4490069ebee18c"

    def __init__(self, interest, from_date, to_date, language="en"):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        # construct URL
        url = self.base_url + \
            f"q={self.interest}" + \
            f"&from={self.from_date}" + \
            f"&to={self.to_date}" + \
            f"&language={self.language}" + \
            f"&apiKey={self.api_key}"

        # get pages
        content = requests.get(url).json()

        # get page titles and urls
        articles = [i['title'] + '\n' +
                    i['url'] + '\n\n'
                    for i in content['articles']]

        return articles


# food_feed = NewsFeed("vegan food", "2021-05-02", "2021-05-03", "en")
# print(*food_feed.get())
