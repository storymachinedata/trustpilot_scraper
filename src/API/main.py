from typing import List
from datetime import datetime
from fastapi import FastAPI
from src.scrapper import Scrapper
from src.pipeline import collect_data

app = FastAPI()


@app.get("/")
def home() -> str:
    """Home page for the API

    Returns:
        str: returns the type of API
    """
    return "trust-pilot scrapper API"


@app.get("/trust-pilot-scrapper")
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
    print(f"log({datetime.now()}): starting to scrape: {website_name}")
    data, page = collect_data(scrapper=scrapper)
    print(f"log({datetime.now()}): finished scraping: {page}")

    return data
