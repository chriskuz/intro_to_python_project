import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv("../data/cleaned_jetblue_df.csv")

niche_encoding_filter = [
    "searchDayOfWeek", 
    "flightDayOfWeek",
    "segmentsAirlineName"
]
general_onehot_encoding_filter = [
    "arrivalCategory", 
    "departureCategory",
    "destinationAirport", 
    "segmentsCabinCode",
    "startingAirport",
] 

nunique_scalers_on_onehot = [lambda x: if ]


## Niche Encoding
# Cyclic weekend encoding
DAY_OF_WEEK_HIERARCHY_DICT = {
    "Sunday":1, 
    "Monday":2,
    "Tuesday":3,
    "Wednesday":4,
    "Thursday":5,
    "Friday":6,
    "Saturday":7
}

niche_df = df.copy()
niche_df = niche_df[niche_encoding_filter]

niche_df["searchDayOfWeekHierarchyEncoded"] = niche_df["searchDayOfWeek"].map(DAY_OF_WEEK_HIERARCHY_DICT)
niche_df["searchDayOfWeekSine"] = np.sin(2 * np.pi * niche_df["searchDayOfWeekHierarchyEncoded"] / 7)
niche_df["searchDayOfWeekCosinee"] = np.cos(2 * np.pi * niche_df["searchDayOfWeekHierarchyEncoded"] / 7)

# Partnership encoding 
non_partnered_airlines = [
    "JetBlueAirways", 
    "JetBlueAirways||JetBlueAirways",
    "JetBlueAirways||JetBlueAirways||JetBlueAirways"
]

niche_df["hasPartnership"] = df["segmentsAirlineName"].apply(lambda names: 1 if names in non_partnered_airlines else 0)

##Drop the encoded columns


niche_df.drop(columns=niche_encoding_filter, axis=1, inplace=True)


##General One Hot
encoder = OneHotEncoder()

encoded = encoder.fit_transform(df[general_onehot_encoding_filter])
encoded_dense = encoded.toarray()

encoded_df = pd.DataFrame(encoded_dense, columns=encoder.get_feature_names_out(general_onehot_encoding_filter))



## General and Niche Concatenatioin
model_encoded_df = pd.concat([encoded_df, niche_df], axis=1)




## Save DF
# relative_path_to_new_data_destination = "../data/model_encoded_jetblue_df.csv"
relative_path_to_new_data_destination = "../data/testing_model_encoded_jetblue_df.csv"

model_encoded_df.to_csv(relative_path_to_new_data_destination, index=False)