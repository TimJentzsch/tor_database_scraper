import psycopg2
import toml


def tor_database_scraper(config):
    postgres_cfg = config.get("postgres", {})
    conn = psycopg2.connect(**postgres_cfg)

    with conn.cursor() as cur:
        cur.execute("SELECT version()")
        print(cur.fetchone())


def main():
    try:
        config = toml.load("config.toml")
    except FileNotFoundError:
        print(
            "Config file not found!\n"
            "Please create a `config.toml` in the root folder."
        )
        exit(1)
        return

    postgres_cfg = config.get("postgres", {})

    if not postgres_cfg:
        print(
            "Postgres data not configured!\n"
            "Please specify `host`, `database` and `user` under `postgres`."
        )
        exit(1)
        return

    tor_database_scraper(config)


if __name__ == "__main__":
    main()
