import pandas as pd 
import numpy as np 
import datetime

def load_and_process(path= "/data/raw/AirQualityUCI.csv"):
    df_bri1 = (
        pd.read_csv("../data/raw/AirQualityUCI.csv")
        .drop(columns= ['Unnamed: 15','Unnamed: 16','CO(GT)','PT08.S1(CO)','NMHC(GT)','C6H6(GT)', 'PT08.S2(NMHC)','PT08.S5(O3)'])
        .dropna()
        .drop_duplicates()
        .rename(columns={'NOx(GT)':'NOx.GT', 'PT08.S3(NOx)': 'PT08.S3.NOx', 'PT08.S4(NO2)':'PT08.S4.NO2', 'NO2(GT)':'NO2.GT'})
        
    )
    df_bri2= (
        df_bri1
        .df_bri2.assign(Date=lambda x: pd.to_datetime(x.Date, format='%d/%m/%Y'), Time=lambda x: pd.to_datetime(x.Time, format='%H.%M.%S'))
        .replace(to_replace=",", value=".",regex=True, inplace=False)
        .astype({'T': 'float', 'AH':'float','RH':'float'})
        )
    return df_bri2 

