import statsmodels.api as sms
import pandas as pd
from sklearn.metrics import mean_squared_error

model = sms.load('model/regression_with_interaction.pickle')


def count_prediction_mod():
    print('Welcome to the counterfactual prediction module')
    load = input('Enter dataset path and name for counterfactual prediction: ')
    save = input('Enter path and name for new dataset with profitable houses: ')
    profit = float(input('Enter the minimum profit: '))
    df = pd.read_csv(load)
    pred = model.predict(df)
    df['prediction'] = pred
    countdf=df.copy()
    countdf['ren']=1
    countpred = model.predict(countdf)
    df['count_prediction'] = countpred
    df['profit_pred']=df['count_prediction']-df['prediction']
    profdf=df[df['profit_pred']>=profit].copy()
    profdf.to_csv(save)
    perc_prof = round(100*(len(profdf['profit_pred'])/len(df['profit_pred'])),2)
    print(f'{perc_prof}% of houses have a predicted profit of at least {profit} USD')
    print(f'dataset with profitable houses saved under {save}')



count_prediction_mod()