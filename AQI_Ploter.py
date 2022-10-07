# The data has been made publicly available by the Central Pollution Control Board: 
# https://cpcb.nic.in/ which is the official portal of Government of India.
#  They also have a real-time monitoring app: https://app.cpcbccr.com/AQI_India/
# years was missing and i am low on time so i didnot bother

import pandas as pd
import matplotlib.pyplot as plt

# generic doesnot work
# feture_extraction_combine.pt line 70: getattribuute error
def avg_data(year):
    average=[]
    location = "Data/air_quality_data/air_quality_data" + str(year) + ".csv"
    df = pd.read_csv(location)
    for val in df['pm25']:
        avg=0.0
        if type(val) is float or type(val) is int:
            avg = avg + val
        elif type(val) is str:
            if val!='' and val!='NoData' and val!='PwrFail' and val!='---' and val!='InVld':
                temp=float(val)
                avg = avg + temp
        average.append(avg)
    return average
    

if __name__=="__main__":
    year_days = { 2014 : 365, 2015 : 365, 2016 : 366, 2017 : 365, 2018 : 365, 2019 : 365, 2020 : 366, 2021 : 365, 2022 : 273 }
    for year in range(2014,2017):
        plot_year = avg_data(year)
        lable_data = str(year) + " data"
        plt.plot(range(0,year_days[year]),plot_year,label=lable_data)
        plt.xlabel('Day')
        plt.ylabel('PM 2.5')
        plt.legend(loc='upper right')
    plt.show()