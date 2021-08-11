import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import warnings
import pickle
warnings.filterwarnings("ignore")

df= pd.read_csv("insurance_new.csv")
df.drop('Unnamed: 0',axis =1, inplace=True)

x = df.iloc[:, :-1].values
y = df.iloc[:,-1].values

xtrain,xtest,ytrain,ytest = train_test_split(x,y, test_size=0.3, random_state = 0)

rf = RandomForestRegressor(bootstrap=True,
 max_depth= 90,
 max_features= 3,
 min_samples_leaf =3,
 min_samples_split= 6,
 n_estimators= 200)
rf.fit(xtrain,ytrain)

pickle_out = open('model.pkl','wb')
pickle.dump(rf,pickle_out)
pickle_out.close()



