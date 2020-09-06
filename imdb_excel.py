# selector for the title: just change the number
# #main > div > span > div > div > div.lister > table > tbody > tr:nth-child(1) > td.titleColumn > a
# #main > div > span > div > div > div.lister > table > tbody > tr:nth-child(250) > td.titleColumn > a
# selector for the year: change the number as well
# #main > div > span > div > div > div.lister > table > tbody > tr:nth-child(1) > td.titleColumn > span
# #main > div > span > div > div > div.lister > table > tbody > tr:nth-child(250) > td.titleColumn > span
'''year = '(1991)'
year = year[1:-1]
print(year)'''
# The python code I made to scrape the IMdB website:
import requests, bs4
from openpyxl import Workbook
workbook = Workbook()
sheet = workbook.active
res = requests.get('https://www.imdb.com/chart/top?ref_=tt_awd')
res.raise_for_status()
n = 1
y = 1
names = []
years = []
soup = bs4.BeautifulSoup(res.text, 'html.parser')
for i in range(250):
    soupy = soup.select(f'#main > div > span > div > div > div.lister > table > tbody > tr:nth-child({n}) > td.titleColumn > a')  # selecting element lists
    titles = soupy[0].getText()
    names.append((soupy[0].getText()))
    sheet[f'A{n}']= titles
    n += 1
print(names)
for i in range(250):
    soupy = soup.select(f'#main > div > span > div > div > div.lister > table > tbody > tr:nth-child({y}) > td.titleColumn > span')  # selecting element lists
    year = (soupy[0].getText())
    year = year[1:-1]
    years.append(year)
    sheet[f'B{y}'] = year
    y += 1
print(years)
workbook.save(filename="imdb.xlsx")

