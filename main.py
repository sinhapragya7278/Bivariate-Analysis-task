# import library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import drive
drive.mount('/content/gdrive', force_remount=True)
root_dir = "/content/gdrive/My Drive/"
df = pd.read_csv(r'/content/gdrive/My Drive/supply_chain_data.csv')
# import dataset
df = pd.read_csv(r'/content/gdrive/My Drive/supply_chain_data.csv')
df.head()
print(df.head())
sns.scatterplot(data=df, x='Price', y='Number of products sold')
plt.show()
correlation = df[['Price', 'Number of products sold']].corr()
print(correlation)
sns.scatterplot(data=df, x='Availability', y='Location')
plt.show()
correlation = df[['Availability', 'Location']].corr()
print(correlation)
# Average Deviation for each category
average_deviation = df.groupby('Availability')['Price'].mad().reset_index()
print('Average Deviation for each category:')
print(average_deviation)
