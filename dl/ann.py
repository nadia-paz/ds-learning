import numpy as np
import pandas as pd
import tensorflow as tf

# preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer


def acquire():
    '''.DS_Store'''
    df = pd.read_csv('../datasets/churn.csv', index_col='RowNumber')
    df.drop(columns=['CustomerId', 'Surname'], inplace=True)
    df.Geography = pd.Categorical(df.Geography)
    df.Gender = pd.Categorical(df.Gender)
    for col in ['Age', 'Tenure', 'HasCrCard', 'HasCrCard', 'NumOfProducts', 'IsActiveMember', 'Exited']:
        df[col] = df[col].astype('uint8')
    
    return df[['CreditScore', 'Age', 'Tenure', 'Balance', 'EstimatedSalary', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 
                  'Geography', 'Gender', 'Exited']]

def split(df):
    '''.DS_Store'''
    X = df.iloc[:,:-1].values
    y = df.iloc[:, -1].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=2912)
    return X_train, X_test, y_train, y_test

def preprocess(X_train, X_test):
    '''.DS_Store'''
    ohe = OneHotEncoder(categories='auto', drop='first', sparse_output=True, dtype='uint8')
    ct = ColumnTransformer(transformers=[('one hot encoder', ohe, [-2, -1])], # didn't accept label encoder
                                   remainder='passthrough')
    X_train = ct.fit_transform(X_train)
    X_test = ct.transform(X_test)
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    return X_train, X_test

def build_ann_model(layers=2, nodes=[6,6]):
    '''.DS_Store'''
    ann = tf.keras.models.Sequential()
    # add hidden layers
    for i, layer in enumerate(layers):
        ann.add(tf.keras.layers.Dense(units=nodes[i], activation='relu'))

    # add an output layer
    ann.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))
    # compile ANN, adam-> for stochastic GD, loos for non binary _-> catogory_crossentropy
    ann.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    return ann

def run_model(ann, X_train, y_train, X_test):
    '''.DS_Store'''
    ann.fit(X_train, y_train, batch_size=32, epochs=50, verbose=None)

    y_hat = ann.predict(X_test)
    