import pandas as pd
import seaborn as sns 
import numpy as np 
import matplotlib.pylab as plt
import datetime as dt

def load_and_process1():


      #Loading the dataset.
      df = pd.read_csv("../data/raw/AirQualityUCI.csv", sep=";", decimal=",")

      #Renaming importat columns for increased readability and data entery, followed by deletion of non-utilized columns. Lastly converting object to datetime.
      df = (df.rename(columns={'NOx(GT)':'NOx_GT', 'NO2(GT)':'NO2_GT', 'T':'Temp','CO(GT)':'CO_GT', 'Time':'Hour'})
            .drop(df.columns[[3, 4, 5, 6, 8, 10, 11 ,15, 16,]], axis=1)
            .astype({'Date': 'datetime64[ns]'}))
      #Replacing missing values with NaN.
      df.replace(to_replace=-200, value= np.NaN, inplace=True)

      #Formating hour column.
      df['Hour'] = pd.to_datetime(df['Hour'], format='%H.%M.%S').dt.hour

      #Dropping all NaN values, restting the index for clarity.
      df2= (df.dropna()
            .reset_index(drop=True))
      #Setting the index as Date      
      df2.set_index("Date", inplace= True)


      return df2