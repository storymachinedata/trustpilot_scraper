from typing import List
import json
import time
import requests
import pandas as pd
import datetime as dt
from bs4 import BeautifulSoup


class Scrapper:
    def __init__(self, website_name: str, start_page: int, end_page: int) -> None:
        self.website_name = website_name
        self.start_page = start_page
        self.end_page = end_page
        self.df_data = []

    def get_json_data(self, page: int) -> List:
        """This function collect the props meta data from the provided link.

        Args:
            page (int): Page number to scrape.

        Returns:
            List: Returns a list of dictionaries with raw props scraped from the website.
        """
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

    def get_data(self) -> List:
        """This function fetchs the raw data from the website.
        We extract the necessary data from the props and
        send it to the endpoint.

        Returns:
            List: Retruns the list of dictionaries that contain the necessary
            data to be scraped from trust-pilot.
        """
        for page in range(self.start_page, self.end_page + 1):
            data = self.get_json_data(page=page)
            if data == None:
                print("Rate Limited")
                return self.df_data, page

            for review in data:
                reviews = {
                    "reviewerName": review["consumer"]["displayName"],
                    "reviewerCountryCode": review["consumer"]["countryCode"],
                    "postDate": review["dates"]["publishedDate"],
                    "postTitle": review["title"],
                    "postContent": review["text"],
                    "rating": review["rating"],
                    "likes": review["likes"],
                }

                if review["reply"] != None:
                    reviews["reply"] = review["reply"]["message"]
                else:
                    reviews["reply"] = None

                self.df_data.append(reviews)
            if page % 100 == 0:
                time.sleep(60)
        return self.df_data, page
