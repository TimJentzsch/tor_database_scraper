from typing import List

from tor_database_scraper import parse_volunteer
from tor_database_scraper.types import Volunteer


def scrape_users(connection) -> List[Volunteer]:
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT u.id, u.username, g.gamma, u.date_joined, u.is_bot
            FROM authentication_blossomuser AS u LEFT JOIN (
                SELECT completed_by_id, COUNT(*) AS gamma
                FROM api_submission
                WHERE completed_by_id IS NOT NULL
                GROUP BY completed_by_id
            ) as g ON u.id = g.completed_by_id
            ORDER BY u.date_joined;
            """
        )

        return [parse_volunteer(*row) for row in cursor.fetchall()]


def scrape_volunteers(connection) -> List[Volunteer]:
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT u.id, u.username, g.gamma, u.date_joined, u.is_bot
            FROM authentication_blossomuser AS u LEFT JOIN (
                SELECT completed_by_id, COUNT(*) AS gamma
                FROM api_submission
                WHERE completed_by_id IS NOT NULL
                GROUP BY completed_by_id
            ) as g ON u.id = g.completed_by_id
            WHERE u.is_bot = false AND u.accepted_coc = true
                AND u.blacklisted = false AND g.gamma > 0
            ORDER BY u.date_joined;
            """
        )

        return [parse_volunteer(*row) for row in cursor.fetchall()]
