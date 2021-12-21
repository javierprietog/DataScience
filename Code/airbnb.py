## Example - Barcelona Airbnb listings ##

# Importing the data #
import pandas as pd
url = 'https://raw.githubusercontent.com/mcanela-iese/DataScience/main/Data/airbnb.csv'
df = pd.read_csv(url, index_col=0)
df.info()
df.isna().sum()
df.head()

# Counting duplicates #
df.index.duplicated().sum()
df.duplicated().sum()

# How are the hosts? #
df['host_id'][df['host_since'] < '2010-01-01'].value_counts()
df['host_id'].unique()
df['host_id'].unique().shape
(df['host_id'].value_counts() == 1).sum()
df['host_id'].value_counts().head(10)
(df['host_id'].value_counts() > 10).mean().round(3)

# Distribution of the price #
df['price'].plot.hist(figsize=(8,6), color='gray', rwidth=0.98);
df['price'].describe()
df['price'][(df['price'] >= 25) & (df['price'] <= 150)].plot.hist(figsize=(8,6),
  color='gray', rwidth=0.94, bins=25);

# Average price per room type #
df.groupby(by='room_type')['price'].mean().round()
df.groupby(by='room_type')['price'].median()

# Top-10 neighbourhoods #
df['neighbourhood'].value_counts().head(10)
df.groupby(by='neighbourhood')['price'].agg(['count', 'median']).sort_values(by='count',
  ascending=False).head(10)
