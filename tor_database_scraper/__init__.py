import json
import os
from typing import Dict, Any

import psycopg2

from tor_database_scraper.parsers import parse_volunteer
from tor_database_scraper.scrapers import scrape_volunteers


def _dump(obj: Any, name: str):
    if not os.path.exists("output"):
        os.makedirs("output")

    with open(f"output/{name}.json", "w+") as file:
        json.dump(obj, file)


def scrape_db(postgres_cfg: Dict):
    with psycopg2.connect(**postgres_cfg) as connection:
        volunteers = scrape_volunteers(connection)
        _dump(volunteers, "volunteers")
