import os
import pandas as pd
import numpy as np
import math
import cmath
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime as dt



##Functions
#Datetime Conversion
def table_datetime_conversion(df):
    # Convert 'searchDate' and 'flightDate' to datetime, handling potential errors
    df['searchDate'] = pd.to_datetime(df['searchDate'], format='%Y-%m-%d', errors='coerce')
    df['flightDate'] = pd.to_datetime(df['flightDate'], format='%Y-%m-%d', errors='coerce')

    # Ensure the columns are of datetime type
    df['searchDate'] = df['searchDate'].astype('datetime64[ns]')
    df['flightDate'] = df['flightDate'].astype('datetime64[ns]')

    return df

#TODO: for days between creation
def extract_time(time_string):
    segments = time_string.split("||")
    first_segment = segments[0]

    datetime = dt.fromisoformat(first_segment)
    return datetime.time()

def kpi_creation(df):
    ## 
    df["daysLeft"] = df["flightDate"] - df["searchDate"].dt.days
    # df["dollarPerMile"]
    # df["milePerDollar"]
    # df["monthlyAverageRoutePrice"]

    return df





##Bring in table
relative_path_to_native_data = "../data/jetblue_df.csv"
relative_path_to_new_data_destination = "../data/cleaned_jetblue_df.csv"

df = pd.read_csv(relative_path_to_native_data) 

##Drop unnamed
df.drop("Unnamed: 0", axis=1, inplace=True)

##Remove Null Values
df.dropna(inplace=True)

#Filtering out JetBlue partners
pure_jetblue_filter = [" 'JetBlue Airways', 'JetBlue Airways||JetBlue Airways','JetBlue Airways||JetBlue Airways||JetBlue Airways' "]
df = df[ df["segmentsAirlineName"].isin(pure_jetblue_filter) ]

##Label cleaning

#Datetime Conversion
df = table_datetime_conversion(df)

##Feature Engineering
df = kpi_creation(df)

##Feature reduction
#drop redundant airline codes and redundant airline names

##Save Table into data folder
df.to_csv(relative_path_to_new_data_destination, index=False)