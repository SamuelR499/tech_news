import requests
from parsel import Selector
from requests.exceptions import ConnectTimeout, HTTPError, ReadTimeout
import time


def fetch(url):

    time.sleep(1)
    try:
        res = requests.get(
            url,
            headers={"user-agent": "Fake user-agent"},
            timeout=3
            )
        res.raise_for_status()
    except (ConnectTimeout, HTTPError, ReadTimeout):
        return None

    return res.text


def scrape_updates(html_content):

    select = Selector(html_content)
    url = select.css("a.cs-overlay-link::attr(href)").getall()

    return url


def scrape_next_page_link(html_content):
    select = Selector(html_content)
    url_next_page = select.css("a.next::attr(href)").get()

    return url_next_page


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
