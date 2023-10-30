from typing import List
import pandas as pd
from src.scrapper import Scrapper


def collect_data(scrapper: Scrapper) -> List:
    return scrapper.get_data()


def convert_scraped_data_to_df(data: List) -> pd.DataFrame:
    df_columns = [
        "reviewerName",
        "reviewerCountryCode",
        "postDate",
        "postTitle",
        "postContent",
        "rating",
        "likes",
        "reply",
    ]
    return pd.DataFrame(data=data, columns=df_columns)


def execute_pipeline(website_name: str, start_page: int, end_page: int):
    scrapper = Scrapper(
        website_name=website_name, start_page=start_page, end_page=end_page
    )
    data = collect_data(scrapper=scrapper)
    df = convert_scraped_data_to_df(data=data)
    return df.to_json()
