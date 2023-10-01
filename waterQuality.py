import random
import numpy as np
from deap import base, creator, tools, algorithms
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Load the dataset with missing values denoted as 'NA'
data = pd.read_csv('WaterQuality.csv', na_values='NA')
