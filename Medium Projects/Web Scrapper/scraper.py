import requests
from bs4 import BeautifulSoup
import os
import string

pages = int(input())
article_type = input()

cwd = os.getcwd()
for page in range(1, pages + 1):
    os.chdir(cwd)
    os.mkdir(f'Page_{page}')
    os.chdir(f'Page_{page}')
    url = f"https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&page={page}"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    script = soup.find_all('article')
    urls = []
    titles = []
    for scp in script:
        a = scp.find("span", {'data-test': "article.type"})
        if a.text.strip() == article_type:
            b = scp.find('h3').find('a')
            titles.append(b.contents)
            urls.append(b.get('href'))
    article_url = "https://www.nature.com"
    soups = []
    for i in range(len(urls)):
        urls[i] = article_url + urls[i]
        r = requests.get(urls[i])
        soup = BeautifulSoup(r.content, 'html.parser')
        test = soup.find('div', {'class': "c-article-body"})
        if test is None:
            test = soup.find('div', {'class': "article-item__body"})
            if test is None:
                test = soup.find('article')
        soups.append(test)
    body_ = []
    for soup in soups:
        body_.append(soup.text.strip())
    for body, title in zip(body_, titles):
        title = title[0]
        for ele in title:
            if ele in string.punctuation:
                title = title.replace(ele, "")
            title = title.replace(' ', '_')
        with open(f"{title}.txt", 'w', encoding='utf-8') as file:
            print(body, file=file)
print('Saved all articles.')
