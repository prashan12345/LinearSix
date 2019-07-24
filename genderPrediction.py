from sklearn import tree

#[between 10 and 20 for male].[between 20 and 30 for female]
X = [[10,20], [23,25], [12,15], [14,16],
     [25,29], [30,27], [19,10], [17,14],
     [22,22], [12,18], [30,28]]

Y = ['male' , 'female', 'male', 'male',
     'female', 'female', 'male',
      'male', 'female', 'male', 'female']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)

prediction = clf.predict([[30,2]])

print (prediction)

