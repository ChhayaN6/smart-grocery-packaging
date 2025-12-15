import os
os.system('cls') 
import json, requests, time
import pyrebase
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

config = {
  "apiKey": "DoVgdZGYciUs0fdPVWDc10LNIkWxb3iY7S7oNfND",
  "authDomain": "smartpackage-f3896-default-rtdb.firebaseio.com",
  "databaseURL": "https://smartpackage-f3896-default-rtdb.firebaseio.com",
  "storageBucket": "smartpackage-f3896-default"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
print(db)

ad=pd.read_csv("./dataset.csv")
ad.shape
ad.info()
ad.describe()
ad.head()
print(ad)
y = ad['Result'].values
X = ad.drop('Result', axis=1).values 
knn = KNeighborsClassifier(n_neighbors=6)
knn.fit(X,y)
y_pred = knn.predict(X)

while True:
   
    temperature = db.child("Temperature").get()
    a=temperature.val()
    print(a)

    humidity = db.child("Humidity").get()
    b=humidity.val()
    print(b)

    mq135 = db.child("Air:").get()
    c=mq135.val()
    print(c)

    #x_new = [int(temperature),int(humidity),int(moist),int(smoke)]
    x_new = [a,b,c]
    new_pred = knn.predict([x_new])
    type(new_pred)
    print("Prediction : {}".format(new_pred))

    db.update({"OUTPUT":new_pred[0]})
    time.sleep(5)
