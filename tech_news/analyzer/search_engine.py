from tech_news.database import db
from datetime import datetime


def search_by_title(title):
    query = {
            "title": {
                "$regex": title,
                "$options": "i"
            }
        }
    projection = {"title": 1, "url": 1, "_id": 0}
    result = []
    for new in db.news.find(query, projection):
        result.append((new["title"], new["url"]))

    return result


def search_by_date(date):
    result = []
    try:
        br_format_date = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        query = {"timestamp": br_format_date}

        for new in db.news.find(query):
            result.append((new["title"], new["url"]))

    except ValueError:
        raise ValueError("Data inválida")
    return result


# Requisito 9
def search_by_category(category):
    query = {
            "category": {
                "$regex": category,
                "$options": "i"
            }
        }
    projection = {"title": 1, "url": 1, "_id": 0}
    result = []
    for new in db.news.find(query, projection):
        result.append((new["title"], new["url"]))

    return result
