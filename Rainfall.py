import pandas as pd

distwise=pd.read_csv('district wise rainfall normal.csv')

def give_Rainfall(district,month):
    rain=distwise[distwise['DISTRICT']==district]
    return rain[month].values

# print(give_Rainfall('RAIPUR','FEB')[0])