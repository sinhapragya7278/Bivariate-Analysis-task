# Bivariate Analysis with Supply Chain Data

This repository contains a script for performing bivariate analysis on supply chain data. The analysis includes importing the dataset, visualizing relationships between variables using scatter plots, and calculating correlations and average deviations.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [License](#license)

## Overview

The script performs the following tasks:
1. Imports necessary libraries.
2. Connects to Google Drive to access the dataset.
3. Loads the supply chain data.
4. Displays the first few rows of the dataset.
5. Creates scatter plots to visualize relationships between variables.
6. Calculates and prints correlation coefficients between variables.
7. Computes and prints the average deviation of prices for each availability category.

## Installation

To install the necessary libraries, run the following commands:

```bash
pip install pandas numpy matplotlib seaborn

from google.colab import drive
drive.mount('/content/gdrive', force_remount=True)
root_dir = "/content/gdrive/My Drive/"

# Load the Dataset
df = pd.read_csv(r'/content/gdrive/My Drive/supply_chain_data.csv')

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Load and Display Data
df = pd.read_csv(r'/content/gdrive/My Drive/supply_chain_data.csv')
df.head()
print(df.head())

#Scatter Plot and Correlation
sns.scatterplot(data=df, x='Price', y='Number of products sold')
plt.show()

correlation = df[['Price', 'Number of products sold']].corr()
print(correlation)

sns.scatterplot(data=df, x='Availability', y='Location')
plt.show()

correlation = df[['Availability', 'Location']].corr()
print(correlation)

# Calculate Average Deviation

average_deviation = df.groupby('Availability')['Price'].mad().reset_index()
print('Average Deviation for each category:')
print(average_deviation)

pip install pandas numpy matplotlib seaborn

# This `README.md` file provides a comprehensive guide to setting up and using the script, including installation steps, setup instructions, and usage examples. Adjust the file paths and any specific details as needed.

