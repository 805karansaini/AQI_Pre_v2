# The data has been made publicly available by the Central Pollution Control Board: 
# https://cpcb.nic.in/ which is the official portal of Government of India.
#  They also have a real-time monitoring app: https://app.cpcbccr.com/AQI_India/
# years was missing and i am low on time so i didnot bother

import pandas as pd
import matplotlib.pyplot as plt


def avg_data(year):
    temp_i=0
    average=[]

    location = "Data/air_quality_data/air_quality_data" + str(year) + ".csv"
    for rows in pd.read_csv(location,chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/24
        temp_i=temp_i+1
        
        average.append(avg)
    return average
    



if __name__=="__main__":
    year_days = {2013:365, 2014:364, 2015:365}
    for year in range(2013,2019):
        plot_year = avg_data(year)
        if year < 2016:
            lable_data = str(year) + " data"
            plt.plot(range(0,year_days[year]),plot_year,label=lable_data)
    plt.xlabel('Day')
    plt.ylabel('PM 2.5')
    plt.legend(loc='upper right')
    plt.show()
