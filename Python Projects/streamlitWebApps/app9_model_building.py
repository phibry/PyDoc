# import pandas as pd
# penguins = pd.read_csv('doc/penguins_cleaned.csv')
# df = penguins.copy()
# target = 'species'
# encode = ['sex','island']

# # Encoding Sex and Island
# for col in encode:
#     dummy = pd.get_dummies(df[col], prefix=col)
#     df = pd.concat([df,dummy], axis=1)
#     del df[col]

# # Species
# target_mapper = {'Adelie':0, 'Chinstrap':1, 'Gentoo':2}
# def target_encode(val):
#     return target_mapper[val]

# df['species'] = df['species'].apply(target_encode)

# # Separating X and y
# X = df.drop('species', axis=1)
# Y = df['species']

# # Build random forest model
# from sklearn.ensemble import RandomForestClassifier
# clf = RandomForestClassifier()
# clf.fit(X, Y)

# # Saving the model
# import pickle
# pickle.dump(clf, open('doc/penguins_clf.pkl', 'wb'))







import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestRegressor
import pickle


# Load Data
boston = datasets.load_boston()

# Split into Training Dataset and Target Dataset
X = pd.DataFrame(boston.data, columns=boston.feature_names)
Y = pd.DataFrame(boston.target, columns=["MEDV"])
# with parameters in X, we can predict Y.

model = RandomForestRegressor()
model.fit(X, Y)


pickle.dump(model, open('doc/boston_clf.pkl', 'wb'))