# main.py

import mylib

from mylib.dataextraction import *
from mylib.config import *
from mylib.datahandler import *
from mylib.modeler import *

#Dataextraction
data = import_json("qbs_json.json")

Date = get_date(data)
Net_Income = get_net_income(data)
Gross_Profit = get_gross_profit(data)
Total_Expenses = get_total_expenses(data)
Total_Other_Expenses = get_total_other_expenses(data)
Total_amount_of_Invoice = get_total_amount_of_invoice(data)
Net_Operating_Income = get_net_operating_income(data)
Total_amount_of_Bill = get_total_amount_of_bill(data)
Total_Bank_Accounts = get_total_bank_accounts(data)
Total_Accounts_Receivable = get_total_accounts_receivable(data)
Total_Current_Assets = get_total_current_assets(data)
Total_Assets = get_total_assets(data)
Total_Accounts_Payable = get_total_accounts_payable(data)
Total_Current_Liabilities = get_total_current_liabilities(data)
Total_Liabilities = get_total_liabilities(data)
Total_Equity = get_total_equity(data)

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
info()

corr()

# Build Model
model_df = pd.read_csv("Features.csv")
train, test = tts(model_df)

# Model 1 - Linear regression
Linear_Regression = regressive_model(train, test, LinearRegression(), 'LinearRegression')

# Model 2 - Random forest regression
Random_Forest = regressive_model(train, test, RandomForestRegressor(n_estimators=Config['RandomForestRegressor_setting']['n_estimators']), 'RandomForest')

# Model 3 - XGBoost
XGBoost = regressive_model(train, test, XGBRegressor(n_estimators=Config['XGBRegressor_setting']['n_estimators'],
                                                     learning_rate=Config['XGBRegressor_setting']['learning_rate'],
                                                     objective='reg:squarederror'),'XGBoost')

# Model 4 - Long Short - Term Memory
LSTM = lstm_model(train, test)

#Save output to json file
to_json(Linear_Regression)
to_json(Random_Forest)
to_json(XGBoost)
to_json(LSTM)
    
# Use Moving average to predict features
get_months_feature(Config["Number_months_forecast"])

# Import model to predict
test = pd.read_csv('forecast_feature.csv')
model = joblib.load('LinearRegression.pkl')
result = model.predict(test)[3:]

# Save prediction to Json File
month =  get_date_num(Config["Number_months_forecast"])

pred_df = pd.DataFrame(zip(month,result), columns = ['Date', 'prediction'])
pred_dic = pred_df.set_index("Date").T.to_dict('list')
pred_outcome = {"LinearRegression" : pred_dic}

jsonData = json.dumps(pred_outcome, indent=1)
fileObject = open("future_prediction.json", 'a+')
fileObject.write(jsonData)
fileObject.close()
