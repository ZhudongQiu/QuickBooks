# main

import mylib.datahandler
import mylib.modeler
import mylib.dataextraction 

import pandas as pd

from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost.sklearn import XGBRegressor

def main():
    #Dataextraction
    data = mylib.dataextraction.import_json("qbs_json.json")

    Date = mylib.dataextraction.get_date(data)
    Net_Income = mylib.dataextraction.get_net_income(data)
    Gross_Profit = mylib.dataextraction.get_gross_profit(data)
    Total_Expenses = mylib.dataextraction.get_total_expenses(data)
    Total_Other_Expenses = mylib.dataextraction.get_total_other_expenses(data)
    Total_amount_of_Invoice = mylib.dataextraction.get_total_amount_of_invoice(data)
    Net_Operating_Income = mylib.dataextraction.get_net_operating_income(data)
    Total_amount_of_Bill = mylib.dataextraction.get_total_amount_of_bill(data)
    Total_Bank_Accounts = mylib.dataextraction.get_total_bank_accounts(data)
    Total_Accounts_Receivable = mylib.dataextraction.get_total_accounts_receivable(data)
    Total_Current_Assets = mylib.dataextraction.get_total_current_assets(data)
    Total_Assets = mylib.dataextraction.get_total_assets(data)
    Total_Accounts_Payable = mylib.dataextraction.get_total_accounts_payable(data)
    Total_Current_Liabilities = mylib.dataextraction.get_total_current_liabilities(data)
    Total_Liabilities = mylib.dataextraction.get_total_liabilities(data)
    Total_Equity = mylib.dataextraction.get_total_equity(data)

    dic = {"Date" : Date,
           "Net_Income": Net_Income,
           "Gross_Profit" : Gross_Profit,
           "Total_Expenses" : Total_Expenses,
           "Total_Other_Expenses" : Total_Other_Expenses,
           "Total_amount_of_Invoice" : Total_amount_of_Invoice,
           "Net_Operating_Income" : Net_Operating_Income,
           "Total_amount_of_Bill" : Total_amount_of_Bill,
           "Total_Bank_Accounts" : Total_Bank_Accounts,
           "Total_Accounts_Receivable" : Total_Accounts_Receivable,
           "Total_Current_Assets" : Total_Current_Assets,
           "Total_Assets" : Total_Assets,
           "Total_Accounts_Payable" : Total_Accounts_Payable,
           "Total_Current_Liabilities" : Total_Current_Liabilities,
           "Total_Liabilities" : Total_Liabilities,
           "Total_Equity" : Total_Equity}

    pd.DataFrame(dic).to_csv("Data.csv", index=False)

    # Prepare data for build model
    mylib.datahandler.info()

    mylib.datahandler.corr()

    # Build Model
    model_df = pd.read_csv("Features.csv")
    train, test = mylib.modeler.tts(model_df)

    # Model 1 - Linear regression
    Linear_Regression = mylib.modeler.regressive_model(train, test, LinearRegression(), 'LinearRegression')

    # Model 2 - Random forest regression
    Random_Forest = mylib.modeler.regressive_model(train, test, RandomForestRegressor(n_estimators = 10), 'RandomForest')

    # Model 3 - XGBoost
    XGBoost = mylib.modeler.regressive_model(train, test, XGBRegressor(n_estimators=100, learning_rate=0.2, objective='reg:squarederror'),'XGBoost')

    # Model 4 - Long Short - Term Memory
    LSTM = mylib.modeler.lstm_model(train, test)

    # Use Moving average to predict features
    MovingAverage = mylib.modeler.MA("Net_Income")

    #Save output to json file
    mylib.modeler.to_json(Linear_Regression)
    mylib.modeler.to_json(Random_Forest)
    mylib.modeler.to_json(XGBoost)
    mylib.modeler.to_json(LSTM)
    mylib.modeler.to_json(MovingAverage)
    
