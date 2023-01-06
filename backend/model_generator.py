# Import libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier
import joblib
from sklearn import datasets
from sklearn.preprocessing import LabelEncoder

# Get the dataset
df = pd.read_csv("penguins.csv")
df.dropna(subset=["bill_length_mm"], inplace=True)
df["sex"].fillna("NONE", inplace=True)

# Encode
df['species'] = df['species'].map({
    'Adelie': 0,
    'Chinstrap': 1,
    'Gentoo': 2,
})

# X feature encoding
df['island'] = df['island'].map({
    'Biscoe': 0,
    'Dream': 1,
    'Torgersen': 2,
})


df['sex'] = df['sex'].map({
    'MALE': 0,
    'FEMALE': 1,
    'NONE': 2,
})

print(df.describe().T)

# Split the dataset into features and labels
X = df.drop(['species'], axis=1)
y = df['species']

# Split the dataset into training (80%) and testing (20%) data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0, shuffle=True)

# Build the classifier and make prediction
classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)
prediction = classifier.predict(X_test)

# Save the model to disk
joblib.dump(classifier, 'classifier.joblib')
