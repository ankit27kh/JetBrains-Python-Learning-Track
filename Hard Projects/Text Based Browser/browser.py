import os
import argparse
import sys
import requests
from bs4 import BeautifulSoup
from colorama import Fore, init

ArgumentParser = argparse.ArgumentParser()
ArgumentParser.add_argument('dir', help='dir-for-files')
args = ArgumentParser.parse_args()
directory = args.dir
if os.access(directory, os.F_OK):
    pass
else:
    os.mkdir(directory)


class Browser:

    def __init__(self):
        self.input_url()

    def input_url(self):
        url = input()
        if url == 'exit':
            self.exit()
        else:
            if url.count('.') > 0 and url.startswith('https://'):
                r = requests.get(url)
                self.output(r, url)
            elif url.count('.') > 0:
                r = requests.get(f"https://{url}")
                self.output(r, url)
            elif os.access(f"{directory}/{url}", os.R_OK):
                self.output(None, url)
            else:
                print("Error: Incorrect URL")
                self.input_url()

    def output(self, r, url):
        init(autoreset=True)
        if r is not None:
            if r:
                soup = BeautifulSoup(r.content, 'html.parser')
                links = soup.find_all('a')
                for link in links:
                    link.insert(0, f"{Fore.BLUE}")
                    link.append("\033[39m")
                print(soup.text)
                with open(f'{directory}/{url.rstrip(".com").lstrip("https://")}', 'w', encoding='utf-8') as file:
                    print(soup.text, file=file)
            else:
                print("Error: Incorrect URL")
        else:
            with open(f'{directory}/{url}', 'r', encoding='utf-8') as file:
                print(file.readlines())
        self.input_url()

    def exit(self):
        sys.exit()


browser = Browser()
