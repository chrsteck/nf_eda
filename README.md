# nf_eda
Neue Fische project EDA

This repo contains an EDA of the Kings County housing prices dataset as well as a model to predict housing prices. The following files are in the repo:

* **house_renovation_analysis.ipynb** - a notebook containing the eda
* **savingthemodel.py** - a script training the model and saving the model as pickle and its summary as a text file
* **prediction.py** - a script predicting housing prices and calculating RMSE
* **counterfactual_prediciton.py** - a script that predicts the prices for unrenovated houses, the price if they were renovated and the difference and return the houses that make a manually set minimum profit
* **requirements.txt** - python virtual environment requirements
* **datasets** - a folder with all datasets
* **model** - a folder with the model and its summary