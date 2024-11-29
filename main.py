KEYWORDS = ['дизайн', 'фото', 'web', 'python']

import requests
import bs4

response = requests.get('https://habr.com/ru/articles/')
soup = bs4.BeautifulSoup(response.text, features='lxml')
articles = soup.select('article.tm-articles-list__item')
parsed_data = []


def parsing_function():
    for article in articles:
        link = 'https://habr.com' + article.select_one('a.tm-title__link')['href']
        article_response = requests.get(link)
        articles_soup = bs4.BeautifulSoup(article_response.text, features='lxml')
        text = articles_soup.select_one('div.tm-article-body').text.lower()
        for keywords in KEYWORDS:
            if keywords in text:
                header = articles_soup.select_one('h1').text
                time = articles_soup.select_one('time')['datetime']
                if link not in parsed_data:
                    parsed_data.append(link)
                    print(f'Дата: {time}   Заголовок: {header}   Ссылка: {link}')


if __name__ == '__main__':
    parsing_function()