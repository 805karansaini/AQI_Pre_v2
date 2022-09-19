import requests
import sys
import pandas as pd
from bs4 import BeautifulSoup
import os
import csv
from AQI import avg_data
"""
def avg_data(year):
"""

def met_data(city, month, year):
    file_html = open('Data/Html_Data/{}/{}/{}.html'.format(city, year,month), 'rb')
    plain_text = file_html.read()  # important: we must read it as soon as possible
    tempData, finalData = [], []

    #intilizing BS
    soup = BeautifulSoup(plain_text, "lxml")
    # findAll( tag, beSpecific)
    for table in soup.findAll('table', {'class': 'medias mensuales numspan'}):
        for tbody in table:
            for tr in tbody:
                a = tr.get_text()
                tempData.append(a)
    rows = len(tempData) / 15

    for times in range(round(rows)):
        newtempData = []
        for i in range(15):
            newtempData.append(tempData[0])
            tempData.pop(0)
        finalData.append(newtempData)

    length = len(finalData)

    finalData.pop(length - 1)
    finalData.pop(0)

    # removing all unnessecary filed in table
    for a in range(len(finalData)):
        finalData[a].pop(13)
        finalData[a].pop(12)
        finalData[a].pop(11)
        finalData[a].pop(10)
        finalData[a].pop(9)
        finalData[a].pop(6)
        finalData[a].pop(0)
    return finalData

def data_combine(year, cs):
    for a in pd.read_csv('Data/Final_Data/final_' + str(year) + '.csv', encoding = 'unicode_escape', chunksize=cs):
        df = pd.DataFrame(data=a)
        mylist = df.values.tolist()
    return mylist


if __name__ == "__main__":
    if not os.path.exists("Data/Final_Data"):
        os.makedirs("Data/Final_Data")
    for city in ["palam","safdarjung"]:
        for year in range(2013, 2016):
            final_data = []
            with open('Data/Final_Data/final_' + str(year) + '.csv', 'w') as csvfile:
                wr = csv.writer(csvfile, dialect='excel')
                wr.writerow(['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
            for month in range(1, 13):
                temp = met_data(city, month, year)
                final_data = final_data + temp
            # i feel so happy to find a way getattr dynamic by passing year
            # 'avg_data')(year) -> avg_data(year) year = 2013,14,15
            pm = getattr(sys.modules[__name__], 'avg_data')(year)

            if len(pm) == 364:
                pm.insert(364, '-')

            for i in range(len(final_data)-1):
                # final[i].insert(0, i + 1)
                final_data[i].insert(8, pm[i])

            with open('Data/Final_Data/final_' + str(year) + '.csv', 'a') as csvfile:
                wr = csv.writer(csvfile, dialect='excel')
                for row in final_data:
                    flag = 0
                    for elem in row:
                        if elem == "" or elem == "-":
                            flag = 1
                    if flag != 1:
                        wr.writerow(row)
                        
    data_2013 = data_combine(2013, 600)
    data_2014 = data_combine(2014, 600)
    data_2015 = data_combine(2015, 600)
     
    total=data_2013+data_2014+data_2015
    
    with open('Data/Final_Data/final_combine.csv', 'w') as csvfile:
        wr = csv.writer(csvfile, dialect='excel')
        wr.writerow(['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
        wr.writerows(total)
        
# https://stackoverflow.com/a/55563504/12227386 this didnot work
# https://stackoverflow.com/a/50538501/12227386 worked
df=pd.read_csv('Data/Final_Data/final_combine.csv', encoding = 'unicode_escape')