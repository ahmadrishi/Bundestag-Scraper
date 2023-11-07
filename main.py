from bs4 import BeautifulSoup
import requests
from lxml import etree
import csv
from time import sleep
from urllib.parse import urlencode
import concurrent.futures
from config import SCRAPER_API_KEY
links = open('data.csv', 'r+')
errors = open('fail.txt', 'w+')
writer = csv.writer(links)

def get_links():
    links = []
    url = 'https://www.bundestag.de/ajax/filterlist/en/members/863330-863330?limit=9999&view=BTBiographyList'
    q = requests.get(url)
    result = q.content
    soup = BeautifulSoup(result, 'html.parser')
    dom = etree.HTML(str(soup))
    persons = dom.xpath("//li/a/@href")
    return persons

def get_info(link):
    try:
        params = {'api_key': SCRAPER_API_KEY, 'url': link}
        q = requests.get('http://api.scraperapi.com/', params=urlencode(params))
        result = q.content
        soup = BeautifulSoup(result, 'html.parser')
        dom = etree.HTML(str(soup))
        name = dom.xpath("//div[@class='col-xs-8 col-md-9 bt-biografie-name']/h3")[0].text.strip()
        bio = dom.xpath("//div[@class='bt-collapse-padding-bottom'][1]//text()")
        bio = "".join(bio).strip()
        if bio == '':
            raise 'Error'
        data = {"Name": name, "Bio": bio}
        writer.writerow(data.values())
    except:
        # Write Failed Links into a text file
        errors.write(link)


urls = open('links.txt', 'r').readlines()

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(get_info, urls)