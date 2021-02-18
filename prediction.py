import statsmodels.api as sms
import pandas as pd
from sklearn.metrics import mean_squared_error

model = sms.load('model/regression_with_interaction.pickle')


def prediction_mod():
    print('Welcome to the prediction module')
    load = input('Enter dataset path and name for prediction: ')
    save = input('Enter path and name for new dataset with predictions: ')
    df = pd.read_csv(load)
    pred = model.predict(df)
    df['prediction'] = pred
    df.to_csv(save)
    rms = mean_squared_error(df.price, df.prediction, squared=False)
    print(f'RMSE = {rms}')
    print(f'dataset saved under {save}')


prediction_mod()