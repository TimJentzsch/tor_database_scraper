from typing import Dict

import psycopg2


def scrape_db(postgres_cfg: Dict):
    with psycopg2.connect(**postgres_cfg) as connection:
        scrape_volunteers(connection)


def scrape_volunteers(connection):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM authentication_blossomuser;")

        for row in [cursor.fetchone()]:
            print(row)
