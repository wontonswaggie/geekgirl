import csv
import pandas
import numpy 
from sklearn.tree import DecisionTreeRegressor
from sklearn import cross_validation
from sklearn.metrics import mean_squared_error

# Process songs
songs = pandas.read_csv('music.csv', header=None)
songs.columns = ['Song_ID', 'Title', 'Singer', 'Tempo', 'Genre']
print songs.head(5)
songs = pandas.get_dummies(songs[['Song_ID', 'Tempo','Genre']], columns = ['Genre'])
print songs.head(5)

# Process users
users = pandas.read_csv('users.csv', header=None)
users.columns = ['User_ID', 'Name', 'Age', 'Gender']
print users.head(5)
users = pandas.get_dummies(users[['User_ID', 'Age', 'Gender']], columns = ['Gender'])
print users.head(5)

# Process preferences
preferences = pandas.read_csv('preferences.csv', header=None)
preferences.columns = ['User_ID', 'Song_ID']
preferences['Preferred'] = 1
print preferences.head(5)

# Combine all the data together
combo = pandas.DataFrame(numpy.vstack(numpy.concatenate((ss, uu), axis=0) for ss in songs.as_matrix() for uu in users.as_matrix()))
l = list(songs.columns.values)
l.extend(list(users.columns.values))
combo.columns = l
print combo.head(5)

combo = combo.merge(preferences, 'left', on = ['Song_ID', 'User_ID'])
combo.fillna(0, inplace=True)
combo.set_index(['Song_ID', 'User_ID'], inplace=True)
print combo.head(5)


y = combo['Preferred'].as_matrix()

combo.drop(['Preferred'], axis=1, inplace=True)
X = combo.as_matrix()

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2, random_state=0)

estimator = DecisionTreeRegressor()
estimator.fit(X_train,y_train)
y_pred = estimator.predict(X_test)
print mean_squared_error(y_test, y_pred)
