

import pandas as pd
import seaborn as sns 
import numpy as np 
import matplotlib.pylab as plt
import datetime as dt

def load_and_process(path= "/data/raw/AirQualityUCI.csv"):
    
      df = ( pd.read_csv("../data/raw/AirQualityUCI.csv", sep=";", decimal=",")
            .rename(columns={'NOx(GT)':'NOx_GT','CO(GT)':'CO_GT', 'Time':'Hour'})
            .drop(columns= ['Unnamed: 15','Unnamed: 16','T','PT08.S1(CO)','NMHC(GT)','C6H6(GT)', 'PT08.S2(NMHC)','PT08.S5(O3)','PT08.S4(NO2)','PT08.S3(NOx)','NO2(GT)','RH','AH'])
            .replace(to_replace=-200, value= np.NaN, inplace=False)
       )

      df["Date"] = pd.to_datetime(df["Date"], format='%d/%m/%Y')
      df['Day'] = df['Date'].dt.day_name() 
      df['Month'] = df['Date'].dt.month_name()
      df['Hour'] = pd.to_datetime(df['Hour'], format='%H.%M.%S').dt.hour

      

      AM_Clean= (df.dropna()
            .reset_index(drop=True)
            .set_index("Date", inplace= False)
       )
     
      
      return AM_Clean

 