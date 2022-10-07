# https://en.tutiempo.net/ main website.

# Climate New Delhi / Safdarjung January - 2013
#  https://en.tutiempo.net/climate/01-2013/ws-421820.html  
#Climate New Delhi / Palam January - 2013
# https://en.tutiempo.net/climate/01-2013/ws-421810.html

# importing Libraries
# -*- coding: utf-8 -*-
import os
import time
import requests
import sys


def retrieve_html(city, city_url):
    # https://en.tutiempo.net/climate/01-2013/ws-421810.html
    city_code = city_url[-15:]
    for year in range(2014,2023):
        for month in range(1,13):
            if year == 2022 and month == 10:
                return 
            if(month<10):
                url='http://en.tutiempo.net/climate/0{}-{}{}'.format(month,year,city_code)
            else:
                url='http://en.tutiempo.net/climate/{}-{}{}'.format(month,year,city_code)

            texts=requests.get(url)
            text_utf=texts.text.encode('utf-8')
            
            if not os.path.exists("Data/Html_Data/{}/{}".format(city, year)):
                os.makedirs("Data/Html_Data/{}/{}".format(city, year))
            with open("Data/Html_Data/{}/{}/{}.html".format(city,year,month),"wb") as output:
                output.write(text_utf)
        sys.stdout.flush()

def scrap_html():
    retrieve_html("safdarjung", "https://en.tutiempo.net/climate/01-2014/ws-421820.html")
    retrieve_html("palam", "https://en.tutiempo.net/climate/01-2014/ws-421810.html")

if __name__=="__main__":
    start_time=time.time()
    scrap_html()
    stop_time=time.time()
    print("Time taken {}".format(stop_time-start_time))
        