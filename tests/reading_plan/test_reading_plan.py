from tech_news.analyzer.reading_plan import ReadingPlanService
import pytest
from unittest.mock import patch


@pytest.fixture
def all_mocked_fixture():
    return {
        'readable': [
            {
                'chosen_news': [
                    ('5 exemplos de algoritmos na vida real e na computação',
                        5)
                                ],
                'unfilled_time': 5
            },
            {
                'chosen_news': [
                    ('TrybeTalks — Gaules: os ensinamentos de um '
                        'dos maiores streamers do Brasil', 9)
                    ],
                'unfilled_time': 1
            },
            {
                'chosen_news': [
                    ('Hardware e software: o que são e quais as '
                        'diferenças?', 8)
                                ],
                'unfilled_time': 2
            }
        ],
        'unreadable': [
            ('Sistema Operacional Windows: versões,'
                ' dicas e como instalar?', 18),
            ('Next JS: o que é, para que serve e por que usar?', 13)
                    ],
        }


def my_mock():
    return [
        {
            'url': 'https://blog.betrybe.com/' +
            'tecnologia/sistema-operacional-windows/',
            'title': 'Sistema Operacional Windows:' +
            ' versões, dicas e como instalar?',
            'timestamp': '06/02/2023',
            'writer': 'Cairo Noleto',
            'reading_time': 18,
            'summary': '''É fato que todo computador
             necessita de um sistema operacional para
             funcionar. Entretanto, diversas opções
             estão disponíveis no mercado, como o Windows,
             o Mac OS, o Linux e suas variações.''',
            'category': 'Tecnologia'
        },
        {
            'url': 'https://blog.betrybe.com/' +
            'tecnologia/exemplos-de-algoritmos/',
            'title': '5 exemplos de algoritmos na vida real e na computação',
            'timestamp': '03/02/2023',
            'writer': 'Lucas Custódio',
            'reading_time': 5,
            'summary': '''Quando falamos de algoritmos, pensamos em matemática
            e programação. Porém, temos exemplos de algoritmos que estão muito
             presentes nas nossas atividades cotidianas.''',
            'category': 'Tecnologia'
        },
        {
            'url': 'https://blog.betrybe.com/carreira/trybetalks-gaules/',
            'title': 'TrybeTalks — Gaules: os ensinamentos de um dos maiores'
            + ' streamers do Brasil',
            'timestamp': '30/01/2023',
            'writer': 'Lucas Custódio',
            'reading_time': 9,
            'summary': '''Gaules, uma das maiores personalidades do mundo de
            esports brasileiro, divide um pouco de sua experiência de vida e
            carreira em um webinar com estudantes e ex-estudantes da Escola de
            Programação Trybe.''',
            'category': 'Carreira'
        },
        {
            'url': 'https://blog.betrybe.com/tecnologia/next-js/',
            'title': 'Next JS: o que é, para que serve e por que usar?',
            'timestamp': '27/01/2023',
            'writer': 'Lucas Marchiori',
            'reading_time': 13,
            'summary': '''Conhecer as principais tecnologias do mercado,
            bibliotecas ou frameworks, sejam elas Angular, React ou Vue é
            essencial. Dentro deles, há mais possibilidades que podemos
            utilizar em nossos projetos, tais como o Next JS, presente no
            ecossistema do React.js.''',
            'category': 'Tecnologia'
        },
        {
            'url': 'https://blog.betrybe.com/tecnologia/hardware-software' +
            '-diferencas/',
            'title': 'Hardware e software: o que são e quais as diferenças?',
            'timestamp': '26/01/2023',
            'writer': 'Lucas Marchiori',
            'reading_time': 8,
            'summary': '''Hardware e software são conceitos muito valiosos para
            pessoas da tecnologia da informação e saber a diferença entre esses
            dois termos é essencial para engrenar na carreira.''',
            'category': 'Tecnologia'
        }
    ]


def test_reading_plan_group_news(all_mocked_fixture):

    with patch("tech_news.analyzer.reading_plan.find_news", my_mock):
        result = ReadingPlanService.group_news_for_available_time(10)
        assert result == all_mocked_fixture

    with pytest.raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        ReadingPlanService.group_news_for_available_time(0)
