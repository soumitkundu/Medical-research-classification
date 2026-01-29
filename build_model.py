import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, classification_report
from sklearn.neighbors import KNeighborsClassifier
from scipy.stats import zscore  # Not recommended on data separated with training and testing
from sklearn.preprocessing import StandardScaler  # Instead apply StandardScaler for proper z-score normalization
# import pickle

import joblib

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
# from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Read the source files
normal = pd.read_csv('data/Normal.csv')
type_h = pd.read_csv('data/Type_H.csv')
type_s = pd.read_csv('data/Type_S.csv')

# Data Preprocessing
normal['Class'] = normal['Class'].apply(lambda x: 'normal')
type_s['Class'] = type_s['Class'].apply(lambda x: 'type_s')
type_h['Class'] = type_h['Class'].apply(lambda x: 'type_h')

# Combine the datasets
df = pd.concat([normal, type_s, type_h])

# Seperating into X features and y target
X = df.drop('Class',axis=1)
y = df['Class']
# Splitting into Train-Test
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 67, test_size = .2)

# Defining numerical features
numeric_features = X.select_dtypes(include=['int64', 'float64']).columns.tolist()


preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric_features)
    ]
)

pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor)
])

# KNN classifier with your specified hyperparameters
knn = KNeighborsClassifier(
    n_neighbors=9,
    weights="distance"
)

pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", knn)
])

# Train
pipeline.fit(X_train, y_train)

joblib.dump(pipeline, "models/best_model_pipeline.pkl")

# loading the pre-trained model
model = joblib.load(open('models/best_model_pipeline.pkl', 'rb'))

# Predict
y_pred = model.predict(X_test)

print(X_test.head())

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
# print("Classification Report:\n", classification_report(y_test, y_pred))
