from typing import Dict

import psycopg2

from tor_database_scraper.parsers import parse_volunteer
from tor_database_scraper.scrapers import scrape_volunteers


def scrape_db(postgres_cfg: Dict):
    with psycopg2.connect(**postgres_cfg) as connection:
        scrape_volunteers(connection)
