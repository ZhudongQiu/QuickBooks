# dataextracttion

"""Get data from json file and input to csv."""
import json

def import_json(name):
    return json.load(open(name, 'rb'))

def get_date(data):
    date = []

    i = 1
    while i < len(data["GetBalanceSheet"]["Columns"]["Column"]):
        date.append(data["GetBalanceSheet"]["Columns"]["Column"][i]["MetaData"][0]['Value'][0:7])
        i = i + 1
        
    return date

def get_date_length(data):
    return len(get_date(data))
    
def get_net_income(data):
    net_income = []
    Get_Net_Income = 0

    i = 1
    while i < 26:
        Get_Net_Income = data["GetProfitAndLossReport"]["Rows"]['Row'][7]['Summary']['ColData'][i]['value']
        net_income.append(Get_Net_Income)
        i = i + 1
    return net_income

def get_gross_profit(data):
    gross_profit = []
    Get_Gross_Porfit = 0

    i = 1
    while i < 26:
        Get_Gross_Profit = data["GetProfitAndLossReport"]["Rows"]['Row'][2]['Summary']['ColData'][i]['value']
        gross_profit.append(Get_Gross_Profit)
        i = i + 1
    return gross_profit

def get_total_expenses(data):
    total_expenses = []
    Get_Total_Expenses = 0

    i = 1
    while i < 26:
        Get_Total_Expenses = data["GetProfitAndLossReport"]["Rows"]['Row'][3]['Summary']['ColData'][i]['value']
        total_expenses.append(Get_Total_Expenses)
        i = i + 1
    return total_expenses

def get_net_operating_income(data):
    net_operating_income = []
    Get_Total_Net_Operating_Income = 0

    i = 1
    while i < 26:
        Get_Total_Net_Operating_Income = data["GetProfitAndLossReport"]["Rows"]['Row'][4]['Summary']['ColData'][i]['value']
        net_operating_income.append(Get_Total_Net_Operating_Income)
        i = i + 1
    return net_operating_income

def get_total_other_expenses(data):
    total_other_expenses = []
    Get_Total_Other_Expenses = 0

    i = 1
    while i < 26:
        Get_Total_Other_Expenses = data["GetProfitAndLossReport"]["Rows"]['Row'][5]['Summary']['ColData'][i]['value']
        total_other_expenses.append(Get_Total_Other_Expenses)
        i = i + 1
    return total_other_expenses

def sum_of_month(date):
    sum = 0
    for i in date:
        sum = sum + i
    return sum

def get_total_amount_of_bill(data):
    bills = []
    one_bill = []
    Date = 0
    Amount = 0
    
    b = {}
    new_get_date = []
    month1,month2,month3,month4,month5,month6,month7,month8,month9 = [],[],[],[],[],[],[],[],[]

    i = 0
    while i < len(data["BillQueryRaw"]["QueryResponse"]["Bill"]):
        Date = data["BillQueryRaw"]["QueryResponse"]["Bill"][i]["DueDate"][0:7]
        Amount = data["BillQueryRaw"]['QueryResponse']['Bill'][i]["TotalAmt"]
        one_bill = [Date, Amount]
        bills.append(one_bill)
        i = i + 1

    for k in bills:
        date = k[0]
        new_get_date.append(date)
    new_get_date.sort(reverse=True)
    month = b.fromkeys(new_get_date)
    date_new = list(month.keys())
    date_new.insert(4, "2020-05")

    for d in date_new:
        if d not in get_date(data):
            date_new.remove(d)

    for cal in bills:
        if cal[0] == date_new[0]:
            month1.append(cal[1])
        elif cal[0] == date_new[1]:
            month2.append(cal[1])
        elif cal[0] == date_new[2]:
            month3.append(cal[1])
        elif cal[0] == date_new[3]:
            month4.append(cal[1])
        elif cal[0] == date_new[4]:
            month5.append(cal[1])
        elif cal[0] == date_new[5]:
            month6.append(cal[1])
        elif cal[0] == date_new[6]:
            month7.append(cal[1])
        elif cal[0] == date_new[7]:
            month8.append(cal[1])
        elif cal[0] == date_new[8]:
            month9.append(cal[1])

    total_amount_of_bill = [sum_of_month(month1),sum_of_month(month2),
                            sum_of_month(month3),sum_of_month(month4),
                            sum_of_month(month5),sum_of_month(month6),
                            sum_of_month(month7),sum_of_month(month8)]

    while len(total_amount_of_bill) < get_date_length(data):
        total_amount_of_bill.append(0)

    new_total_amount_of_bill = total_amount_of_bill[::-1]

        
    return new_total_amount_of_bill


