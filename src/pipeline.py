from typing import List
import pandas as pd
from src.scrapper import Scrapper


def collect_data(scrapper: Scrapper) -> List:
    """Collects data from website using Scraper object.

    Args:
        scrapper (Scrapper): This class is a scraper built to
        scrape trust-pilot.

    Returns:
        List: Returns all data scraped as a list
    """
    return scrapper.get_data()


def execute_pipeline(website_name: str, end_page: int, start_page: int = 1) -> List:
    """This function uses the Scrapper to collect data from
    trust-pilot and provide it at an end-point for processing.

    Args:
        website_name (str): The name of the website we need to scrape.
        end_page (int): The page number that you would like to stop scraping.
        start_page (int, optional): The page number to start scraping. Defaults to 1.

    Returns:
        List: Returns a list of dicts in JSON format with all data.
    """
    scrapper = Scrapper(
        website_name=website_name, start_page=start_page, end_page=end_page
    )
    data = collect_data(scrapper=scrapper)
    return data
