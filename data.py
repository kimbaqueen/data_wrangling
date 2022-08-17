import pandas as pd

df = pd.read_csv('Street_Tree_List.csv')

# *************** Step 1: Exploration ************

print(df.info())

print(df.describe())

print(df.head(3))

print(df.columns)

print(len(df))
tree_species = df['qSpecies'].value_counts()
print(df['qSpecies'].value_counts())

print(df['Zip Codes'].value_counts())

# ********** Step 2: Select, Filter, Sort using DataFrames**********

print(df.loc[0, :])
print(df.loc[df.qLegalStatus == 'Private', 'TreeID'])
print(df.loc[df.qCaretaker == 'Rec/Park', 'TreeID'])
print(df.sort_values(by=tree_species, ascending=False))

# ************************ Step 3: Clean Data **********************

print(df['SiteOrder'].min())
print(df['SiteOrder'].max())
print(df.loc[df.SiteOrder == -50.0, :])
print(df.loc[df.SiteOrder == 1700, :])

# ************************ Step 4: Transform Data **********************
print(df.info('PlantDate')) 
# PlantDate is an object. Convert to datetime object
df['PlantDate'] = pd.to_datetime(df['PlantDate'])
print(df.info('PlantDate')) 
# SUCESS!!!! now showing datetime64[ns] instead of object
# extracting time out of PlantDate timestamp column into own seperate column:
print(df['PlantDate'].dt.time)
df['PlantTime'] = df['PlantDate'].dt.time
print(df['PlantDate'])
print(df['PlantTime'])