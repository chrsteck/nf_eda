import statsmodels.api as sms
import statsmodels.formula.api as smf
import pandas as pd


def modelz():
    df = pd.read_csv('/Users/christiansteck/neuefische/nf_eda/datasets/training-set.csv')
    coeffs = ['bathrooms*ren', 'sqft_living*ren', 'bedrooms', 'C(floors)', 'C(zipcode)', 'sqft_living15*ren', 'age*ren', 'grade*ren']
    modelz = smf.ols(formula='price ~ '+' + '.join(coeffs), data=df).fit()

    with open('/Users/christiansteck/neuefische/nf_eda/model/model_summary.txt', 'w') as fh:
        fh.write(modelz.summary().as_text())

    print(modelz.summary())
    modelz.save("/Users/christiansteck/neuefische/nf_eda/model/regression_with_interaction.pickle")

modelz()