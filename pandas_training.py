import pandas as pd
import numpy as np

df = pd.read_csv("data/TG_STAID000001.txt", skiprows=20, parse_dates=["    DATE"]) # Preskočimo 20 prvih vrstic in date nam pretvori v bolj berljivo obliko

### SIMPLE STATISTICS AND FILTERING ###
average = df.loc[df['   TG'] != -9999]['   TG'].mean() / 10 # sfiltriramo avg. temp.
maximum = df.loc[df['   TG'] != -9999]['   TG'].max() / 10
print(f"Average: {average}")
print(f"Maximum: {maximum}")

### RISANJE GRAFA ###
# df.loc[df['   TG'] != -9999]['   TG'].hist() # Risanje grafa

### GET CERTAIN CELLS ###
temp_on_date = df.loc[df["    DATE"] == "1860-01-05"]['   TG'].squeeze() / 10
print(f"Temp on date: {temp_on_date}")
### GET CERTAIN CELLS - MAXIMUM ###
max_cell = df.loc[df['   TG'] == df['   TG'].max()]["    DATE"].squeeze()
print(f"Max temp: {max_cell}")

### CALCULATE A NEW COLUMN OUT OF EXISTING COLUMN ###
df["TG0"] = df['   TG'].mask(df['   TG'] == -9999, np.nan) # mask pomeni without. Torej naredimo nov column without -9999
df["TG"] = df['TG0'] / 10
df["FAHRENHEIT"] = df['TG'] * (9/5) + 32
print(df)

### PLOTTING ###
# df["TG"].hist()
# df.plot(x="    DATE", y="TG", figsize=(15,3))
# df[10:1000].plot(x="    DATE", y="TG", figsize=(15,3))

### EXAMPLES ###
#print(df.columns)
#print(df[['   TG', '    DATE']])