```python
import urllib.request
from bs4 import BeautifulSoup
import json
import time

try:
    html = urllib.request.urlopen('https://lednikbar.ru/vino/').read()
    soup = BeautifulSoup(html, 'html.parser')
except urllib.error.HTTPError:
    print('Error 404 Not Found')

def get_menu(title_class, items_name_class, items_price_class):
    common = []
    korob ={}
    title = soup.find(class_=title_class)
    section_header = title.find('h3').get_text()

    for i in title:
        try:
            name = i.find(class_= items_name_class).get_text()
            price = i.find(class_= items_price_class).get_text()
            common.append(name+' - <b>'+price+'</b>')
        except:
            pass
    korob[section_header] = common
    return korob

title_class = 'fdm-item-title'
items_price_class = 'fdm-item-price'
w_white_glass_class = 'fdm-section fdm-sectionid-308 fdm-section-white-wines-glass-cat-ru fdm-section-0'
w_red_glass_class = 'fdm-section fdm-sectionid-316 fdm-section-red-wines-glasses-cat-ru fdm-section-0'
w_strong_glass_class = 'fdm-section fdm-sectionid-30 fdm-section-fortified-wines-glasses-cat-ru fdm-section-0'
w_dessert_glass_class = 'fdm-section fdm-sectionid-637 fdm-section-dessert-wines-glasses-cat-ru fdm-section-0'
w_sparkl_bottles_class = 'fdm-section fdm-sectionid-45 fdm-section-sparkling-wines-bottles-cat-ru fdm-section-0'

wine_white_glass = get_menu(w_white_glass_class, title_class, items_price_class)
wine_red_glass = get_menu(w_red_glass_class, title_class, items_price_class)
wine_strong_glass = get_menu(w_strong_glass_class, title_class, items_price_class)
wine_dessert_glass = get_menu(w_dessert_glass_class, title_class, items_price_class)

wine_sparkl_bottles = get_menu(w_sparkl_bottles_class, title_class, items_price_class)

wine = [wine_white_glass, wine_red_glass, wine_strong_glass, wine_dessert_glass]

with open('alcohol.json', 'w', encoding='utf-8') as file:
    json.dump(wine, file, ensure_ascii=False)
```
