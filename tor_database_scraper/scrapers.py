from tor_database_scraper import parse_volunteer


def scrape_volunteers(connection):
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
            WHERE u.id = 4034
            """
        )

        for row in [cursor.fetchone()]:
            volunteer = parse_volunteer(*row)
            print(volunteer)
