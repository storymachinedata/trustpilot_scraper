from fastapi import FastAPI
from src.scrapper import Scrapper
from src.pipeline import collect_data, convert_scraped_data_to_df

app = FastAPI()


@app.get("/")
def home():
    return "trust-pilot scrapper API"


@app.get("/trust-pilot-scrapper")
def execute_pipeline(website_name: str, start_page: int, end_page: int):
    scrapper = Scrapper(
        website_name=website_name, start_page=start_page, end_page=end_page
    )
    data = collect_data(scrapper=scrapper)
    return data
