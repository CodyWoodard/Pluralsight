import requests
import click
import sqlite3
import datetime



create_table_query = """
    CREATE TABLE investments (
        coin_id TEXT,
        currency TEXT,
        sell INT,
        amount REAL,
        date TIMESTAMP
        );
        """

investment = ("bitcoin", "usd", True, 1.0, datetime.datetime.now())

cursor.execute(
    "INSERT INTO investments VALUES (?, ?, ?, ?, ?);",
    investment)
database.commit()

result = cursor.execute("SELECT * FROM investments;")

all_rows = result.fetchall()

first_or_only_row = result.fetchone()

@click.group()
def cli():
    pass



@click.command()
@click.option("--coin_id", default="bitcoin")
@click.option("--currency", default="usd")
def get_coin_price(coin_id, currency):
    coin_id = "bitcoin"
    currency = "usd"
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies={currency}"
    data = requests.get(url).json()
    coin_price = data[coin_id][currency]
    print(f"the price of {coin_id} is {coin_price:.2f} {currency.upper()}")

if __name__ == "__main__":
    database = sqlite3.connect("portfolio.db")
    cursor = database.cursor()
    cursor.execute()
    cli()