def get_total_current_assets(data):
    total_current_assets = []
    Get_Total_Current_Assets = 0

    i = 1
    while i < len(data["GetBalanceSheet"]["Rows"]["Row"][0]["Rows"]["Row"][0]["Summary"]["ColData"]):
        Get_Total_Current_Assets = data["GetBalanceSheet"]["Rows"]["Row"][0]["Rows"]["Row"][0]["Summary"]["ColData"][i]["value"]
        total_current_assets.append(Get_Total_Current_Assets)
        i = i + 1

    return total_current_assets

def get_total_bank_accounts(data):
    total_bank_accounts = []
    Get_Total_Bank_Accounts = 0

    i = 1
    while i < len(data["GetBalanceSheet"]["Rows"]["Row"][0]["Rows"]["Row"][0]["Rows"]["Row"][0]["Summary"]["ColData"]):
        Get_Total_Bank_Accounts = data["GetBalanceSheet"]["Rows"]["Row"][0]["Rows"]["Row"][0]["Rows"]["Row"][0]["Summary"]["ColData"][i]["value"]
        total_bank_accounts.append(Get_Total_Bank_Accounts)
        i = i + 1

    return total_bank_accounts

def get_total_accounts_receivable(data):
    total_accounts_receivable = []
    Get_Total_Accounts_Receivable = 0

    i = 1
    while i < len(data["GetBalanceSheet"]["Rows"]["Row"][0]["Rows"]["Row"][0]["Rows"]["Row"][1]["Summary"]["ColData"]):
        Get_Total_Accounts_Receivable  = data["GetBalanceSheet"]["Rows"]["Row"][0]["Rows"]["Row"][0]["Rows"]["Row"][1]["Summary"]["ColData"][i]["value"]
        total_accounts_receivable.append(Get_Total_Accounts_Receivable )
        i = i + 1

    return total_accounts_receivable

def get_total_assets(data):
    total_assets = []
    Get_Total_Assets = 0

    i = 1
    while i <len(data["GetBalanceSheet"]["Rows"]["Row"][0]["Summary"]["ColData"]):
        Get_Total_Assets = data["GetBalanceSheet"]["Rows"]["Row"][0]["Summary"]["ColData"][i]["value"]
        total_assets.append(Get_Total_Assets)
        i = i + 1

    return total_assets

def get_total_current_liabilities(data):
    total_current_liabilities = []
    Get_Total_Current_Liabilities = 0

    i = 1
    while i < len(data["GetBalanceSheet"]["Rows"]["Row"][1]["Rows"]["Row"][0]["Rows"]["Row"][0]["Summary"]["ColData"]):
        Get_Total_Current_Liabilities = data["GetBalanceSheet"]["Rows"]["Row"][1]["Rows"]["Row"][0]["Rows"]["Row"][0]["Summary"]["ColData"][i]["value"]
        total_current_liabilities.append(Get_Total_Current_Liabilities)
        i = i + 1

    return total_current_liabilities

def get_total_accounts_payable(data):
    total_accounts_payable = []
    Get_Total_Accounts_Payable = 0

    i = 1
    while i < len(data["GetBalanceSheet"]["Rows"]["Row"][1]["Rows"]["Row"][0]["Rows"]["Row"][0]["Rows"]["Row"][0]["Summary"]["ColData"]):
        Get_Total_Accounts_Payable = data["GetBalanceSheet"]["Rows"]["Row"][1]["Rows"]["Row"][0]["Rows"]["Row"][0]["Rows"]["Row"][0]["Summary"]["ColData"][i]["value"]
        total_accounts_payable.append(Get_Total_Accounts_Payable)
        i = i + 1

    return total_accounts_payable

