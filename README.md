# tor_database_scraper

A python script to scrape Blossom database dumps and turn them into JSON files.

Done in a hurry, don't expect quality code here.

## Prerequisites

- Poetry for dependency management.
- On Linux you might need to install `libpq-dev` or other dependencies.

## Usage

- First run `poetry install` to install the dependencies.
- Then create a `config.toml` file in the project root with your Postgres details:

    ```toml
    [postgres]
    host="localhost"
    database="..."
    user="..."
    password="..."
    ```
- Then run `python main.py` to generate the JSON files. This might take a while.
The output will be written to the `./output/` folder. 
