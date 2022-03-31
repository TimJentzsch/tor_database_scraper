import toml

from tor_database_scraper import scrape_db


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

    postgres_cfg = config.get("postgres", {})
    scrape_db(postgres_cfg)


if __name__ == "__main__":
    main()
