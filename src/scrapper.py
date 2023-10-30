from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime as dt
import json


class Scrapper:
    def __init__(self, website_name: str, start_page: int, end_page: int) -> None:
        self.website_name = website_name
        self.start_page = start_page
        self.end_page = end_page
        self.df_data = []

    def get_json_data(self, page: int):
        response = requests.get(
            f"https://de.trustpilot.com/review/{self.website_name}?page={page}"
        )
        web_page = response.text
        soup = BeautifulSoup(web_page, "html.parser")
        try:
            data = json.loads(
                soup.find("script", id="__NEXT_DATA__", type="application/json").text
            )
            data = data["props"]["pageProps"]["reviews"]
            return data
        except:
            return None

    def get_data(self):
        for page in range(self.start_page, self.end_page + 1):
            data = self.get_json_data(page=page)
            if data == None:
                print("Rate Limited")
                return self.df_data

            for review in data:
                reviews = []
                reviews.extend(
                    [
                        review["consumer"]["displayName"],
                        review["consumer"]["countryCode"],
                        review["dates"]["publishedDate"],
                        review["title"],
                        review["text"],
                        review["rating"],
                        review["likes"],
                    ]
                )

                if review["reply"] != None:
                    reviews.append(review["reply"]["message"])
                else:
                    reviews.append(None)
                self.df_data.append(reviews)
        return self.df_data
