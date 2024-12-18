import os
import pandas as pd
import numpy as np
import math
import cmath
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime as dt


##Functions and 
#Datetime Conversion
def table_datetime_conversion(df):
    # Convert 'searchDate' and 'flightDate' to datetime, handling potential errors
    df['searchDate'] = pd.to_datetime(df['searchDate'], format='%Y-%m-%d', errors='coerce')
    df['flightDate'] = pd.to_datetime(df['flightDate'], format='%Y-%m-%d', errors='coerce')

    # Ensure the columns are of datetime type
    df['searchDate'] = df['searchDate'].astype('datetime64[ns]')
    df['flightDate'] = df['flightDate'].astype('datetime64[ns]')

    return df


#For start-end time classification 
def extract_time(time_string):
    segments = time_string.split("||")
    first_segment = segments[0]

    datetime = dt.fromisoformat(first_segment)
    return datetime.time()

#For start-end time classification 
def time_classification(time):
    hour=time.hour #get the hour from the time object
    #ex: 06:30 -> 6
    if hour in range(3,7): #03:00 - 06:00
        return 'Early Morning'
    elif hour in range(7,11):
        return 'Morning'
    elif hour in range(11,15):
        return 'Noon'
    elif hour in range(15,19):
        return 'Afternoon'
    elif hour in range(19,23):
        return 'Evening'
    elif hour in [23,0,1,2]: # 23:00 - 02:00 (covering late night)
        return 'Late night'
    else:
        return 'Unknown'


#For non-KPI feature creation
def feature_creation(df):
    
    #Extracted Time Columns
    df['departureTime']=df['segmentsDepartureTimeRaw'].apply(extract_time)
    df['arrivalTime']=df['segmentsArrivalTimeRaw'].apply(extract_time)

    #Categorizing ordinal times
    df['departureCategory'] = df['departureTime'].apply(time_classification)
    df['arrivalCategory'] = df['arrivalTime'].apply(time_classification)

    #Route
    df['route']=df['startingAirport'] + '|' + df['destinationAirport']
    relocate_route_col = df.pop('route')
    df.insert(1,'route', relocate_route_col)

    #dayOfWeek creation
    df["searchDayOfWeek"] = df["searchDate"].dt.day_name() #day of week for the search date
    df["flightDayOfWeek"] = df["flightDate"].dt.day_name() #day of week for the flight date

    #reorders the columns to have the dayOfWeek features align near the actual search datess
    columns_order = []
    for col in df.columns:
        columns_order.append(col)
        if col == 'searchDate':
            columns_order.append('searchDayOfWeek')
        if col == 'flightDate':
            columns_order.append('flightDayOfWeek')
    
    columns_order = list(dict.fromkeys(columns_order))
    df = df[columns_order]

    #isHoliday creation AND nearHoliday creation
    HOLIDAYS_LIST = [
        "2022-04-15", #Good Friday
        "2022-04-17", #Easter Sunday
        "2022-04-23", #NYC Spring Break
        "2022-04-30", #Solar Eclips
        "2022-05-02", #Eid al-Fitr
        "2022-05-08", #Mother's Day
        "2022-05-30", #Memorial Day
        "2022-06-19", #Juneteenth AND Father's Day
        "2022-06-20", #Observed Juneteenth
        "2022-07-04", #Independence Day
        "2022-06-26", #NYC Pride March
        "2022-07-22", #Comic-Con NYC start
        "2022-09-05", #Labor Day
    ]
    holidays = pd.to_datetime(HOLIDAYS_LIST)

    df["isHolidaySearchDate"] = df["searchDate"].isin(holidays).astype(int)
    df["isHolidayFlightDate"] = df["flightDate"].isin(holidays).astype(int)
    

    def is_near_holiday(date, holidays, window=6): #window default for 6 day windows around holidays should capture a full week given the 7th day is the holiday itself
        return any( (date > holiday - pd.Timedelta(days=window)) & (date < holiday + pd.Timedelta(days=window)) for holiday in holidays )

    df["nearHolidaySearchDate"] = (
        df["searchDate"].apply(lambda searchDate: 1 if is_near_holiday(searchDate, holidays, window=6) else 0)
    )
    df["nearHolidayFlightDate"] = (
        df["flightDate"].apply(lambda flightDate: 1 if is_near_holiday(flightDate, holidays, window=6) else 0)
    )

    df.loc[df["isHolidaySearchDate"] == 1, "nearHolidaySearchDate"] = 0 #override to make sure is and near are separate on specific offending rows
    df.loc[df["isHolidayFlightDate"] == 1, "nearHolidayFlightDate"] = 0 #override to make sure is and near are separate on specific offending rows

    #Squished integer date creation for modeling
    df["searchDateInt"] = df["searchDate"].dt.strftime("%Y%m%d").astype(int)
    df["flightDateInt"] = df["flightDate"].dt.strftime("%Y%m%d").astype(int)
    
    return df



