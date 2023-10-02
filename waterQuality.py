import random
import numpy as np
from deap import base, creator, tools, algorithms
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Load the dataset with missing values denoted as 'NA'
data = pd.read_csv('WaterQuality.csv', na_values='NA')

# Split the dataset into two subsets based on the target variable
subset_with_target_1 = data[data['EVENT'] == 1]
subset_with_target_0 = data[data['EVENT'] == 0]

# Calculate the average values for each column in both subsets
subset_with_target_1_means = subset_with_target_1.mean()
subset_with_target_0_means = subset_with_target_0.mean()

# Fill missing values in each subset with the corresponding average values
subset_with_target_1.fillna(subset_with_target_1_means, inplace=True)
subset_with_target_0.fillna(subset_with_target_0_means, inplace=True)

# Merge the two subsets back into one dataset
filled_data = pd.concat([subset_with_target_1, subset_with_target_0])
