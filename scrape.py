from bs4 import BeautifulSoup
import requests
import csv

url = "https://www.bbc.com/news"
page = requests.get(url)

print(page)

soup = BeautifulSoup(page.content, 'html.parser')


results = soup.find_all('div', class_='sc-b8778340-3 gxEarx')

with open('headlines.csv', 'w', newline='', encoding='utf-8') as file:
       writer = csv.writer(file)
       writer.writerow(['Headline', 'URL', 'Summary'])

       for result in results:
            
            link_tag = result.find_parent('a', class_='sc-2e6baa30-0 gILusN') 
            if link_tag:
                link = link_tag['href']
                if not link.startswith('https://www.bbc.com'):
                    link = "https://www.bbc.com" + link
            else:
                 link=None

            title = result.find('h2', class_='sc-4fedabc7-3 zTZri') 
            summary = result.find('p', class_='sc-b8778340-4 kYtujW')

            if title:
                title = title.get_text()
            if summary:
                summary = summary.get_text()
                
            writer.writerow([title , link , summary])
