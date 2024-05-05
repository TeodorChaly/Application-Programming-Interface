import asyncio

import requests
import requests as req
from bs4 import BeautifulSoup
from fastapi import FastAPI

app = FastAPI()


@app.get("/random/")
async def add_trades():
    price = await asyncio.gather(async_scraping_random())
    return {"price": price}


async def async_scraping_random():
    query = "bitcoin"
    url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "*/*",
    }
    response = requests.get(url, headers=headers)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')
    bitcoin_price = soup.find('div', class_='card-section PZPZlf').find(class_="pclqee").text

    return bitcoin_price
