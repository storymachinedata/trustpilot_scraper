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


def execute_pipeline(website_name: str, start_page: int, end_page: int):
    scrapper = Scrapper(
        website_name=website_name, start_page=start_page, end_page=end_page
    )
    data = collect_data(scrapper=scrapper)
    return data
