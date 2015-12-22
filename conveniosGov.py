import pprint
import json
import BeautifulSoup
import urllib2
import csv
import requests
import simplejson
import pandas as pd


def dados_generator():
    with open(r'E:\Downloads\remuneracao.csv', "rb") as csv_file:
        reader = pd.read_csv(csv_file)
        dataframe = pd.DataFrame(reader) 
        for row in dataframe:
            yield row

print list(dados_generator())

# for item in a:
#     count = 0
#     print(item.decode('iso-8859-1').encode('utf-8'))


