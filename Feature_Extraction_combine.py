import requests
import sys
import pandas as pd
from bs4 import BeautifulSoup
import os
import csv
from AQI_Ploter import avg_data
"""
def avg_data(year):
"""
def meta_data(month, year, city):
    file_html = open('Data/Html_Data/{}/{}/{}.html'.format(city, year,month), 'rb')
    plain_text = file_html.read()  # important: we must read it as soon as possible
    tempD, finalD = [], []

    #intilizing BS
    soup = BeautifulSoup(plain_text, "lxml")
    # findAll( tag, beSpecific)
    for table in soup.findAll('table', {'class': 'medias mensuales numspan'}):
        for tbody in table:
            for tr in tbody:
                a = tr.get_text()
                tempD.append(a)
    rows = len(tempD) / 15

    for times in range(round(rows)):
        newtempData = []
        for i in range(15):
            newtempData.append(tempD[0])
            tempD.pop(0)
        finalD.append(newtempData)

    length = len(finalD)

    finalD.pop(length - 1)
    finalD.pop(0)
    # if month == 1:
    #     print(finalD[0], month, year, city)
    # removing all unnessecary filed in table
    for a in range(len(finalD)):
        for indx in [14,13,12,11,10,6,4,0]:
            finalD[a].pop(indx)
    # print("modidied : ", finalD[0], month, year, city)
    return finalD

def data_combine(year, city, cs):
    for a in pd.read_csv('Data/Final_Data/final_' + city  + str(year) + '.csv', encoding = 'utf-8', chunksize=cs):
        df = pd.DataFrame(data=a)
        mylist = df.values.tolist()
    return mylist


if __name__ == "__main__":
    if not os.path.exists("Data/Final_Data"):
        os.makedirs("Data/Final_Data")
    cities =[ "palam", "safdarjung"]
    for city in cities:
        for year in range(2014, 2023):
            final_data = []
            with open('Data/Final_Data/final_' + city + str(year) + '.csv', 'w') as csvfile:
                wr = csv.writer(csvfile, dialect='excel')
                wr.writerow(['T', 'TM', 'Tm', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
            for month in range(1, 13):
                if year == 2022 and month >= 10:
                    continue
                temp = meta_data(month, year, city)
                final_data = final_data + temp

            print(city, year, len(final_data), final_data[0])

            # i feel so happy to find a way getattr dynamic by passing year
            # 'avg_data')(year) -> avg_data(year) year = 2013,14,15
            pm = getattr(sys.modules[__name__], 'avg_data')(year)

            # if len(pm) == 364:
            #     pm.insert(364, '-')

            for i in range(len(final_data)-1):
                # final[i].insert(0, i + 1)
                final_data[i].insert(8, pm[i])
            # print("inserted pm", city, year, final_data[0], "\n", final_data[1])
            with open('Data/Final_Data/final_' + city  + str(year) + '.csv', 'a') as csvfile:
                wr = csv.writer(csvfile, dialect='excel')
                for row in final_data:
                    flag = 0
                    for elem in row:
                        if elem == "" or elem == "-":
                            flag = 1
                    if flag == 0:
                        wr.writerow(row)

    data_palam2014 = data_combine(2014,"palam", 600)
    data_palam2015 = data_combine(2015,"palam", 600)
    data_palam2016 = data_combine(2016,"palam", 600)
    data_palam2017 = data_combine(2017,"palam", 600)
    data_palam2018 = data_combine(2018,"palam", 600)
    data_palam2019 = data_combine(2019,"palam", 600)
    data_palam2020 = data_combine(2020,"palam", 600)
    data_palam2021 = data_combine(2021,"palam", 600)
    data_palam2022 = data_combine(2022,"palam", 600)
    
    data_safdarjung2014 = data_combine(2014,"safdarjung", 600)
    data_safdarjung2015 = data_combine(2015,"safdarjung", 600)
    data_safdarjung2016 = data_combine(2016,"safdarjung", 600)
    data_safdarjung2017 = data_combine(2017,"safdarjung", 600)
    data_safdarjung2018 = data_combine(2018,"safdarjung", 600)
    data_safdarjung2019 = data_combine(2019,"safdarjung", 600)
    data_safdarjung2020 = data_combine(2020,"safdarjung", 600)
    data_safdarjung2021 = data_combine(2021,"safdarjung", 600)
    data_safdarjung2022 = data_combine(2022,"safdarjung", 600)
    
    total = data_palam2014 + data_palam2015 + data_palam2016 + data_palam2017 + data_palam2018 + data_palam2019 + data_palam2020 + data_palam2021 + data_palam2022
    total = total + data_safdarjung2014 + data_safdarjung2015 + data_safdarjung2016 + data_safdarjung2017 + data_safdarjung2018 + data_safdarjung2019 + data_safdarjung2020 + data_safdarjung2021 + data_safdarjung2022
    

    
    
    with open('Data/Final_Data/final_combine.csv', 'w') as csvfile:
        wr = csv.writer(csvfile, dialect='excel')
        wr.writerow(['T', 'TM', 'Tm', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
        wr.writerows(total)
        
# https://stackoverflow.com/a/55563504/12227386 this didnot work
# https://stackoverflow.com/a/50538501/12227386 worked
# actuall it worked for utf=8 encoding by self.
df=pd.read_csv('Data/Final_Data/final_combine.csv', encoding = 'utf-8')
