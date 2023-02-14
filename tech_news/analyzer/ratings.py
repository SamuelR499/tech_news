from tech_news.database import find_news
from collections import Counter


def top_5_categories():
    news = find_news()
    categories = []
    ranking = []
    for item in news:
        categories.append(item["category"])

    categories.sort()
    c = Counter(categories).most_common()
    for values in c:
        ranking.append(values[0])

    print(ranking)
    return ranking[:5]
