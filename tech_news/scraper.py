import requests
from parsel import Selector
from requests.exceptions import ConnectTimeout, HTTPError, ReadTimeout
import time
import re


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


def scrape_news(html_content):

    select = Selector(html_content)

    string_time = select.css("ul > li.meta-reading-time::text").get()
    number_time = int("".join(re.findall("\d", string_time)))

    summary = select.css(
        "div.entry-content > p:nth-of-type(1) ::text").getall()

    data = {
        "url": select.css("head > link[rel='canonical']::attr(href)").get(),
        "title": select.css("h1.entry-title::text").get().strip(),
        "timestamp": select.css("li.meta-date::text").get(),
        "writer": select.css("span.author > a::text").get(),
        "reading_time": number_time,
        "summary": "".join(summary).strip(),
        "category": select.css("span.label::text").get(),
    }

    return data


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
