import json
import math
import os
import sys
from datetime import datetime

import django
import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter

path = os.path.abspath(os.path.join(os.path.join(os.path.realpath(__file__), os.pardir), os.pardir))
print(path)
if path not in sys.path:
    sys.path.append(path)
SETTINGS_PATH = 'flats.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', SETTINGS_PATH)
django.setup()

from search.models import Advertisement


def parse_kyiv():
    s = requests.Session()
    s.mount('https', HTTPAdapter(max_retries=5))
    r = s.get('https://dom.ria.com/node/searchEngine/v2/?category=1&realty_type=2&operation_type=3&fullCategoryOperation=1_2_3&page=0&state_id=10&city_id=10&limit=1&from_realty_id=&to_realty_id=&sort=inspected_sort&user_id=&characteristic%5B235%5D%5Bfrom%5D=&characteristic%5B235%5D%5Bto%5D=&characteristic%5B246%5D=244&characteristic%5B1609%5D%5Bfrom%5D=&characteristic%5B1609%5D%5Bto%5D=&characteristic%5B1610%5D%5Bfrom%5D=&characteristic%5B1610%5D%5Bto%5D=&characteristic%5B209%5D%5Bfrom%5D=&characteristic%5B209%5D%5Bto%5D=&characteristic%5B214%5D%5Bfrom%5D=&characteristic%5B214%5D%5Bto%5D=&characteristic%5B216%5D%5Bfrom%5D=&characteristic%5B216%5D%5Bto%5D=&characteristic%5B218%5D%5Bfrom%5D=&characteristic%5B218%5D%5Bto%5D=&characteristic%5B227%5D%5Bfrom%5D=&characteristic%5B227%5D%5Bto%5D=&characteristic%5B228%5D%5Bfrom%5D=&characteristic%5B228%5D%5Bto%5D=&realty_id_only=&date_from=&date_to=&with_phone=&exclude_my=&new_housing_only=&banks_only=&exclude_realty_id=&_csrf=F2jks7kM-TH-R7jYOj1QSNU_TSeejamnFlS0&reviewText=&email=&period=0')
    data = json.loads(r.text)
    print(data['count'])
    i = 0
    for page in range(math.ceil(int(data['count']) / 1000.0)):
        r = s.get('https://dom.ria.com/node/searchEngine/v2/?category=1&realty_type=2&operation_type=3&fullCategoryOperation=1_2_3&page={}&state_id=10&city_id=10&limit=1000&from_realty_id=&to_realty_id=&sort=inspected_sort&user_id=&characteristic%5B235%5D%5Bfrom%5D=&characteristic%5B235%5D%5Bto%5D=&characteristic%5B246%5D=244&characteristic%5B1609%5D%5Bfrom%5D=&characteristic%5B1609%5D%5Bto%5D=&characteristic%5B1610%5D%5Bfrom%5D=&characteristic%5B1610%5D%5Bto%5D=&characteristic%5B209%5D%5Bfrom%5D=&characteristic%5B209%5D%5Bto%5D=&characteristic%5B214%5D%5Bfrom%5D=&characteristic%5B214%5D%5Bto%5D=&characteristic%5B216%5D%5Bfrom%5D=&characteristic%5B216%5D%5Bto%5D=&characteristic%5B218%5D%5Bfrom%5D=&characteristic%5B218%5D%5Bto%5D=&characteristic%5B227%5D%5Bfrom%5D=&characteristic%5B227%5D%5Bto%5D=&characteristic%5B228%5D%5Bfrom%5D=&characteristic%5B228%5D%5Bto%5D=&realty_id_only=&date_from=&date_to=&with_phone=&exclude_my=&new_housing_only=&banks_only=&exclude_realty_id=&_csrf=F2jks7kM-TH-R7jYOj1QSNU_TSeejamnFlS0&reviewText=&email=&period=0'.format(page))
        data = json.loads(r.text)
        for ad_id in data['items']:
            i += 1
            if i >= 2151:
                r = s.get('https://dom.ria.com/ru/realty-dolgosrochnaya-arenda-kvartira-kiev-{}.html'.format(ad_id))
                soup = BeautifulSoup(r.text, 'html.parser')
                title = soup.h1.text
                r = s.get('https://dom.ria.com/node/searchEngine/v2/view/realty/{}?lang_id=2'.format(ad_id))
                data = json.loads(r.text)
                short_name = ''
                if 'district_name' in data:
                    short_name = 'р‑н. {}'.format(data['district_name'])
                if 'street_name' in data:
                    short_name += ' ' + data['street_name']
                short_name += ', {} ком. г. Киев'.format(data['rooms_count'])
                if 'metro_station_name' in data:
                    short_name += ' м. {}'.format(data['metro_station_name'])
                image = None
                if 'main_photo' in data:
                    image = data['main_photo'].replace('.jpg', 'b.jpg')
                print(data['priceArr'])
                if '1' in data['priceArr']:
                    advertisement = Advertisement(
                        code=ad_id,
                        title=title,
                        short_title=short_name,
                        description=data.get('description', None),
                        district=data.get('district_name', None),
                        rooms_count=data['rooms_count'],
                        url=data['beautiful_url'],
                        image=image,
                        price_hr=int(data['priceArr']['3'].replace(' ', '')),
                        price_usd=int(data['priceArr']['1'].replace(' ', '')),
                        created=datetime.strptime(data['publishing_date'], '%Y-%m-%d %H:%M:%S')
                    )
                else:
                    advertisement = Advertisement(
                        code=ad_id,
                        title=title,
                        short_title=short_name,
                        description=data.get('description', None),
                        district=data.get('district_name', None),
                        rooms_count=data['rooms_count'],
                        url=data['beautiful_url'],
                        image=image,
                        price_hr=None,
                        price_usd=None,
                        created=datetime.strptime(data['publishing_date'], '%Y-%m-%d %H:%M:%S')
                    )

                advertisement.save()
                print(advertisement)


if __name__ == '__main__':
    parse_kyiv()
