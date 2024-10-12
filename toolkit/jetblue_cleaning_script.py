import os
import pandas as pd
import numpy as np
import math
import cmath
import matplotlib.pyplot as plt
import seaborn as sns


##Bring in table
relative_path_to_native_data = "../data/jetblue_df.csv"
relative_path_to_new_data_destination = "../data/cleaned_jetblue_df.csv"

df = pd.read_csv(relative_path_to_native_data) 

##Drop unnamed
df.drop("Unnamed: 0", axis=1, inplace=True)

##Remove Null Values
df.dropna(inplace=True)

#Label cleaning




##Feature reduction



#drop redundant airline codes and redundant 

##Save Table into data folder
df.to_csv(relative_path_to_new_data_destination, index=False)