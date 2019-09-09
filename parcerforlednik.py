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
    output = ''
    items_name = ''
    items_price = ''
    item_names = []
    items_prices = []

    title = soup.find(class_=title_class)
    section_header = title.find('h3').get_text()

    soup_items_name = title.find_all(class_= items_name_class)
    soup_items_price = title.find_all(class_=items_price_class)

    for i in soup_items_name:
        i = i.get_text()
        # items_name += (i + '\n')
        item_names.append(i)

    for j in soup_items_price:
        j = j.get_text()
        # items_price += (j + '\n')
        items_prices.append(j)

    output = section_header, dict(zip(item_names, items_prices))
    return output

fdm_item_title = 'fdm-item-title'
fdm_item_price = 'fdm-item-price'
w_white_glass_class = 'fdm-section fdm-sectionid-308 fdm-section-white-wines-glass-cat-ru fdm-section-0'
w_red_glass_class = 'fdm-section fdm-sectionid-316 fdm-section-red-wines-glasses-cat-ru fdm-section-0'
w_strong_glass_class = 'fdm-section fdm-sectionid-30 fdm-section-fortified-wines-glasses-cat-ru fdm-section-0'
w_dessert_glass_class = 'fdm-section fdm-sectionid-637 fdm-section-dessert-wines-glasses-cat-ru fdm-section-0'
w_sparkl_glass_class = 'fdm-section fdm-sectionid-45 fdm-section-sparkling-wines-bottles-cat-ru fdm-section-0'

k=0
while True:
    time.sleep(21600) # in seconds
    wine_white_glass = get_menu(w_white_glass_class, fdm_item_title, fdm_item_price)
    wine_red_glass = get_menu(w_red_glass_class, fdm_item_title, fdm_item_price)
    wine_strong_glass = get_menu(w_strong_glass_class, fdm_item_title, fdm_item_price)
    wine_dessert_glass = get_menu(w_dessert_glass_class, fdm_item_title, fdm_item_price)
    wine_sparkl_glass = get_menu(w_sparkl_glass_class, fdm_item_title, fdm_item_price)

    wine = [wine_white_glass, wine_red_glass, wine_strong_glass, wine_dessert_glass, wine_sparkl_glass]

    with open('alcohol.json', 'w', encoding='utf-8') as file:
        json.dump(wine, file, ensure_ascii=False)
    k+=1
    print(k)



