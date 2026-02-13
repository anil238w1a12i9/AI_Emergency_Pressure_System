from sklearn.linear_model import LinearRegression
import numpy as np

def predict_pressure(accidents, ambulance):
    X = accidents[['accident_count']].values
    y = ambulance['ambulance_arrivals'].values

    model = LinearRegression()
    model.fit(X, y)

    predicted = model.predict(X)
    return predicted
