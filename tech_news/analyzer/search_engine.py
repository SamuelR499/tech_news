from tech_news.database import db


def search_by_title(title):
    query = {
            "title": {
                "$regex": title,
                "$options": "i"
            }
        }
    projection = {"title": 1, "url": 1, "_id": 0}
    news = db.news.find(query, projection)

    result = []

    for new in news:
        result.append((new["title"], new["url"]))

    return result


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
