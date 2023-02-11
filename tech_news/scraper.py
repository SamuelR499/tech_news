import requests
import time
import re
from parsel import Selector
from tech_news.database import create_news
from requests.exceptions import ConnectTimeout, HTTPError, ReadTimeout


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


def get_tech_news(amount):
    base_url = 'https://blog.betrybe.com/'
    # a cada interação no while, este link troca

    url_news = []  # lista de urls de noticias

    while len(url_news) < amount:
        news_page = fetch(base_url)  # pagina de "noticias"
        url_news += scrape_updates(news_page)
        # url_news recebe uma lista de todas as urls desta pagina atual
        base_url = scrape_next_page_link(news_page)
        # Recebe como parametro a pagina atual, e pega o link da proxima pagina

    news_list = []

    for url in url_news:
        if len(news_list) < amount:
            html_content = fetch(url)
            news_data = scrape_news(html_content)
            news_list.append(news_data)

    create_news(news_list)
    return news_list