def get_total_liabilities(data):
    total_liabilities = []
    Get_Total_Liabilities = 0

    i = 1
    while i < len(data["GetBalanceSheet"]["Rows"]["Row"][1]["Rows"]["Row"][0]["Summary"]["ColData"]):
        Get_Total_Liabilities = data["GetBalanceSheet"]["Rows"]["Row"][1]["Rows"]["Row"][0]["Summary"]["ColData"][i]["value"]
        total_liabilities.append(Get_Total_Liabilities)
        i = i + 1

    return total_liabilities

def get_total_equity(data):
    total_equity = []
    Get_Total_Equity = 0

    i = 1
    while i < len(data["GetBalanceSheet"]["Rows"]["Row"][1]["Rows"]["Row"][1]["Summary"]["ColData"]):
        Get_Total_Equity = data["GetBalanceSheet"]["Rows"]["Row"][1]["Rows"]["Row"][1]["Summary"]["ColData"][i]["value"]
        total_equity.append(Get_Total_Equity)
        i = i + 1

    return total_equity

def get_total_amount_of_invoice(data):
    invoice = []
    one_invoice = []
    Date = 0
    Amount = 0

    b = {}
    new_get_date = []
    month1,month2,month3,month4,month5,month6,month7,month8,month9,month10,month11,month12,month13,month14 = [],[],[],[],[],[],[],[],[],[],[],[],[],[]

    i = 0
    while i < len(data["InvoiceQueryRaw"]["QueryResponse"]["Invoice"]):
        Date = data["InvoiceQueryRaw"]["QueryResponse"]["Invoice"][i]["TxnDate"][0:7]
        Amount = data["InvoiceQueryRaw"]["QueryResponse"]["Invoice"][i]["TotalAmt"]
        one_invoice = [Date, Amount]
        invoice.append(one_invoice)
        i = i + 1

    for k in invoice:
        date = k[0]
        new_get_date.append(date)
    new_get_date.sort(reverse=True)
    month = b.fromkeys(new_get_date)
    date_new = list(month.keys())
    date_new.insert(9, "2020-01")
    date_new.insert(10, "2019-12")

    for d in date_new:
        if d not in get_date(data):
            date_new.remove(d)

    for cal in invoice:
        if cal[0] == date_new[0]:
            month1.append(cal[1])
        elif cal[0] == date_new[1]:
            month2.append(cal[1])
        elif cal[0] == date_new[2]:
            month3.append(cal[1])
        elif cal[0] == date_new[3]:
            month4.append(cal[1])
        elif cal[0] == date_new[4]:
            month5.append(cal[1])
        elif cal[0] == date_new[5]:
            month6.append(cal[1])
        elif cal[0] == date_new[6]:
            month7.append(cal[1])
        elif cal[0] == date_new[7]:
            month8.append(cal[1])
        elif cal[0] == date_new[8]:
            month9.append(cal[1])
        elif cal[0] == date_new[9]:
            month10.append(cal[1])
        elif cal[0] == date_new[10]:
            month11.append(cal[1])
        elif cal[0] == date_new[11]:
            month12.append(cal[1])
        elif cal[0] == date_new[12]:
            month13.append(cal[1])
        elif cal[0] == date_new[13]:
            month14.append(cal[1])


    total_amount_of_invoice = [sum_of_month(month1),sum_of_month(month2),
                               sum_of_month(month3),sum_of_month(month4),
                               sum_of_month(month5),sum_of_month(month6),
                               sum_of_month(month7),sum_of_month(month8),
                               sum_of_month(month9),sum_of_month(month10),
                               sum_of_month(month11),sum_of_month(month12),
                               sum_of_month(month13),sum_of_month(month14)]

    while len(total_amount_of_invoice) < get_date_length(data):
        total_amount_of_invoice.append(0)

    new_total_amount_of_invoice = total_amount_of_invoice[::-1]

    return new_total_amount_of_invoice
