import sys
import requests
from bs4 import BeautifulSoup
import argparse
import lxml


arguments = argparse.ArgumentParser(description='provide from_lang to_lang word --limit')
arguments.add_argument('from_lang', type=str, help='from language')
arguments.add_argument('to_lang', type=str, help='to language type "all" for all')
arguments.add_argument('translate_word', type=str, help='word to be translated')
arguments.add_argument('--limit', type=int, help='number of examples')

args = arguments.parse_args()
from_lang = args.from_lang
to_lang = args.to_lang
translate_word = args.translate_word
if args.limit:
    example_limit = args.limit
else:
    example_limit = 2

language_dictionary = {1: "arabic",
                       2: "german",
                       3: "english",
                       4: "spanish",
                       5: "french",
                       6: "hebrew",
                       7: "japanese",
                       8: "dutch",
                       9: "polish",
                       10: "portuguese",
                       11: "romanian",
                       12: "russian",
                       13: "turkish"}

if from_lang not in list(language_dictionary.values()):
    print(f"Sorry, the program doesn't support {from_lang}")
    sys.exit()
if to_lang not in list(language_dictionary.values()) and to_lang != 'all':
    print(f"Sorry, the program doesn't support {to_lang}")
    sys.exit()


if to_lang == 'all':
    to_langs = [language_dictionary[i] for i in range(1, 14)]
    to_langs.remove(from_lang)
else:
    to_langs = [to_lang]

session = requests.session()
with open(f'{translate_word}.txt', 'w', encoding='utf-8') as f:
    for to_lang in to_langs:
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = f"https://context.reverso.net/translation/{from_lang}-{to_lang}/{translate_word}"
        try:
            r = session.get(url, headers=headers)
            if r:
                soup = BeautifulSoup(r.content, 'lxml')
                words = soup.find_all(class_='translation')
                translations = soup.find_all(class_='example')
                words = [word.text.strip() for word in words]
                translations = [translation.text for translation in translations]
                translations = [translation.rstrip().lstrip().split('\n') for translation in translations]
                translations = [[translation[0], translation[-1].lstrip()] for translation in translations]
                translations_list = []
                for translation in translations:
                    translations_list.extend(translation)

                print()
                f.write('\n')
                print(f"{to_lang.capitalize()} Translations:")
                print(f"{to_lang.capitalize()} Translations:", file=f)
                count = 0
                for word in words[1:]:
                    print(word)
                    print(word, file=f)
                    count = count + 1
                    if count == example_limit:
                        break

                count = 0
                print()
                f.write('\n')
                print(f"{to_lang.capitalize()} Examples:")
                print(f"{to_lang.capitalize()} Examples:", file=f)
                for translation in translations:
                    print(translation[0])
                    print(translation[1])
                    print(translation[0], file=f)
                    print(translation[1], file=f)
                    count = count + 1
                    print()
                    f.write('\n')
                    if count == example_limit:
                        break
            else:
                if r.status_code == 404:
                    print(f'Sorry, unable to find {translate_word}')
        except ConnectionError:
            print("Something wrong with your internet connection")