#For KPI feature creation
def kpi_creation(df):

    df["daysLeft"] = (df["flightDate"] - df["searchDate"]).dt.days
    df['numStops']= df['segmentsAirlineName'].apply(lambda x: len(x.split('||'))-1)
    # df["dollarPerMile"]
    # df["milePerDollar"]
    # df["monthlyAverageRoutePrice"]

    return df



### Table Transformation# ###

##Bring in table
relative_path_to_native_data = "../data/jetblue_df.csv"
relative_path_to_new_data_destination = "../data/cleaned_jetblue_df.csv"
# relative_path_to_new_data_destination = "../data/testing_cleaned_jetblue_df.csv"

df = pd.read_csv(relative_path_to_native_data) 

##Drop unused columns
dropped_columns = [
    "Unnamed: 0", #useless
    "segmentsAirlineCode", #redundant
    "segmentsEquipmentDescription", #dirty
    "fareBasisCode", #bloat
    "legId", #bloat
    "segmentsDistance", #bloat
    "travelDuration", #bloat
    "segmentsDepartureTimeEpochSeconds", #wont use
    "segmentsArrivalTimeEpochSeconds", #wont use

]
df.drop(columns=dropped_columns, axis=1, inplace=True)


##Remove Null Values
df.dropna(inplace=True)


##Remove Duplicates
df.drop_duplicates(inplace=True)


##Filtering

# Filtering only "NY" routes..
# EWR (NJ airport) included as it's poopular for New Yorkers to travel to Newark for flights.
ny_filter = ["JFK", "LGA", "EWR"]
df = df[
    (df["startingAirport"].isin(ny_filter)) |         #only starting airport
    (df["destinationAirport"].isin(ny_filter))        #only destination airports
    ]  


# #Filtering out JetBlue partners
# pure_jetblue_filter = ['JetBlue Airways', 'JetBlue Airways||JetBlue Airways','JetBlue Airways||JetBlue Airways||JetBlue Airways'] #here for interpretability
# df = df[ df["segmentsAirlineName"].isin(pure_jetblue_filter) ]


##Price outlier cutting
df = df[
    df["totalFare"] <= 1500 #chosen based on plot of total fare spread 
]

##Label cleaning
#Datetime Conversion
df = table_datetime_conversion(df)


##Feature Engineering
#Feature Creation
df = feature_creation(df)


#KPI Creation
df = kpi_creation(df)


##Remove white space
cols_to_strip_white_space = [
    "route",
    "startingAirport",
    "destinationAirport",
    "segmentsArrivalAirportCode",
    "segmentsDepartureAirportCode",
    "segmentsCabinCode",
    "segmentsAirlineName"
]
for col in cols_to_strip_white_space:
    df[col] = df[col].str.replace(r"\s+", "", regex=True)


##Feature reduction
#drop redundant airline codes and redundant airline names


##Train, Test Split?
##this means we will create two outputs denoted with a train and test
##Have to decide a uniform seed and consider if stratification is necessary

##Save Table into data folder
df.to_csv(relative_path_to_new_data_destination, index=False)