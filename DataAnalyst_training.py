import pandas as pd

df = pd.read_csv("wines/wines.csv")
count = 0

# HOW MANY RATINGS HAS GIVEN 100 POINTS
count_100 = len(df.loc[df['points'] == 100]['points'].squeeze())
print(count_100)
# WHAT IS THE NAME OF THE MOST EXPENSIVE WINE?
name = df.loc[df['price'] == df['price'].max()]['name'].squeeze()
print(name)
# CALCULATE A NEW COLUMN WHERE YOU SHOW THE RATINGS IN A SCALE FROM 0 to 5.
df['scale'] = (df['points'] / 100) * 5
print(df[['points', 'scale']])

### USE JUPYTER FOR THIS ###

# CREATE A PRICE HISTOGRAM FOR WINES THAT COST LESS THAN 100
# df.loc[df['price'] < 100]["price"].hist()
# PLOT PRICE HORIZONTALLYY AGAINST POINTS VERTICALLY
# df.plot(x="price", y="points", figsize=(15,3), kind="scatter")
