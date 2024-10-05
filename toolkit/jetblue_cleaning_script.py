import os
import pandas as pd
import numpy as np
import math
import cmath
import matplotlib.pyplot as plt
import seaborn as sns

##Bring in table
df = pd.read_csv("../data/jetblue_df.csv")

##Drop unnamed
df.drop("Unnamed: 0", axis=1, inplace=True)

##Remove Null Values
df.dropna(inplace=True)

##Drop non JetBlue flights

##Save Table into 