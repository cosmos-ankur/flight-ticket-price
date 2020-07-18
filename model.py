import pandas as pd 
df = pd.read_csv('final.csv')
x = df[['Airline', 'Source', 'Destination', 'Total_Stops',
       'Additional_Info', 'Date', 'Month', 'Year', 'dep_hour', 'dep_mint',
       'arr_hour', 'arr_mint', 'hour_duration', 'mint_duration']]
y = df['Price']
from sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test =train_test_split(x,y,test_size = 0.25,random_state=101)
from sklearn.ensemble import RandomForestRegressor
forest = RandomForestRegressor(n_estimators=200)
forest.fit(x_train,y_train)
print(forest.score(x_test,y_test))

import pickle
# open a file, where you ant to store the data
file = open('model.pkl', 'wb')

# dump information to that file
pickle.dump(forest, file)