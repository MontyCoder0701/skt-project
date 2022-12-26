# Import libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets
import streamlit as st

# Get the dataset
dataset = datasets.load_iris()

# Split the dataset into features and labels
X = dataset.data
y = dataset.target

# Split the dataset into training (80%) and testing (20%) data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0, shuffle=True)

# Build the classifier and make prediction
classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)
prediction = classifier.predict(X_test)

st.title("Iris Dataset")
# with st.form("my_form"):
#     try:
#         user_input = st.text_input(
#             "Enter the headline of the article you want to detect.")
#     except ValueError:
#         st.error(
#             "Please enter the article headline in a full english sentence format.")

#     submitted = st.form_submit_button("Submit")
#     if submitted:
#         data = tfidf_vectorizer.transform([user_input]).toarray()
#         with st.spinner(text="Detecting the validity..."):
#             time.sleep(3)
#             st.success("Detection complete.")
#         if len(user_input) == 0:
#             st.error(
#                 "The input is blank. Please try again.")
#         else:
#             match = re.search(r'[a-zA-Z]', user_input)
#             if match == None:
#                 st.error(
#                     "This is not a sentence. Please try again.")
#             else:
#                 st.text("The following article is " + pac.predict(data)[0])
#                 if pac.predict(data)[0] == "UNBIASED":
#                     st.balloons()
