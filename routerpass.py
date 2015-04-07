import requests
from bs4 import BeautifulSoup as bs
import csv
import collections
import re
import argparse

class routerpass:
    def scraper(self):
        routers=[]
        response=requests.get('http://www.phenoelit.org/dpl/dpl.html').text
        soup=bs(response)
        table=soup.find('table')
        for tr in table.find_all('tr')[1:]:
            tds=tr.find_all('td')
            d=collections.OrderedDict()
            d['name']=tds[0].text
            d['mark']=tds[1].text
            d['username']=tds[4].text
            d['password']=tds[5].text
            routers.append(d)
        keys = routers[0].keys()
        with open('routers.csv','w') as f:
            dict_writer = csv.DictWriter(f, keys)
            dict_writer.writeheader()
            dict_writer.writerows(toCSV)
    def search(self,query):
        input_file = csv.DictReader(open("routers.csv"))
        for row in input_file:
            match=re.search(query,row['name'].lower())
            if  match :
                print row['name'],row['mark'],row['username'],row['password']

    def main(self):
        parser = argparse.ArgumentParser(usage="-h for full usage")
        parser.add_argument('query', help='letters')
        args = parser.parse_args()
        self.search(args.query)
if __name__ == '__main__':
    routerpass().main()
