import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_category,
    search_by_date
)


def option0():
    quantity = int(input("Digite quantas notícias serão buscadas"))

    news = get_tech_news(quantity)
    print(f"Total de noticias populdas no bnaco: {quantity}")
    print("==-==" * 10)
    print(news)


def option1():
    title = input("Digite o titulo:")
    result = search_by_title(title)
    print(result)


def option2():
    date = input("Digite a data no formato aaaa-mm-dd")
    result = search_by_date(date)
    print(result)


def option3():
    category = input("Digite a categoria:")
    result = search_by_category(category)
    print(result)


def option4():
    result = top_5_categories()
    print(result)


options = {
    "0": option0,
    "1": option1,
    "2": option2,
    "3": option3,
    "4": option4
}


def analyzer_menu():

    print("Selecione uma das opções a seguir:\n"
          " 0 - Popular o banco com notícias;\n"
          " 1 - Buscar notícias por título;\n"
          " 2 - Buscar notícias por data;\n"
          " 3 - Buscar notícias por categoria;\n"
          " 4 - Listar top 5 categorias;\n"
          " 5 - Sair.")
    option = input("Sua opção-> ")
    try:
        if option == "5":
            print("Encerrando script")
        else:
            options[option]()
    except (KeyError, ValueError):
        return print("Opção inválida", file=sys.stderr)
