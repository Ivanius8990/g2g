import time
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import pandas as pd
from proxy import proxy




proxy = proxy()
proxy = {"http": f'{proxy}',
         "https": f'{proxy}'}
headers = {
    'authority': 'funpay.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '"Chromium";v="90", "Opera";v="76", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 OPR/76.0.4017.94',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://funpay.com/chips/26/',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
}
i=0
session=requests.Session()
while True:
    i += 1
    url_list=[17,26,6]
    for url in url_list:
        try:

            response = session.get(f'https://funpay.com/chips/{url}/', headers=headers,proxies=proxy).text
            soup = BeautifulSoup(response, 'lxml')
            sellers = soup.find_all('a', class_='tc-item')
            table = []
            now = datetime.now()
            for seller in sellers:
                string = []
                server_name = seller.find('div', class_='tc-server').text.strip()
                side = seller.find('div', class_='tc-side').text.strip()
                seller_name = seller.find('div', class_='media-user-name').text.strip()
                amount = seller.find('div', class_='tc-amount').text.strip(' кк')
                price = seller.find('div', class_='tc-price').text.strip(' ₽\n')
                string.append(server_name)
                string.append(side)
                string.append(seller_name)
                string.append(int(amount.replace(' ', '')))
                string.append(float(price))
                # print(string)
                table.append(string)

            df = pd.DataFrame(table)
            df.columns = ['server', 'side', 'seller', 'amount', 'price']
            df['time'] = now

            # print(df)

            # result = df.groupby(['server', 'side'])[['amount', 'price']].agg({'amount': ['mean', 'min', 'sum'], 'price': ['mean', 'min']})

            # print(result)

            reads_df = pd.read_excel(f'example_{url}.xlsx')
            new_df = pd.concat([reads_df, df])
            new_df.to_excel(f'example_{url}.xlsx', index=False)
        except:
            continue
    print(f'сканирование №{i} завершено')
    time.sleep(5*60)


